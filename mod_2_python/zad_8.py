# polecenie: 
# 1. Wypisz ekwipunek każdej osoby w postaci `Ola: miecz, tarcza, mikstura`.
# 2. **Dopiero potem** dodaj Mai przedmiot `"mikstura"`.
# 3. Wypisz, kto ma `"miecz"` (już po dodaniu mikstury - przy mieczu nic to nie zmienia).
# 4. Policz, ile mikstur jest w całej drużynie.
# 5. Zbuduj słownik: osoba → liczba przedmiotów. Wypisz go.

gracze = {
   "Ola": ["miecz", "tarcza", "mikstura"],
   "Kuba": ["luk", "mikstura"],
   "Maja": ["miecz", "zwój"]
}

gracze["Maja"].append("mikstura")

ma_miecz = []
for gracz, ekwipunek in gracze.items():
    if "miecz" in ekwipunek:
        ma_miecz.append(gracz)
print(f"Gracze posiadające miecz: {ma_miecz}")

liczba_mikstur = 0
for dane in gracze.values():
    if "mikstura" in dane:
        liczba_mikstur += 1
print(f"Liczba mikstur w drużynie: {liczba_mikstur}")

liczba_przedmiotow = {}
for imie, dane in gracze.items():
    liczba_przedmiotow[imie] = len(dane)

print(liczba_przedmiotow)