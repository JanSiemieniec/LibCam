import face_recognition
import cv2
from datetime import date
import os
import pandas as pd


def load_image_and_encode(file_path):
    img = face_recognition.load_image_file(file_path)

    face_locations = face_recognition.face_locations(img)

    if not face_locations:
        return None, None, None, None

    face_location = face_locations[0]
    face_encoding = face_recognition.face_encodings(img)[0]

    parts = file_path.split('/')
    filename_with_extension = parts[-1]

    filename, extension = filename_with_extension.split('.')
    return img, face_location, face_encoding, filename


def detect_participants():
    cap = cv2.VideoCapture(0)

    folder_path = 'Zdjęcia_SUML/'
    training_data = []  # all students
    present_students = []
    all_students_names = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        img, face_location, face_encoding, name = load_image_and_encode(file_path)
        all_students_names.append(name)
        if img is not None:
            training_data.append((img, face_encoding, name))

    for i in range(10):
        ret, frame = cap.read()

        face_locations = face_recognition.face_locations(frame)
        cv2.putText(frame, "Wszyscy studenci: " + str(len(training_data)), (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 150, 255), 2)
        n_present_students = 0

        if face_locations:
            for face_location in face_locations:
                test_encode = face_recognition.face_encodings(frame, [face_location])[0]

                # Porównywanie z danymi treningowymi
                found_match = False
                for _, train_encode, name in training_data:
                    results = face_recognition.compare_faces([train_encode], test_encode)
                    if results[0]:
                        cv2.putText(frame, name, (face_location[3], face_location[0] - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        cv2.rectangle(frame, (face_location[3], face_location[0]),
                                      (face_location[1], face_location[2]), (0, 255, 0), 2)
                        found_match = True
                        n_present_students += 1
                        present_students.append(name)
                        break

                if not found_match:
                    cv2.putText(frame, "Brak dopasowania", (face_location[3], face_location[0] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    cv2.rectangle(frame, (face_location[3], face_location[0]),
                                  (face_location[1], face_location[2]), (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Nie znaleziono twarzy!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.putText(frame, f"Obecni studenci: {n_present_students}", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 2)

        cv2.imshow('LibKam', frame)
        print(set(present_students))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    generate_csv(all_students_names, present_students)


def generate_csv(all_students, present_list_names):
    date_today = date.today().strftime("%Y-%m-%d")
    headers = ["Imie i nazwisko", f"Obecnosc {date_today}"]
    present_list = []

    for name in all_students:
        present_list.append("obecny" if name in present_list_names else "nieobecny")

    print(all_students)
    print(present_list)

    df = pd.DataFrame({headers[0]: all_students,
                       headers[1]: present_list
                       })
    df.to_csv(f"lista_obecnosci_{date_today}.csv", sep=';')


detect_participants()
