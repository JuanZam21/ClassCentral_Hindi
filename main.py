from bs4 import BeautifulSoup
from googletrans import Translator

# Load the HTML file
with open("path/to/html/file.html", "r") as f:
    html = f.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Get all the text from the HTML
text = soup.get_text()

# Create a translator object
translator = Translator()

# Translate the text to Hindi
translated_text = translator.translate(text, dest="hi").text

# Replace the original text with the translated text
soup.body.string = translated_text

# Save the translated HTML file
with open("path/to/translated/html/file.html", "w") as f:
    f.write(str(soup))
