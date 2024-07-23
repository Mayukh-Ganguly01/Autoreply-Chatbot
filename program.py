import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="API_KEY"
)

def last_message(chat_log, sender_name="Sender_Name"):
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False


pyautogui.click(1159,1051)
time.sleep(1)

while True:


    pyautogui.moveTo(653,109)
    pyautogui.dragTo(1289, 985, duration=1.0, button='left')

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click()
    time.sleep(1)

    chatHistroy = pyperclip.paste()

    print(chatHistroy)

    if last_message(chatHistroy):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person who is a sudent of an engineering collage from india and you speaks bengali, english and hindi.You analyze the chat history and try to give proper human like reply"},
            {"role": "user", "content": chatHistroy}
        ]
        )

        response = completion.choices[0].message
        pyperclip.copy(response)

        pyautogui.click(1110,999)
        time.sleep()

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')