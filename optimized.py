from bs4 import BeautifulSoup
from mtranslate import translate
import os
import concurrent.futures

# set the input and output directories
input_dir = "C:/Users/juand/Documents/IA/ClassCentraltoHindiProject/WEB"
output_dir = "C:/Users/juand/Documents/IA/ClassCentraltoHindiProject/WEB/complete"

# define the batch size
batch_size = 10

# define a function to translate a text element
def translate_element(element):
    if element.parent.name in ['script', 'style']:
        return str(element)
    try:
        translated_text = translate(element, 'hi')
        return translated_text
    except:
        return str(element)

# define a function to translate a batch of HTML files
def translate_batch(file_paths):
    for file_path in file_paths:
        # read the HTML file
        with open(file_path, encoding="utf-8") as fp:
            response = fp.read()

        # parse the HTML
        soup = BeautifulSoup(response, "lxml")

        # find all text elements in the HTML
        text_elements = soup.find_all(string=True)

        # use multi-threading to translate the text elements
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(translate_element, text_elements)

        # update the HTML with the translated text
        for element, translated_text in zip(text_elements, results):
            element.replace_with(translated_text)

        # save the modified HTML
        file_name = os.path.basename(file_path)
        output_file_path = os.path.join(output_dir, file_name)
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(str(soup))

# get a list of all HTML files in the input directory
file_paths = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.html')]

# split the file paths into batches and translate each batch
for i in range(0, len(file_paths), batch_size):
    batch = file_paths[i:i+batch_size]
    translate_batch(batch)
