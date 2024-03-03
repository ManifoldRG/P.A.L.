import random
import time

from proactive_scheduler import ProactiveScheduler
from plugins.proactive_plugin import ProactivePlugin
from plugins.voicemail.plugin import VoiceMailPlugin
from plugins.vision.plugin import VisionPlugin
from plugins.arxiv.plugin import ArxivPlugin
from plugins.health.plugin import HealthPlugin
from plugins.chat_back.plugin import ChatBackPlugin

USER_PROMPT = """
I am heavily invested in bitcoin.

I am a busy startup founder and often get a ton of miss phone calls.
Let me know if i have any important voicemails. plase ignore the spam.
I am interested in events in my local area.
I am a startup founder who needs to constantly stay updated about research involving language models. 
Let me know if there are any papers relevant to my interests uploaded to Arxiv. If they are not relevant, please ignore the papers.
I like to stay healthy and analyze my health stats weekly. I generally enjoy lifting, crossfit, running, and biking, and plan my workouts based on the weather.

I have the following friends:
- Abhishek also an AI startup founder who is interested in reading papers and attending conferences.
- Manny Miller is an AI Researcher

I like coffee and finding different places to explore and work from."""


class BitcoinPlugin(ProactivePlugin):
    def __init__(self):
        self.price = 60_000.0

    def invoke(self, event):
        return f"The price of bitcoin is ${self.price}."


scheduler = ProactiveScheduler(preprompt=USER_PROMPT, prompt_name='default')
btc = BitcoinPlugin()
scheduler.register_plugin(btc, "bitcoin-event")
scheduler.register_plugin(ArxivPlugin(), "arxiv-event")
scheduler.register_plugin(VoiceMailPlugin(), "voicemail-event")
scheduler.register_plugin(VisionPlugin(), "vision-event")
scheduler.register_plugin(HealthPlugin(), "health-event")
chat_back_plugin = ChatBackPlugin()
scheduler.register_plugin(chat_back_plugin, "chat-back-event")

def invoke_and_print(scheduler, custom_prompt = None):
    info = scheduler.invoke_llm(custom_prompt)
    if info != "None" and info != "None.":
        print(info)
        print("---")


if __name__ == "__main__":
    btc.price = 60_301.46
    scheduler.trigger("bitcoin-event")
    invoke_and_print(scheduler)

    scheduler.trigger("health-event")
    invoke_and_print(scheduler)

    scheduler.trigger("arxiv-event")
    invoke_and_print(scheduler)

    btc.price = 60_302.11
    scheduler.trigger("bitcoin-event")
    btc.price = 60_305.22
    scheduler.trigger("bitcoin-event")
    invoke_and_print(scheduler)

    # scheduler.trigger("chat-back-event")
    # print()
    # invoke_and_print(scheduler, "Answer any questions the user had.")

    scheduler.trigger("voicemail-event")
    invoke_and_print(scheduler)

    scheduler.trigger("vision-event")
    invoke_and_print(scheduler)

    btc.price = 270_230.34
    scheduler.trigger("bitcoin-event")
    invoke_and_print(scheduler)

    invoke_and_print(scheduler)

    btc.price = 270_230.34
    scheduler.trigger("bitcoin-event")
    invoke_and_print(scheduler)


    # scheduler.trigger("chat-back-event")
    # print()
    # invoke_and_print(scheduler, "Answer any questions the user had.")

    invoke_and_print(scheduler)
