import openai #pip install openai
from dotenv import load_dotenv #pip install python-dotenv

fileopen = open("F:/AI ChatBot/Api.txt")
api = fileopen.read()
fileopen.close()

openai.api_key = api
load_dotenv()


def Engine(ques, chat=None):

    File = open("F:/AI ChatBot/chat_history.txt")
    chat_temp = File.read()
    File.close()

    if chat is None:
        chat = chat_temp
    
    prompt = f'{chat}You : {ques}\nBrian : '
    response = openai.Completion.create(
        model = "text-davinci-002",
        prompt= prompt,
        temperature = 0.5,
        max_tokens=60,
        top_p = 0.3,
        frequency_penalty=0.5,
        presence_penalty=0)
    
    ans=response.choices[0].text.strip()
    chat_p = chat_temp
    File = open("F:/AI ChatBot/chat_history.txt","w")
    File.write(chat_p)
    File.close()
    return ans

while (True):
    user_inp = input("Type : ")
    aps = Engine(user_inp)
    print(aps)
    if user_inp == 'qs':
        break
print('The BOT has terminated !')