from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)