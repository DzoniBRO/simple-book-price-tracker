import csv
import requests
from bs4 import BeautifulSoup

# Target URL
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get maximum budget from user input
max_budget = float(input("Enter your maximum budget (GBP): "))

books_data = []

# Find all book items on the page
books = soup.find_all("article", class_="product_pod")

print("\n--- Books Found Within Budget ---")

for book in books:
    title = book.h3.a["title"]

    # Extract price, clean currency symbols, and convert to float
    price_text = book.find("p", class_="price_color").text
    clean_price = price_text.replace("£", "").replace("Â", "").strip()
    price = float(clean_price)

    # Filter books within budget
    if price <= max_budget:
        print(f"📖 {title} - £{price}")
        books_data.append([title, price])

# Save filtered results to CSV file optimized for Excel
csv_filename = "books.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8-sig") as file:
    file.write("sep=;\n")
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Book Title", "Price (GBP)"])
    writer.writerows(books_data)

print(f"\n✅ Data successfully saved to '{csv_filename}'!")