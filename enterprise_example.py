import random
import time

from proactive_scheduler import ProactiveScheduler
from plugins.proactive_plugin import ProactivePlugin
from plugins.enterprise.plugin import EnterprisePlugin

USER_PROMPT = """
Macy's is an American department store chain with 508 stores across the United States. 
Macy's provides a wide range of products including clothing, accessories, jewelry, beauty products, shows, and home goods. 
Macy's has a wide variety of sofa collections such as Custom Color Sofa Collections, Living Room Couches and Sofas, and Furniture Couches and Sofas. 
Macy's has a high level of focus on customer satisfaction and retention. 
Macy's strongly prefers to serve customers and sell their products even if the exact thing customers are looking for is not present at that time."""


scheduler = ProactiveScheduler(USER_PROMPT, prompt_name='prompts/enterprise_cx.yaml')
scheduler.register_plugin(EnterprisePlugin(), "enterprise-event")

def invoke_and_print(scheduler):
    info = scheduler.invoke_llm()
    if info != "None":
        print(info)
        print("---")


time.sleep(2)
scheduler.trigger("enterprise-event")
invoke_and_print(scheduler)
