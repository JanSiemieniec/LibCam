# LibCam Projekt README

Witaj w repozytorium projektu LibCam! 
Ten projekt ma na celu ułatwienie rozpoznawania twarzy studentów podczas wykładów.
Program wykorzystuje bibliotekę `Face_recognition` i potrzebuje tylko jednego zdjęcia studenta do dokładnej detekcji. 
Został stworzony, aby usprawnić proces rejestrowania obecności studentów na zajęciach.

## Opis Projektu

LibCam to system rozpoznawania twarzy dostosowany do środowiska akademickiego. 
Ułatwia prowadzenie listy obecności podczas wykładów, identyfikując twarze studentów za pomocą biblioteki `Face_recognition`.
Projekt kładzie nacisk na prostotę użycia, wymagając jedynie jednego zdjęcia każdego studenta do dokładnego rozpoznania. 
Projekt oparty jest na modelu wykorzystującym bibliotekę 'Face_recognition'. Model korzysta z jednego zdjęcia, 
które może pochodzić z bazy zdjęć studentów (każdy student posiada swoje zdjęcie w bazie z procesu tworzenia legitymacji studenckiej).

## Tworzenie pliku .csv jako listy obecności 

LibCam po każdym zakończeniu działania zapisuje listę obecnych i nieobecnych studentów w 
formie pliku .csv, aby lista mogła służyć jako dowód obecności studenta w razie niespodziewanych problemów.

## Wizualizacja wyników pracy
![](/wizualizacja.jpg)
## Twórcy projektu
- Jan Siemieniec s22596
- Maciej Salwin s22593
- Bartek Siemieniec s22793
