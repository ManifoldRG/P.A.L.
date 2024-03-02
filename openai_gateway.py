import os
from openai import OpenAI

class PromptService:
    def __init__(self):
        self.key = os.environ.get("OPENAI_KEY")
        self.client = OpenAI(api_key=self.key)
        self.context = []
        self.system_content = """
        You are a helpful and proactive assistant. You are able to periodically alert the user to important information.
            
        You receive formation tagged with "Context:" followed by information that may or may not matter to the user.
        You receive periodic updates from multiple sources of information some of which are automated. This may result
        in repeated information. Repetition of information need not be reported to the user.
            
        You are then asked periodically whether or not there is anything interesting to tell the user. Do not include
        anything that the user is likely to know apriori, for example, the user likely already knows where they are or
        what time it is.
        """
        system_message = {
            "role": "system",
            "content": self.system_content
        }
        self.context.append(system_message)
        
    
    def add_context(self, role, content):
        message = {
            "role": role,
            "content": content
        }
        self.context.append(message)


    def invoke_llm(self):
        completion = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=self.context
        )
        return completion.choices[0].message.content
