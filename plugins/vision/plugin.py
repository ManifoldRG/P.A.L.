import os
import random
from utils import get_client
import base64
from ..proactive_plugin import ProactivePlugin


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


class VisionPlugin(ProactivePlugin):
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.image_files = [
            os.path.join(current_dir, "images", "image.jpg"),
        ]
        self.client = get_client()
        self.triggered = False

    def invoke(self, event):
        if random.random() < 0.05 and self.triggered == False:
            self.triggered = True
            image_path = self.image_files[0]
            base64_image = encode_image(image_path)
            return {
                "role": "user",
                "content": [
                        {
                            "type": "text",
                            "text": "Image context:"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
        return None
