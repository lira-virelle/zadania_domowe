# polecenie: Każda gra ma tytuł, cenę i gatunek.
# 1. Wypisz same tytuły, jeden pod drugim.
# 2. Policz, ile kosztują wszystkie gry razem.
# 3. Wypisz tytuły gier tańszych niż 100 zł (w jednej linii, po przecinku).
# 4. Znajdź najdroższą grę i wypisz jej tytuł oraz cenę.
# 5. Policz, ile gier jest z gatunku `"sandbox"`.

gry = {
    "Minecraft": [("cena", 99), ("gatunek", "sandbox")],
    "FIFA 25": [("cena", 280), ("gatunek", "sport")],
    "Hades": [("cena", 114.99), ("gatunek", "RPG")],
    "Stardew Valley": [("cena", 53.99), ("gatunek", "RPG")],
    "Rocket League": [("cena", 0), ("gatunek", "sport")],
}
for tytul in gry.keys():
    print(f"{tytul}")

lancznie = 0
for ceny in gry.values():
    lancznie += ceny[0][1]
print(f"Łącznie: {lancznie:.2f}")

tansze = []
for tytul, dane in gry.items():
    if dane[0][1] <= 100:
        tansze.append(tytul)
print(f"Gry, które kosztują taniej niż 100zł: {tansze}")

najdrozsza = "Minecraft"
for tytul, dane in gry.items():
    if dane[0][1] > gry[najdrozsza][0][1]:
        najdrozsza = tytul
print(f"Najdroższa gra: {najdrozsza}")

sandboxy = 0
for dane in gry.values():
    if dane[1][1] == "sandbox":
        sandboxy += 1
print(f"Gry które są sandbox'ami: {sandboxy}")