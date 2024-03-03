import os
import random
from utils import get_client
from ..proactive_plugin import ProactivePlugin

class VoiceMailPlugin(ProactivePlugin):
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.audio_files = [
            os.path.join(current_dir, "samples", "spam1.wav"),
            os.path.join(current_dir, "samples", "spam2.wav"),
            os.path.join(current_dir, "samples", "spam3.wav"),
            os.path.join(current_dir, "samples", "abhishek.wav"),
        ]
        self.client = get_client()

    def invoke(self, event):
        transcripts = "Here are recent voicemail messages you may have missed:\n"
        for idx, file_path in enumerate(self.audio_files):
            with open(file_path, 'rb') as file:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1", file=file
                )
                transcripts += f"voice mail {idx + 1}: {transcription.text}\n\n"
        return transcripts
