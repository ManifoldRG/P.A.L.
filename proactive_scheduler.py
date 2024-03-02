import threading, time, datetime
from proactive_plugin import ProactivePlugin

PREPROMPT_TEMPLATE = """
The user has prodvided the following information about him or herself:

"""

class ProactiveScheduler:
    def __init__(self, preprompt: str):
        self.invocation_dict = dict()
        self.context = PREPROMPT_TEMPLATE + preprompt
        self.pending_events = []

    def trigger_pending(self):
        while len(self.pending_events) > 0:
            self.trigger(self.pending_events.pop(0))

    def trigger(self, event: str):
        for plugin in self.invocation_dict.get(event, []):
            additional_context = plugin.invoke(event)
            self.context += f"\n{additional_context}"

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