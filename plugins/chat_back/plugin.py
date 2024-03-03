import os
from utils import get_client
from ..proactive_plugin import ProactivePlugin


class ChatBackPlugin(ProactivePlugin):
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.image_files = [
            os.path.join(current_dir, "images", "image.jpg"),
        ]

    def invoke(self, event):
        chat = input('ChatBack input: ')
        if len(chat) > 0:
            return f"User chatted directly: {chat}"
        else:
            return None
