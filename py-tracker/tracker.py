import requests
from bs4 import BeautifulSoup

url = f"http://books.toscrape.com/"
response= requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")
maximum_price_of_the_book = float(input("Enter maximum price that suits you (in £): "))
if maximum_price_of_the_book<=0:
    while maximum_price_of_the_book<=0:
        print("Please enter the valid price.")
        maximum_price_of_the_book = float(input("Enter maximum price that suits you (in £): "))

for i in books:
    price_text= i.find("p", class_="price_color").text
    titlee = i.find("h3").find("a")["title"]

    clear_price = price_text.replace("£", "").replace("Â", "")
    number_price=float(clear_price)
    if number_price<=maximum_price_of_the_book:
        print(f"{titlee} - £{number_price}")