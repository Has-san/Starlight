import asyncio
import json
import serial
import websockets
from twitch_api import subscribe_to_follows, create_eventsub_subscription
from event_bridge import handle_twitch_event


TWITCH_EVENTSUB_URL = "wss://eventsub.wss.twitch.tv/ws"


async def handle_message(
    message: str,
    client_id: str,
    access_token: str,
    user_id: str,
    arduino: serial.Serial,
) -> None:
    data = json.loads(message)
    message_type = data.get("metadata", {}).get("message_type")

    if message_type == "session_welcome":
        session_id = data["payload"]["session"]["id"]
        print(f"Session WebSocket ouverte : {session_id}")
        await subscribe_to_events(client_id, access_token, user_id, session_id)

    elif message_type == "notification":
        payload = data.get("payload", {})
        await handle_twitch_notification(payload, arduino)

    elif message_type == "session_keepalive":
        pass

    else:
        print(f"Message non gere : {message_type}")


async def subscribe_to_events(
    client_id: str,
    access_token: str,
    user_id: str,
    session_id: str,
) -> None:
    print("Souscription aux evenements...")

    subscribe_to_follows(
        client_id=client_id,
        access_token=access_token,
        broadcaster_user_id=user_id,
        moderator_user_id=user_id,
        session_id=session_id,
    )

    create_eventsub_subscription(
        client_id=client_id,
        access_token=access_token,
        subscription_type="channel.subscribe",
        version="1",
        condition={"broadcaster_user_id": user_id},
        session_id=session_id,
    )

    create_eventsub_subscription(
        client_id=client_id,
        access_token=access_token,
        subscription_type="channel.raid",
        version="1",
        condition={"to_broadcaster_user_id": user_id},
        session_id=session_id,
    )

    create_eventsub_subscription(
        client_id=client_id,
        access_token=access_token,
        subscription_type="channel.channel_points_custom_reward_redemption.add",
        version="1",
        condition={"broadcaster_user_id": user_id},
        session_id=session_id,
    )

    print("Souscriptions OK.")


async def handle_twitch_notification(
    payload: dict,
    arduino: serial.Serial,
) -> None:
    subscription_type = payload.get("subscription", {}).get("type")
    event = payload.get("event", {})

    print(f"Evenement recu : {subscription_type}")
    print(f"Details : {event}")

    handle_twitch_event(arduino, payload)


async def connect(
    client_id: str,
    access_token: str,
    user_id: str,
    arduino: serial.Serial,
) -> None:
    print("Connexion WebSocket Twitch...")

    async with websockets.connect(TWITCH_EVENTSUB_URL) as ws:
        print("Connecte.")

        async for message in ws:
            await handle_message(message, client_id, access_token, user_id, arduino)


def start(
    client_id: str,
    access_token: str,
    user_id: str,
    arduino: serial.Serial,
) -> None:
    asyncio.run(connect(client_id, access_token, user_id, arduino))
