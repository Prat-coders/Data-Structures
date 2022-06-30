import requests
from bs4 import BeautifulSoup

newegg_link = "https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Description" \
              "=samsung%20z%20flip%205g&cm_re=samsung_z%20flip%205g-_-75-168-090-_-Product&quicklink=true "
req = requests.get(newegg_link)
content = req.content
print(content)

soup = BeautifulSoup(content, "html.parser")
full_display = soup.find_all("div", {"class": "row is-product has-side-right has-side-items"})
item_det = soup.find_all("li")

for display in full_display:
    item_name = display.find("h1", attrs={"class": "product-title"}).text
    item_price = display.find("div", attrs={"class": "price-current"}).text
    item_stock_check = display.find("div", attrs={"class": "product-inventory"}).text
    item_seller = display.find("div", attrs={"class": "product-seller"}).text
    print(
        f"Name: {item_name},\nPrice: {item_price}, \nAvailability of the product: {item_stock_check},\n{item_seller}")
