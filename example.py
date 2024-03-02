import random
import time

from proactive_scheduler import ProactiveScheduler
from plugins.proactive_plugin import ProactivePlugin

USER_PROMPT = """
I am heavily invested in bitcoin.
Jack is heavily invested in bitcoin.

I have the following friends:
- Jack Hill
- Manny Miller"""


class BitcoinPlugin(ProactivePlugin):
    def __init__(self):
        self.price = 60_000.0

    def invoke(self, event):
        if random.random() < 0.05:
            self.price = 100_000
        if random.random() < 0.05:
            self.price = 0
        return f"The price of bitcoin is ${self.price}."


class FriendPlugin(ProactivePlugin):
    def __init__(self):
        self.triggered = False

    def invoke(self, event):
        if random.random() < 0.05 and self.triggered == False:
            self.triggered = True
            return "Jack Hill is present near you. He is available for lunch."
        return None


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
scheduler.register_plugin(FriendPlugin(), "every_second")
scheduler.register_plugin(ArxivPlugin(), "every_second")


t = time.time()
while True:
    time.sleep(10)
    scheduler.trigger_pending()
    info = scheduler.invoke_llm()
    if info != "None":
        print(info)
        print("---")
