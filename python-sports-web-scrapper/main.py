import requests
from bs4 import BeautifulSoup

url ='https://www.bretas.com.br/mercearia'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

div_element = soup.find("div", id="product-container").find_child("div", class_="bretas-bretas-components-0-x-WrapperProductName")

# Extract the text from the div element.



print(div_element)
