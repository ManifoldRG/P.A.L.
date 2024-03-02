import os
from openai import OpenAI


def get_client(key=None):
    if key is None:
        key = os.environ.get("OPENAI_KEY")
    return OpenAI(api_key=key)


def invoke_llm(client: OpenAI, context: list[dict]):
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=context
    )
    return completion.choices[0].message.content