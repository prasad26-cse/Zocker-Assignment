import requests
from bs4 import BeautifulSoup
import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Step 1: Accept a URL as input
url = input("Please enter the URL: ")

# Step 2: Retrieve the content of the provided web link
response = requests.get(url)
if response.status_code == 200:
    web_content = response.text
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
    exit()

# Step 3: Analyze the content
soup = BeautifulSoup(web_content, 'html.parser')

# Step 4: Extract key information
title = soup.title.string if soup.title else "No Title Found"
paragraphs = soup.find_all('p')
extracted_texts = [para.get_text() for para in paragraphs]

# Step 5: Generate a concise summary
full_text = ' '.join(extracted_texts)
doc = nlp(full_text)
sentences = [sent.text for sent in doc.sents]
summary = ' '.join(sentences[:3])  # Adjust the number of sentences as needed

# Step 6: Display the content in a structured manner
print("\n--- Web Page Title ---")
print(title)
print("\n--- Extracted Content ---")
for i, text in enumerate(extracted_texts, start=1):
    print(f"Paragraph {i}: {text}\n")

print("--- Summary ---")
print(summary)