#polecenie: 
# Zrób **wyłącznie comprehensions** (bez osobnej pętli `for`, która buduje wynik).
# Każdy punkt wypisz osobnym `print`.
# 1. Lista ocen co najmniej 4. Zostaw powtórki – jeśli piątka jest dwa razy, ma być dwa razy
# 2. Lista nicków wielkimi literami.
# 3. Słownik: nick → liczba liter.
# 4. Lista rund większych niż 100.
# 5. Zbiór gatunków ze sklepu z zadania 7. Kolejność w zbiorze może być inna. Mają być dokładnie: `akcja`, `sandbox`, `sport`.

oceny = [5, 2, 6, 3, 4, 1, 5]
nicki = ["ola", "kuba", "maja", "piotr"]
punkty = [90, 200, 120, 69, 180, 220]
gry = {
    "Minecraft": [("cena", 99), ("gatunek", "sandbox")],
    "FIFA 25": [("cena", 280), ("gatunek", "sport")],
    "Hades": [("cena", 114.99), ("gatunek", "RPG")],
    "Stardew Valley": [("cena", 53.99), ("gatunek", "RPG")],
    "Rocket League": [("cena", 0), ("gatunek", "sport")],
}

wielkie = [nick.upper() for nick in nicki]

liczba_liter = {nick: len(nick) for nick in nicki}
print(liczba_liter)

wiecej_100 = [wiecej for wiecej in punkty if wiecej > 100]
print(wiecej_100)

gatunki_gier = {gatunki[1][1] for gatunki in gry.values()}
print(gatunki_gier)