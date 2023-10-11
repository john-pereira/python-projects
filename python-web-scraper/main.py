from urllib.request import urlopen

url = "https://www.coelhodiniz.com.br/"

page = urlopen(url)

"""
To extract the HTML from the page, first use the HTTPResponse object’s .read() method,
which returns a sequence of bytes. Then use .decode() to decode the bytes to a string using UTF-8
"""

html_bytes = page.read()
# html = html_bytes.decode("utf-8")
html = html_bytes.decode("latin-1")


# print(html)

title_index = html.find("<title>")
# title_index

start_index = title_index + len("<title>")
# start_index

end_index = html.find("</title>")
# end_index

title = html[start_index:end_index]
print(title)


