# Polecenie: 
# Każda osoba grała trzy mapy. Wyniki map są listą, a opis osoby słownikiem.
# 1. Dla każdej osoby policz sumę punktów i wypisz `Ola: 27` (w kolejności z listy `turniej`).
# 2. Wskaż zwycięzcę – osobę z największą sumą. W tych danych remisu nie ma.
# 3. Zbuduj słownik `nick → suma` i wypisz go. Może to być pętla albo dict comprehension.
# 4. Wypisz nicky osób z drużyny `"czerwoni"`, które mają sumę co najmniej 25.
# 5. Zbuduj zbiór nazw drużyn i wypisz je posortowane, oddzielone przecinkami.

turniej = [
    {"nick": "Ola", "druzyna": "czerwoni", "wyniki": [10, 8, 9]},
    {"nick": "Maja", "druzyna": "czerwoni", "wyniki": [10, 9, 10]},
    {"nick": "Kuba", "druzyna": "niebiescy", "wyniki": [7, 6, 7]},
    {"nick": "Piotr", "druzyna": "niebiescy", "wyniki": [5, 8, 4]},
]
for gracz in turniej:
    print(f"{gracz["nick"]}: {sum(gracz["wyniki"])}")

zwyciezca = turniej[0]["nick"]
najlepszy_wynik = sum(turniej[0]["wyniki"])

for wynik in turniej:
    if sum(wynik["wyniki"]) > najlepszy_wynik:
        najlepszy_wynik = sum(wynik["wyniki"])
        zwyciezca = wynik["nick"]
print(f"Zwyciężca to: {zwyciezca} ({najlepszy_wynik})")

czerwoni_25 = []
for gracz in turniej:
    suma = sum(gracz["wyniki"])
    if "czerwoni" in gracz["druzyna"] and suma >= 25:
        czerwoni_25.append(gracz["nick"])
print(f"Czerwoni z co najmniej 25: {', '.join(czerwoni_25)}")

druzyny = {gracz["druzyna"] for gracz in turniej}
print(f"Drużyny: {", ".join(druzyny)}")