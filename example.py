import random
import time

from proactive_scheduler import ProactiveScheduler


USER_PROMPT = """
I am heavily invested in bitcoin."""


class BitcoinPlugin:
    def __init__(self):
        self.price = 60_000.
    def invoke(self, event):
        if random.random() < 0.05:
            
            self.price = 100_000
        if random.random() < 0.05:
            self.price = 0
        return f"The price of bitcoin is ${self.price}."


scheduler = ProactiveScheduler(USER_PROMPT)
scheduler.start_timer(interval_secs=1, event_name="every_second")
scheduler.register_plugin(BitcoinPlugin(), "every_second")


t = time.time()
while True:
    time.sleep(1)
    scheduler.trigger_pending()
    info = scheduler.invoke_llm()
    if info != "None":
        print(info)