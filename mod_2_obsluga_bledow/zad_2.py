#zadanie:
# Masz słownik: osoba → lista przedmiotów.

# 1. Zapisz go do `prace_wlasne/ekwipunek.json` (`indent=2`, `ensure_ascii=False`).
# 2. Wczytaj plik z powrotem.
# 3. W pętli wypisz ekwipunek każdej osoby: `Ola: miecz, tarcza, mikstura`.
# 4. Zbuduj listę osób, które mają `"mikstura"`, i wypisz ją.
# 5. Policz **wszystkie** przedmioty w drużynie (suma długości list) i wypisz wynik.
# 6. Dopisz Kubie `"lina"`, zapisz plik ponownie, wypisz ekwipunek Kuby.

import json
from pathlib import Path

ekwipunek = {
    "Ola": ["miecz", "tarcza", "mikstura"],
    "Kuba": ["luk", "mikstura"],
    "Maja": ["miecz", "zwoj"],
}

# Tu piszesz rozwiązanie zadania 2

plik = Path("prace_wlasne") / "ekwipunek.json"
tekst_json = json.dumps(ekwipunek, indent=2, ensure_ascii=False)
plik.write_text(tekst_json, encoding="utf-8")

odczytany_tekst = plik.read_text(encoding="utf-8")
wczytany_dict = json.loads(odczytany_tekst)

ladny_zapis = []
for osoba, przedmioty in wczytany_dict.items():
    tekst = ", ".join(przedmioty)
    ladny_zapis.append(f"{osoba}: {tekst}")
print("\n".join(ladny_zapis))

mikstury = []
for osoba, przedmioty in wczytany_dict.items():
    if "mikstura" in przedmioty:
        mikstury.append(osoba)
print(f"Mają miksturę: {', '.join(mikstury)}")

liczba_przedmiotow = 0
for przedmiotow in wczytany_dict.values():
    liczba_przedmiotow += len(przedmiotow)
print(f"Liczba przedmiotów w drużynie: {liczba_przedmiotow}")

wczytany_dict["Kuba"].append("lina")
tekst_json = json.dumps(wczytany_dict, indent=2, ensure_ascii=False)
plik.write_text(tekst_json, encoding="utf-8")

odczytany_text = plik.read_text(encoding="utf-8")
wczytany_dict = json.loads(odczytany_text)

print(f"Ekwipunek Kuby: {", ".join(wczytany_dict["Kuba"])}")