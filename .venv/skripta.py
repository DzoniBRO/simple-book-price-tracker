import requests
from bs4 import BeautifulSoup

# 1. Pitamo korisnika koga želi da pretraži
trazeni_autor = input("Ukucaj ime autora (npr. Albert Einstein, Steve Martin, J.K. Rowling): ")

stranica = 1
nadjeni_citati = []

print(f"\nPretražujem sajt za autora: {trazeni_autor}...\n")

while True:
    # Otvaramo stranicu po stranicu (1, 2, 3...)
    url = f"https://quotes.toscrape.com/page/{stranica}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    # Ako na stranici nema više citata, stigli smo do kraja sajta
    if not quotes:
        break

    # Prolazimo kroz sve citate na trenutnoj stranici
    for q in quotes:
        author = q.find("small", class_="author").text

        # Proveravamo da li se ime autora poklapa (koristimo .lower() da ne pravi razliku između malih/velikih slova)
        if trazeni_autor.lower() in author.lower():
            text = q.find("span", class_="text").text
            nadjeni_citati.append((text, author))

    stranica += 1

# 2. Prikazujemo i čuvamo rezultate
if nadjeni_citati:
    ime_fajla = f"{trazeni_autor.replace(' ', '_').lower()}_citati.txt"

    with open(ime_fajla, "w", encoding="utf-8") as file:
        file.write(f"--- SVI CITATI ZA: {trazeni_autor} ---\n\n")

        for i, (citat, autor) in enumerate(nadjeni_citati, 1):
            ispis = f"{i}. {citat} — {autor}"
            print(ispis)  # Ispis u konzoli
            file.write(ispis + "\n")  # Upis u fajl

    print(f"\nPronađeno je ukupno {len(nadjeni_citati)} citata. Sačuvano u '{ime_fajla}'.")
else:
    print("Nismo pronašli nijedan citat za tog autora.")