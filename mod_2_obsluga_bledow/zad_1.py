from pathlib import Path

logi = [
    "OK: rozgrzewka",
    "DEBUG: temp=21",
    "WARN: mało wody",
    "OK: interwał x8",
    "INFO: pulse ok",
    "WARN: spadek tempa",
    "OK: stretching",
]

# Tu piszesz rozwiązanie zadania 1

wybrane = []
for n in logi:
    if n.startswith("OK:"):
        wybrane.append(n)
    elif n.startswith("WARN:"):
        wybrane.append(n)
tekst = "\n".join(wybrane)
log_czysty = Path("prace_wlasne") / "log_czysty.txt"
log_czysty.write_text(tekst, encoding="utf-8")

liczba_OK = 0 
liczba_WARN = 0
for n in logi:
    if n.startswith("OK:"):
        liczba_OK += 1
    elif n.startswith("WARN:"):
        liczba_WARN += 1
print(f"liczba OK: {liczba_OK}")
print(f"liczba WARN: {liczba_WARN}")

odczytany_tekst = log_czysty.read_text(encoding="utf-8")
linie = odczytany_tekst.splitlines()
print(f"Linii w pliku: {len(linie)}")