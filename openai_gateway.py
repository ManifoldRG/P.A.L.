import os
import yaml
from utils import get_client

class PromptService:
    def __init__(self, prompt_name='default', preprompt=''):
        self.client = get_client()
        self.context = []
        prompt_file_path = os.path.join('prompts', f'{prompt_name}.yaml')
        self.system_content = None
        self.preprompt_command = None
        self.invoke_command = None
        try:
            with open(prompt_file_path, 'r') as file:
                data = yaml.safe_load(file)
                self.system_content = data['SYSTEM']
                self.preprompt_command = data['PREPROMPT'] + preprompt
                self.invoke_command = data['INVOKE']
        except FileNotFoundError:
            print(f"File '{prompt_file_path}' not found.")
        system_message = {
            "role": "system",
            "content": self.system_content
        }
        self.context.append(system_message)
        preprompt_message = {
            "role": "user",
            "content": self.preprompt_command
        }
        self.context.append(preprompt_message)

    def add_context(self, role, content):
        message = {
            "role": role,
            "content": content
        }
        self.context.append(message)


    def invoke_llm(self):
        self.add_context(role="user", content=self.invoke_command)
        completion = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=self.context
        )
        return completion.choices[0].message.content
