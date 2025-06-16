from openai import OpenAI

client = OpenAI(
  api_key="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"
)


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "Em que ano o Brasil foi descoberto?"}
  ]
)

print(completion.choices[0].message)
