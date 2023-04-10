from bs4 import BeautifulSoup, Comment

# Load the HTML file
with open("C:/Users/karen/OneDrive/Documentos/AI/ClassCentral_Hindi/freecertificates.html", encoding="utf-8") as f:
    html = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Remove all comments
for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
    comment.extract()
    
# save the modified HTML
with open("C:/Users/karen/OneDrive/Documentos/AI/ClassCentral_Hindi/freecertificates.html", "w", encoding="utf-8") as file:
  file.write(soup.prettify())
