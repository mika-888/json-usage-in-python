import json 
'''
#def save_chat(chat):
    with open("chat.json","w")as f:
        json.dump(chat,f)

#def read_chat():
    try:
        with open("chat.json","r")as f:
            data=json.load(f)
            for i in data:
                print(f"{i["role"]}: {i["content"]}")
    except FileNotFoundError:
        print("No chat history found.")
'''
            

chat=[
    {"role":"user","content":"Hi"},
    {"role": "assistant", "content": "Hello"},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "I'm fine!"}
    ]
#print(chat)
with open("chat.json","w")as f:
        json.dump(chat,f)
try:
        with open("chat.json","r")as f:
            data=json.load(f)
            for i in data:
                print(f"{i["role"]}: {i["content"]}")
except FileNotFoundError:
        print("No chat history found.")

   
