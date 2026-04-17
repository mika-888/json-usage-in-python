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
            

# Simple bot response logic (can replace later with AI)
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    if "hi" in user_input or "hello" in user_input:
        return "Hello!"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I don't understand that yet."

# MAIN PROGRAM

messages = load_chat()

print("Chatbot started (type 'stop' to exit)\n")

# Show previous chat
if messages:
    print("Previous conversation:")
    for msg in messages:
        print(f"{msg['role']}: {msg['content']}")
    print("\n--- Continue chatting ---\n")

while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.strip() == "" or user_input.lower() == "stop":
        print("Chat ended.")
        break

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate bot response
    bot_reply = get_bot_response(user_input)

    # Add bot message
    messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    # Print response
    print(f"Bot: {bot_reply}")

    # Save conversation
    save_chat(messages)
except FileNotFoundError:
        print("No chat history found.")

   
