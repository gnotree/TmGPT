#!/usr/bin/env python3
import openai
#I am unable to post the complete '.py' file and keep my OpenAI key in the code, as OpenAI processes my key as leaked and rotates it if I do so.
#If you do not want to create your own key, you download the .zip from my website (gtai.io) and save yourself from having to enter a seperate key
#However, it should be noted, that it is recommended you use your own key if possible. It will help with the programs efficiency and effectiveness.
openai.api_key = "pasteYourOwnOpenAIKeyInTheQuotes"
#Paste you own API key from Open AI in the quotations in line 6
user_prompt = ""
count = 0

print("$" * 48)
print("[TmGPT] -- (V1.1) -- {Engine ID: DaVinci 003}")
print("Updated 02/13/2023 | <Programmed by GTAI.io> ")
print("*" * 48)
print("[NOTE]:To QUIT the program, enter  '-1'")
print("*" * 48)
print(" ")
print("Welcome to GTAI's [Terminal GPT]...")
print(" ")

while user_prompt != "-1" :
    count = count + 1
    print("◌ Prompt " + str(count) + " ◌")
    print("[Terminal GPT]: Enter your PROMPT below...")
    user_prompt = input("      [User]: » ")
    if user_prompt != "-1":
        completions = openai.Completion.create(engine="text-davinci-003", prompt=user_prompt, temperature=0.7, max_tokens=3000)
        #Note 1: The engine options are currently either davinci002 or 003, babbage001,currie001, ada001, cpu001, code-davinci-002, code-cushman-001
        #Note 2: The temperature controls the depth of response in this script. The temperature parameter controls the
        # diversity and randomness of the generated responses.
        # The higher the temperature, the more diverse and unpredictable the responses will be.
        # To adjust the depth of response, you can set the temperature to a lower value (e.g. 0.5) to generate more
        # conservative responses, or a higher value (e.g. 1.0) to generate more creative and diverse responses.
        response = completions.choices[0].text
        print("[TmGPT]: " + response + "\n" + "-"*48)

if user_prompt == "-1":
    print("[TmGPT]:" + "\n" + "NO DATA or a NEGATIVE value was entered by the user. TerminalGPT [GTAI.io, V1.0] will now quit.")
