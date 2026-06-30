# twitch_api.py

import requests


TWITCH_API_BASE_URL = "https://api.twitch.tv/helix"


def build_headers(client_id: str, access_token: str) -> dict:
    return {
        "Client-Id": client_id,
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }


def get_current_user(client_id: str, access_token: str) -> dict:
    response = requests.get(
        f"{TWITCH_API_BASE_URL}/users",
        headers=build_headers(client_id, access_token),
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()

    if not data.get("data"):
        raise RuntimeError("Aucun utilisateur Twitch trouvé avec ce token.")

    return data["data"][0]


def create_eventsub_subscription(
    client_id: str,
    access_token: str,
    subscription_type: str,
    version: str,
    condition: dict,
    session_id: str,
) -> dict:
    body = {
        "type": subscription_type,
        "version": version,
        "condition": condition,
        "transport": {
            "method": "websocket",
            "session_id": session_id,
        },
    }

    response = requests.post(
        f"{TWITCH_API_BASE_URL}/eventsub/subscriptions",
        headers=build_headers(client_id, access_token),
        json=body,
        timeout=10,
    )

    response.raise_for_status()
    return response.json()


def subscribe_to_follows(
    client_id: str,
    access_token: str,
    broadcaster_user_id: str,
    moderator_user_id: str,
    session_id: str,
) -> dict:
    return create_eventsub_subscription(
        client_id=client_id,
        access_token=access_token,
        subscription_type="channel.follow",
        version="2",
        condition={
            "broadcaster_user_id": broadcaster_user_id,
            "moderator_user_id": moderator_user_id,
        },
        session_id=session_id,
    )


