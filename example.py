import random
import time

from proactive_scheduler import ProactiveScheduler
from plugins.proactive_plugin import ProactivePlugin
from plugins.voicemail.plugin import VoiceMailPlugin
from plugins.vision.plugin import VisionPlugin
from plugins.arxiv.plugin import ArxivPlugin

USER_PROMPT = """
I am heavily invested in bitcoin.

I am a busy startup founder and often get a ton of miss phone calls.
Let me know if i have any important voicemails. plase ignore the spam.
I am interested in events in my local area.
I am a startup founder who needs to constantly stay updated about research involving language models. 
Let me know if there are any papers relevant to my interests uploaded to Arxiv. If they are not relevant, please ignore the papers.

I have the following friends:
- Abhishek also an AI startup founder
- Manny Miller is an AI Researcher

I like coffee and reading"""


class BitcoinPlugin(ProactivePlugin):
    def __init__(self):
        self.price = 60_000.0
    def invoke(self, event):
        return f"The price of bitcoin is ${self.price}."


scheduler = ProactiveScheduler(USER_PROMPT)
btc = BitcoinPlugin()
scheduler.register_plugin(btc, "bitcoin-event")
scheduler.register_plugin(ArxivPlugin(), "arxiv-event")
scheduler.register_plugin(VoiceMailPlugin(), "voicemail-event")
scheduler.register_plugin(VisionPlugin(), "vision-event")

def invoke_and_print(scheduler):
    info = scheduler.invoke_llm()
    if info != "None":
        print(info)
        print("---")


btc.price = 60_301.46
scheduler.trigger("bitcoin-event")
invoke_and_print(scheduler)

time.sleep(2)
scheduler.trigger("arxiv-event")
invoke_and_print(scheduler)

time.sleep(0.5)
btc.price = 60_302.11
scheduler.trigger("bitcoin-event")
btc.price = 60_305.22
scheduler.trigger("bitcoin-event")
invoke_and_print(scheduler)

time.sleep(1)
scheduler.trigger("vision-event")
invoke_and_print(scheduler)

time.sleep(2)
scheduler.trigger("voicemail-event")
invoke_and_print(scheduler)

time.sleep(2)
btc.price = 270_230.34
scheduler.trigger("bitcoin-event")
invoke_and_print(scheduler)

invoke_and_print(scheduler)
