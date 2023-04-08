from bs4 import BeautifulSoup

with open("C:/Users/juand/Documents/IA/ClassCentraltoHindiProject/WEB/coursera.html", encoding="utf-8") as fp:
  response = fp.read()

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text(separator='')

# Remove text that does not belong to any tag
html = html.replace(text, '')

print(html)
