#Plik `dane/wyniki_klasy.json` zawiera listę osób. Każda osoba ma:
#- `nick` (str),
#- `punkty` (lista liczb),
#- `klasa` (`"1A"` albo `"1B"`).

#Napisz program, który:

#1. Bezpiecznie wczyta plik (gdy brak pliku → komunikat `Brak pliku wyników.` i zakończ / nie kontynuuj dalszych punktów).
#2. Dla każdej osoby policzy **sumę** punktów i wypisze `Ola: 27`.
#3. Wypisze zwycięzcę (największa suma; w tych danych remisu nie ma).
#4. Wypisze nicky z klasy `"1A"`, których suma to **co najmniej 25**, oddzielone przecinkami.
#5. Zapisze do `prace_wlasne/podsumowanie.json` słownik postaci:

#{
#  "zwyciezca": "...",
#  "suma_zwyciezcy": ...,
#  "liczba_osob": ...,
#}

import json
from pathlib import Path

plik = Path("dane") / "wyniki_klasy.json"

try:
    ranking = json.loads(plik.read_text(encoding="utf-8"))

except FileNotFoundError:
    print("Brak pliku wyników.")

else:
    for osoba in ranking:
        suma = sum(osoba["punkty"])
        print(f"{osoba['nick']} ma: {suma} punktów")
    
    zwyciezca = ranking[0]["nick"]
    najlepszy_wynik = sum(ranking[0]["punkty"])
    for osoba in ranking:
        suma = sum(osoba["punkty"])
        if suma > najlepszy_wynik:
            najlepszy_wynik = suma
            zwyciezca = osoba["nick"]

    print(f"\nZwycięzca to: {zwyciezca} \nZ wynikiem: {najlepszy_wynik}")

    wynik_25 = []
    for osoba in ranking:
        suma = sum(osoba["punkty"])
        if osoba["klasa"] == "1A" and suma >= 25:
            wynik_25.append(osoba["nick"])

    print(f"\nCo najmniej 25 (1A): {", ".join(wynik_25)}")

    liczba_osob = len(ranking)

    sumy = [sum(osoba["punkty"]) for osoba in ranking]
    srednia = round(sum(sumy) / len(sumy), 1)

    podsumowanie = {
        "zwyciezca": zwyciezca,
        "suma_zwyciezcy": najlepszy_wynik,
        "liczba_osob": liczba_osob,
        "srednia_sum": srednia,
    }

    Path("prace_wlasne").mkdir(parents=True, exist_ok=True)
    plik_podsumowania = Path("prace_wlasne") / "podsumowanie.json"
    tekst_podsumowania = json.dumps(podsumowanie, indent=2, ensure_ascii=False)
    plik_podsumowania.write_text(tekst_podsumowania, encoding="utf-8")
    odczytane = json.loads(plik_podsumowania.read_text(encoding="utf-8"))
    print(odczytane)