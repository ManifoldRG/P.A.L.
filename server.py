from flask import Flask, jsonify, request
from flask_cors import CORS
from example import scheduler, btc, chat_back_plugin
import json
import threading
from time import sleep

app = Flask(__name__)
CORS(app)

event_state = 0


def initialize_events_db():
    """Initialize the events database by resetting the events.json file."""
    with open("events.json", "w") as file:
        json.dump([], file)  # Write an empty list to the file


def run_events():
    global event_state
    print('event state', event_state)
    while True:  # Infinite loop to run events
        info = ""
        # Your event logic (simplified for brevity)
        if event_state == 0:
            btc.price = 60_301.46
            scheduler.trigger("bitcoin-event")
            info = scheduler.invoke_llm()
        elif event_state == 1:
            scheduler.trigger("health-event")
            info = scheduler.invoke_llm()
        elif event_state == 2:
            scheduler.trigger("arxiv-event")
            info = scheduler.invoke_llm()
        elif event_state == 3:
            btc.price = 60_302.11
            scheduler.trigger("bitcoin-event")
            btc.price = 60_305.22
            scheduler.trigger("bitcoin-event")
        elif event_state == 4:
            scheduler.trigger("vision-event")
            info = scheduler.invoke_llm()
        elif event_state == 5:
            scheduler.trigger("voicemail-event")
            info = scheduler.invoke_llm()
        elif event_state == 6:
            btc.price = 270_230.34
            scheduler.trigger("bitcoin-event")
            info = scheduler.invoke_llm()
        event_state += 1
    
        if info != "None" and info != "":
            # Append the event info to the JSON database
            with open("events.json", "r+") as file:
                data = json.load(file)
                data.append(info)
                file.seek(0)
                file.truncate()  # Clear the file before rewriting
                json.dump(data, file)

        sleep(5)  # Wait for 2 seconds before the next event


@app.route("/get-event")
def get_event():
    try:
        with open("events.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return jsonify(data)


@app.route("/chat", methods=['POST'])
def chat():
    data = request.json
    chat_prompt = data['prompt']

    chat_back_plugin.prompt = chat_prompt
    scheduler.trigger("chat-back-event")
    chat_back_plugin.prompt = None
    info = scheduler.invoke_llm("Answer any questions the user had.")
    # Append the event info to the JSON database
    with open("events.json", "r+") as file:
        data = json.load(file)
        data.append(info)
        file.seek(0)
        file.truncate()  # Clear the file before rewriting
        json.dump(data, file)

    return jsonify({"response": info})


if __name__ == "__main__":
    initialize_events_db()  # Reset the events database on start
    threading.Thread(target=run_events, daemon=True).start()
    app.run(debug=False)
