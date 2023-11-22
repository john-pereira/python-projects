import requests

api_key = "7c4b9b99e771442b9bfa64a3b8de7fa9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-22&sortBy=publishedAt&apiKey=7c4b9b99e771442b9bfa64a3b8de7fa9"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
