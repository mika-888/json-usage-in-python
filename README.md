
# JSON Handling in Python

This repository contains my practical implementation and understanding of JSON handling in Python.

# HOW THIS FOLDER IS STRUCTURED :

json-python-practice/
│
├── basics/
│   ├── parse_json.py
│   ├── convert_json.py
│
├── file_handling/
│   ├── write_json.py
│   ├── read_json.py
│
├── api/
│   ├── fetch_posts.py
│   ├── fetch_users.py
│
├── mini_project/
│   ├── chat_storage.py
│
├── data/
│   ├── sample.json
│   ├── chat.json   # (generated file)
│
├── requirements.txt
├── README.md
└── .gitignore

## Topics Covered

* Parsing JSON (`json.loads`)
* Converting Python to JSON (`json.dumps`)
* Reading and writing JSON files
* Working with APIs using requests
* Extracting nested data from JSON
* Handling missing keys safely

##  API Practice

Used JSONPlaceholder API to:

* Fetch posts and extract title + id
* Fetch users and extract name + email

##  Mini Project

Implemented a simple chat storage system:

* Save conversation history to JSON
* Load previous chat data
* Simulates memory used in AI chatbots

## 🛠 Tech Stack

* Python
* requests
* JSON module

##  Why This Project

This project builds the foundation for:

* LLM API handling
* Agent-based systems
* RAG pipelines
* Backend data handling

## I referred to : https://www.youtube.com/watch?v=9N6a-VLBa2I&t=2s
