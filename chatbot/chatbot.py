import random
import chromadb
import gradio as gr
from db_helper import SQLiteDBReader


from PyPDF2 import PdfReader
import os

import re
import requests
from bs4 import BeautifulSoup

def extract_text_from_url(input_text):
    # Regular expression to find URLs
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, input_text)
    
    # If no URLs are found, return None
    if not urls:
        return None
    
    extracted_text = []
    for url in urls:
        try:
            # Fetch the webpage content
            response = requests.get(url)
            response.raise_for_status()  # Raise an error if the request fails

            soup = BeautifulSoup(response.text, 'html.parser')

            page_text = soup.get_text(separator=' ', strip=True)
            extracted_text.append(page_text)
        except Exception as e:
            print(f"Error fetching or parsing {url}: {e}")
            extracted_text.append(f"Error fetching content from {url}")
    
    return extracted_text

clientChroma = chromadb.Client()

def read_pdfs_from_folder(folder_path):
    pdf_texts = []
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):  # Check if the file is a PDF
            file_path = os.path.join(folder_path, filename)
            reader = PdfReader(file_path)
            text = "resume: "
            
            # Extract text from all pages in the PDF
            for page in reader.pages:
                text += page.extract_text()
            
            pdf_texts.append(text)
    
    return pdf_texts


def rag_context(text):
    pdfs = read_pdfs_from_folder("../trackmyjob-backend/resumes")
    db_data = SQLiteDBReader("../trackmyjob-backend/mydb.db").get_all_tables_data()
    print(db_data)
    docs = []
    ct = 0
    for k,v in db_data.items():
        for row in v:
            print(str(row))
            docs.append(str(row))
            ct += 1
    for pdf in pdfs:
        docs.append(pdf)
        ct+=1
    # print(docs)
    idxs = [str(id) for id in range(ct)]
    
    collection_name = "all-my-documents"
    if collection_name in [collection.name for collection in clientChroma.list_collections()]:
        clientChroma.delete_collection(collection_name)
    collection = clientChroma.create_collection(collection_name)
    collection.add(
        documents=docs,
        ids = idxs
    )
    results = collection.query(
        query_texts=[text],
        n_results=3,
    )
    print(results['documents'])
    return results['documents']


from openai import OpenAI

clientAI = OpenAI()

def chat_completion(messages):
    response = clientAI.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:personal:directed-studies:AZUkXjAe",
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

# print(rag_context(""))

def random_response(message, history):
    context = rag_context(message)
    msg = message + "\ncontext: " + str(context)
    url_text = extract_text_from_url(message)
    if url_text:
        msg = msg + "/n relevant information from url: " + str(url_text)
    new_msg = {"role":"user","content":msg}
    tmp = history.copy()
    tmp.append(new_msg)
    reply = chat_completion(tmp)
    return reply


gr.ChatInterface(
    fn=random_response, 
    type="messages"
).launch()


# pdfs = read_pdfs_from_folder("../trackmyjob-backend/resumes")
# print(pdfs)

# import sqlite3

# # Connect to database
# connection = sqlite3.connect("example.db")
# cursor = connection.cursor()

# # Create table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL
# )
# ''')

# # Insert data
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
# connection.commit()

# # Query data
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# # Close connection
# connection.close()
