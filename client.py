from openai import OpenAI
client = OpenAI(
    api_key="API_KEY"
)


command = '''
     chat-history
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person who is a sudent of an engineering collage and he speaks bengali, english and hindi.You analyze the chat history and try to give proper human like reply"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message)