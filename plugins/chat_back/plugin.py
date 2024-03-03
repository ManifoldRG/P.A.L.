import os
from utils import get_client
from ..proactive_plugin import ProactivePlugin


class ChatBackPlugin(ProactivePlugin):
    def __init__(self):
        self.prompt = None

    def invoke(self, event):
        if self.prompt is not None and len(self.prompt) > 0:
            return f"User chatted directly: {self.prompt}"
        else:
            return None
