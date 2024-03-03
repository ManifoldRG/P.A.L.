import random
import time

from proactive_scheduler import ProactiveScheduler
from plugins.proactive_plugin import ProactivePlugin
from plugins.voicemail.plugin import VoiceMailPlugin
from plugins.vision.plugin import VisionPlugin

USER_PROMPT = """
I am heavily invested in bitcoin.
I am a busy startup founder and often get a ton of miss phone calls. 
Let me know if i have any important voicemails. plase ignore the spam.
I am interested in events in my local area.

I have the following friends:
- Abhishek also an AI startup founder
- Manny Miller is an AI Researcher"""


class BitcoinPlugin(ProactivePlugin):
    def __init__(self):
        self.price = 60_000.0

    def invoke(self, event):
        if random.random() < 0.05:
            self.price = 100_000
        if random.random() < 0.05:
            self.price = 0
        return f"The price of bitcoin is ${self.price}."


class ArxivPlugin(ProactivePlugin):
    def __init__(self):
        self.triggered = False

    def invoke(self, event):
        if random.random() < 0.05 and self.triggered == False:
            self.triggered = True
            return """
New Arxiv paper:
Title: Proactivity in AI Agents
Author: Manny Miller"""
        return None


scheduler = ProactiveScheduler(USER_PROMPT)
scheduler.start_timer(interval_secs=1, event_name="every_second")
scheduler.register_plugin(BitcoinPlugin(), "every_second")
scheduler.register_plugin(ArxivPlugin(), "every_second")
scheduler.register_plugin(VoiceMailPlugin(), "every_second")
scheduler.register_plugin(VisionPlugin(), "every_second")


t = time.time()
while True:
    time.sleep(10)
    scheduler.trigger_pending()
    info = scheduler.invoke_llm()
    if info != "None":
        print(info)
        print("---")
