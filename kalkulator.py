#Zadanie 3 (3.py) Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
#dzielić oraz obliczać potęgę.
#Przykład: Jaką operację chcesz wykonać?
#1) dodawanie
#2) odejmowanie
#3) mnożenie
#4) dzielenie
#5) potęgowanie
#Wpisz numer operacji: 2
#Podaj argument 1: 34
#Podaj argument 2: 5
#Wynik: 29

print("1) dodawanie"
"2) Odejmowanie"
"3) mnożenie"
"4) dzielenie"
"5) potęgowanie")

x = int(input('Liczba'))
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if x == 1:
    print (a + b)
if x == 2:
    print(a ** b)
if x == 3:
    print(a * b)
if x == 4:
    print(a / b)
if x == 5:
    print(a ** b)
else:
    print('not a valid numer')
