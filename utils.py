import os
from openai import OpenAI

def get_client(key=None):
    if key is None:
        key = os.environ.get("OPENAI_KEY")
    return OpenAI(api_key=key)