import json
import websocket
from twitch_api import get_current_user, subscribe_to_follows

EVENTSUB_URL = "wss://eventsub.wss.twitch.tv/ws"


def on_open(ws):
    print("Connecté au WebSocket Twitch.")


def on_message(ws, message):
    payload = json.loads(message)

    print("===================================")
    print("on_message.")
    print(json.dumps(payload, indent=4))
    print("===================================")



def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Connexion fermée")


def main():

    ws = websocket.WebSocketApp(
        EVENTSUB_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws.run_forever()


if __name__ == "__main__":
    main()