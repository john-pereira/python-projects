import re
from urllib.request import urlopen

url = "https://www.bretas.com.br/"
page = urlopen(url)
html = page.read().decode("utf-8")

"""
<title.*?> matches the opening <TITLE > tag in html. 
The <title part of the pattern matches with <TITLE because re.search() is called with re.IGNORECASE,
 and .*?> matches any text after <TITLE up to the first instance of >.
"""
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()

"""
*? non-greedily matches all text after the opening <TITLE >, stopping at the first match for </title.*?>.
</title.*?> differs from the first pattern only in its use of the / character, so it matches the closing </title  / > tag in html
"""
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
