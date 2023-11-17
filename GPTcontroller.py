import openai
from openai import OpenAI


def create_new_conversation(selected_api_key):
    openai.api_key = selected_api_key
    messages = []
    system_message = input("What type of chatbot you want me to be?")
    messages.append({"role": "system", "content": system_message})
    print("Alright! I am ready to be your friendly chatbot" + "\n" + "You can now type your messages."
                                                                     "Enter '!quit' to stop.")

    while True:
        message = input("")
        if message.lower() == '!quit':
            break
        messages.append({"role": "user", "content": message})
        client = OpenAI(
            api_key=selected_api_key,
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages
        )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(reply)
    print("Conversation ended.")
