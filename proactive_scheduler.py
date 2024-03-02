import threading, time
from llm_invoker import get_client, invoke_llm
from proactive_plugin import ProactivePlugin

PREPROMPT_TEMPLATE = """
The user has prodvided the following information about him or herself:

"""

SYSTEM_PROMPT = """
You are a helpful and proactive assistant. You are able to periodically alert the user to important information.
     
You receive formation tagged with "Context:" followed by information that may or may not matter to the user.
You receive periodic updates from multiple sources of information some of which are automated. This may result
in repeated information. Repetition of information need not be reported to the user.
     
You are then asked periodically whether or not there is anything interesting to tell the user. Do not include
anything that the user is likely to know apriori, for example, the user likely already knows where they are or
what time it is.
"""

class ProactiveScheduler:
    def __init__(self, preprompt: str):
        self.invocation_dict = dict()
        self.context = [
            {
                "role": "user",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": PREPROMPT_TEMPLATE + preprompt
            }]
        self.pending_events = []
        self.client = get_client()

    def trigger_pending(self):
        while len(self.pending_events) > 0:
            self.trigger(self.pending_events.pop(0))

    def trigger(self, event: str):
        for plugin in self.invocation_dict.get(event, []):
            additional_context = plugin.invoke(event)
            if additional_context is not None:
                self.context.append(
                    {
                        "role": "user",
                        "content": f"Context: {additional_context}"
                    })

    def register_plugin(self, plugin: ProactivePlugin, event: str):
        if event in self.invocation_dict:
            self.invocation_dict[event].append(plugin)
        else:
            self.invocation_dict[event] = [plugin]

    def start_timer(self,
                    interval_secs: int,
                    event_name: str,
                    invoke_immediately: bool = False):
        Timer(interval_secs, event_name, self).start_timer(invoke_immediately)

    def invoke_llm(self):
        self.context.append(
            {
                "role": "user",
                "content": "If there is anything important, tell the user in a friendly tone with modest elaboration. If there is no new information, simply type 'None'."
            })
        result = invoke_llm(self.client, self.context)
        self.context.append(
            {
                "role": "assistant",
                "content": result
            })
        return result

class Timer:
    def __init__(self,
                 interval_secs: int,
                 event_name: str,
                 scheduler: ProactiveScheduler):
        self.next_time = time.time()
        self.interval_secs = interval_secs
        self.event_name = event_name
        self.scheduler = scheduler

    def start_timer(self, invoke_immediately: bool):
        def timer_event():
            self.next_time += self.interval_secs
            threading.Timer(self.next_time - time.time(), timer_event).start()
            self.scheduler.pending_events.append(self.event_name)
        if invoke_immediately:
            threading.Thread(target=timer_event).start()
        else:
            self.next_time = time.time() + self.interval_secs
            threading.Timer(self.next_time - time.time(), timer_event).start()
