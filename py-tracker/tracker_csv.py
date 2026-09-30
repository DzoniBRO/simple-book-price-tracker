import csv
import requests
from bs4 import BeautifulSoup

# Učitavanje stranice
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Unos budžeta od strane korisnika
max_budget = float(input("Unesite vaš maksimalni budžet (GBP): "))

books_data = []

# Pronalaženje svih knjiga na stranici
books = soup.find_all("article", class_="product_pod")

print("\n--- Pronađene knjige u okviru budžeta ---")

for book in books:
    title = book.h3.a["title"]

    # Izvlačenje cene, čišćenje teksta i konverzija u float
    price_text = book.find("p", class_="price_color").text
    clean_price = price_text.replace("£", "").replace("Â", "").strip()
    price = float(clean_price)

    # Provera da li je cena u okviru budžeta
    if price <= max_budget:
        print(f"📖 {title} - £{price}")
        books_data.append([title, price])

# Čuvanje podataka u CSV fajl prilagođen za Excel (sa ';' separatorom)
csv_filename = "books.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Naslov knjige", "Cena (GBP)"])
    writer.writerows(books_data)

print(f"\n✅ Podaci su uspešno sačuvani u '{csv_filename}'!")