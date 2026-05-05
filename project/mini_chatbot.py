import json

def prev_message():
    try:
        with open("savechat.json", "r") as f:
            data = json.load(f)

            for i in data:
                try:
                    print(f'{i["role"]}: {i["content"]}')
                except KeyError:
                    print("Invalid message format skipped")

            return data   # ✅ ALWAYS return if successful

    except FileNotFoundError:
        print("No previous chat found.")
        return []

    except json.JSONDecodeError:
        print("Corrupted or empty file. Resetting...")
        return []

    except PermissionError:
        print("Permission denied.")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def save_convo(message: list):
    with open("savechat.json", "w") as f:
        json.dump(message, f, indent=4)


def bot_response(s: str):
    s = s.lower()

    if "hi" in s:
        bot = "Hello"
    elif "how are you" in s:
        bot = "I am good"
    elif "bye" in s:
        bot = "Goodbye"
    else:
        bot = "I don't understand"

    print(f"Bot: {bot}")
    return bot


if __name__ == "__main__":
    print("Previous conversation:")
    message = prev_message()

    print("Continue chatting")

    while True:
        try:
            i = input("User: ")

            if i.lower() == "stop":
                break

            if i.lower() == "clear":
                message = []
                save_convo(message)
                print("Chat cleared")
                continue

        except KeyboardInterrupt:
            print("\nExiting safely...")
            break

        except EOFError:
            print("\nInput stream closed.")
            break

        message.append({"role": "user", "content": i})

        bot = bot_response(i)

        message.append({"role": "assistant", "content": bot})

        save_convo(message)
