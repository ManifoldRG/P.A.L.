from flask import Flask, jsonify
from flask_cors import CORS

from proactive_scheduler import ProactiveScheduler
from plugins.proactive_plugin import ProactivePlugin
from plugins.voicemail.plugin import VoiceMailPlugin

app = Flask(__name__)
CORS(app)

updates = [
    {'id': 1, 'content': 'This is the first update'},
]

@app.route('/api/updates')
def get_updates():
    scheduler.trigger_pending()
    info = scheduler.invoke_llm()
    data = {'id': 1, 'content': info}
    print('backend', data)
    return jsonify(data)


USER_PROMPT = """
I am heavily invested in bitcoin.
I am a busy startup founder and often get a ton of miss phone calls. 
Let me know if i have any important voicemails. plase ignore the spam.

I have the following friends:
- Abhishek also an AI startup founder
- Manny Miller is an AI Researcher"""

scheduler = ProactiveScheduler(USER_PROMPT)
scheduler.start_timer(interval_secs=1, event_name="every_second")
scheduler.register_plugin(VoiceMailPlugin(), "every_second")

if __name__ == '__main__':
    app.run(port=5328)
