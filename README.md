# 🤖 Automat do wypełniania formularzy internetowych

## 📌 Opis
Projekt przedstawia **automat do wypełniania formularzy internetowych** na podstawie danych z plików Excel.  
Program wykorzystuje bibliotekę **Selenium** do interakcji z formularzami online – automatycznie wprowadza dane i zatwierdza formularze.  

👉 Dzięki temu rozwiązaniu można **zaoszczędzić czas** oraz **zredukować błędy ludzkie** podczas pracy z dużą liczbą formularzy.

---

## 🚀 Funkcjonalności
- 📂 Pobieranie danych z plików **Excel (.xlsx)**
- 📝 Automatyczne uzupełnianie pól formularza
- ✅ Zatwierdzanie formularzy po wypełnieniu
- 🌐 Obsługa przez **Selenium** – automatyzacja w przeglądarce

---

## 🛠️ Jak używać
1. Zainstaluj bibliotekę **Selenium**:
   ```bash
   pip install selenium

2. Przygotuj plik dane.xlsx z danymi do wprowadzenia.

3. Uruchom skrypt:

4. Skrypt automatycznie:

  wypełni formularze danymi z pliku,

  zatwierdzi je,

  przejdzie do kolejnego wpisu.
  

  ## 📝 Podsumowanie działania

Automat realizuje poniższe kroki:

1. 📂 Wczytuje dane z pliku Excel (**login, hasło, URL, dane ogłoszenia**).
2. 🔑 Loguje się do serwisu (np. **OLX**).
3. 🔄 Dla każdego wiersza w Excelu:
   - 🌐 otwiera stronę dodawania ogłoszenia,  
   - 📝 uzupełnia tytuł, zdjęcia, opis, cenę, stan, kategorię itp.,  
   - 📦 włącza opcje wysyłki,  
   - ✅ publikuje ogłoszenie i pomija promowanie,  
   - ⏭️ przechodzi do kolejnego wpisu.  

