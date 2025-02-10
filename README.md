# Automat do wypełniania formularzy internetowych
Opis
Wykonany automat umożliwia automatyczne wypełnianie formularzy internetowych na podstawie danych pobranych z plików Excel. Program wykorzystuje bibliotekę Selenium do interakcji z formularzami online, wprowadzania danych oraz zatwierdzania formularzy. Celem projektu było uproszczenie i przyspieszenie procesu wprowadzania danych do formularzy internetowych, oszczędzając czas i eliminując błędy ludzkie.

# Funkcjonalności
Pobieranie danych z plików Excel (w formacie .xlsx)
Automatyczne wprowadzanie danych do formularzy internetowych
Zatwierdzanie formularzy po wypełnieniu
Użycie biblioteki Selenium do automatyzacji interakcji z przeglądarką

# Jak używać
Upewnij się, że masz zainstalowaną bibliotekę Selenium:

pip install selenium
Przygotuj plik Excel z danymi, które mają zostać wprowadzone do formularza.

Uruchom skrypt Python (automatyzacja_formularzy.py) i postępuj zgodnie z instrukcjami w kodzie.

Skrypt automatycznie wypełni formularze na podstawie danych w pliku Excel i zatwierdzi je.

# Pliki
.py: Główny plik z kodem automatu
dane.xlsx: Przykładowy plik Excel z danymi wejściowymi (można dostosować do własnych potrzeb)

# Podsumowanie działania kodu
-Wczytuje dane z pliku Excel (login, hasło, URL oraz dane ogłoszenia).
-Loguje się do OLX.
Dla każdego wiersza w Excelu:
-Otwiera stronę dodawania ogłoszenia.
-Wprowadza tytuł, zdjęcia, opis, cenę, stan, kategorię itp.
-Włącza opcje wysyłki.
-Publikuje ogłoszenie i odrzuca promowanie.
-Przechodzi do kolejnego ogłoszenia.
