#requirements:
#openai

# setup:
# download python
# type in win + r on your keyboard
# type in cmd
# hit enter
# type this in cmd:
# pip install openai

# imports
import openai
import os

openai.api_key = str(input('enter your api key')

model_engine = "davinci" #model
gpt_model = openai.Model(engine=model_engine)

# Function to generate chat response

def generate_chat_response(prompt):
    response = gpt_model.generate(
        prompt=prompt,
        max_length=40,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Main loop
def main():
    print("Hi, how can I help?")
    while True:
        os.system('cls')
        user_input = input("Enter question: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Bye!")
            break
        response = generate_chat_response(user_input)
        print("Chatbot: " + response)

if __name__ == '__main__':
    main()
