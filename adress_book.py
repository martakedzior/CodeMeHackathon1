# ### Książka adresowa:
# Program przechowujący danę kontaktowe znajomych/klientów.
# - Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
#     - Wyświetlenie wszystkich wpisów
#     - Stworzenie nowego wpisu (dane wczytywane z klawiatury)
#     - Usunięcie wpisu
#     - Zakończenie pracy programu
# - Program powinien na starcie mieć już wprowadzone kilka wpisów.


adress_book = {
  'Jan Kowalski': 'jkowalski@gmail.com',
  'Anna Nowak': 'anowak@gmail.com',
  'Zbigniew Szczygieł': 'zszcz'
  }

user_input = input('Podaj opcję do wybrania: 1 - Książka Adresowa')

if user_input == '1':
    print(adress_book)
if user_input == '2':
    new_entry = input('Podaj imię i nazwisko osoby, którą chcesz dodać do słownika: ')
    new_contact = input('Podaj kontakt: ')
    adress_book[new_entry]