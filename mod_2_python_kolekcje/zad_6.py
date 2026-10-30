# polecenie: Ola i Kuba zapisali, w co grają. Zbiór sam pilnuje, żeby gra nie powtórzyła się dwa razy. 
# Wypisz nazwy **posortowane alfabetycznie** i oddzielone przecinkami (`", ".join(sorted(...))`), żeby wynik zawsze wyglądał tak samo:
# - gry, w które grają oboje,
# - gry tylko Oli,
# - gry tylko Kuby,
# - wszystkie gry bez powtórzeń,
# - czy `"Minecraft"` jest u Kuby (`tak` albo `nie`).

gry_oli = {"Minecraft", "FIFA", "Among Us", "Roblox"}
gry_kuby = {"FIFA", "Fortnite", "Roblox", "Valorant"}

print(f"wspólne: {gry_oli & gry_kuby}")
print(f"Tylko Ola: {gry_oli - gry_kuby}")
print(f"Tylko Kuba: {gry_kuby - gry_oli}")
print(f"wszystkie {gry_oli | gry_kuby}")
print(f"Minecraft u Kuby: {'tak' if 'Minecraft' in gry_kuby else 'nie'}")