from openai import OpenAI

class OpenAIManager:
    client = OpenAI("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")

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello world"}]
    )