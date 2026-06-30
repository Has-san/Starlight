import time
import serial

PORT = "COM3"   # A adapter
BAUD_RATE = 9600

VALID_COLORS = {"RED", "GREEN", "BLUE", "YELLOW", "PURPLE", "WHITE"}
MANUAL_COMMANDS = {"ON", "OFF", "BLINK"}
TWITCH_EVENT_MAPPING = {
    "channel.follow": "follow",
    "channel.subscribe": "sub",
    "channel.raid": "raid",
    "channel.bits": "bits",
}

EVENTS = {
    "follow": {
        "action": "BLINK",
        "color": "BLUE",
        "count": 5,
        "duration": 250,
    },
    "sub": {
        "action": "BLINK",
        "color": "PURPLE",
        "count": 10,
        "duration": 150,
    },
    "raid": {
        "action": "BLINK",
        "color": "YELLOW",
        "count": 15,
        "duration": 100,
    },
    "bits": {
        "action": "BLINK",
        "color": "GREEN",
        "count": 7,
        "duration": 200,
    },
    "warning": {
        "action": "ON",
        "color": "RED",
    },
    "clear": {
        "action": "OFF",
    },
}

def normalize_text(text: str) -> str:
    return text.strip()

def normalize_event_name(event_name: str) -> str:
    return normalize_text(event_name).lower()

def get_event_config(event_name: str) -> dict | None:
    normalized_event = normalize_event_name(event_name)
    return EVENTS.get(normalized_event)

def build_command_from_config(event_config: dict) -> str:
    action = event_config["action"]
    if action == "OFF":
        return "OFF"

    if action == "ON":
        color = event_config["color"]
        return f"ON {color}"

    if action == "BLINK":
        color = event_config["color"]
        count = event_config["count"]
        duration = event_config["duration"]
        return f"BLINK {color} {count} {duration}"

    raise ValueError(f"Action non geree : {action}")

def send_command(arduino: serial.Serial, command: str) -> None:
    payload = command + "\n"
    arduino.write(payload.encode("utf-8"))
    print(f"Commande envoyee : {command}")

def is_manual_command(user_input: str) -> bool:
    cleaned_input = normalize_text(user_input)

    if not cleaned_input:
        return False

    first_word = cleaned_input.split()[0].upper()
    return first_word in MANUAL_COMMANDS


def validate_manual_command(user_input: str) -> str | None:
    parts = normalize_text(user_input).split()

    if not parts:
        print("Commande vide.")
        return None

    action = parts[0].upper()

    if action == "OFF":
        if len(parts) != 1:
            print("Format attendu : OFF")
            return None
        return "OFF"

    if action == "ON":
        if len(parts) != 2:
            print("Format attendu : ON COLOR")
            return None

        color = parts[1].upper()

        if color not in VALID_COLORS:
            print(f"Couleur invalide : {color}")
            print("Couleurs valides :", ", ".join(sorted(VALID_COLORS)))
            return None

        return f"ON {color}"

    if action == "BLINK":
        if len(parts) != 4:
            print("Format attendu : BLINK COLOR COUNT DURATION")
            return None

        color = parts[1].upper()

        if color not in VALID_COLORS:
            print(f"Couleur invalide : {color}")
            print("Couleurs valides :", ", ".join(sorted(VALID_COLORS)))
            return None

        try:
            count = int(parts[2])
            duration = int(parts[3])
        except ValueError:
            print("COUNT et DURATION doivent etre des entiers.")
            return None

        if count <= 0:
            print("COUNT doit etre strictement positif.")
            return None

        if duration <= 0:
            print("DURATION doit etre strictement positive.")
            return None

        return f"BLINK {color} {count} {duration}"

    print(f"Commande manuelle inconnue : {action}")
    print("Commandes valides : ON, OFF, BLINK")
    return None

def handle_twitch_event(arduino: serial.Serial, payload: dict) -> None:
    subscription = payload.get("subscription", {})
    event = payload.get("event", {})
    event_type = subscription.get("type")
    if event_type is None:
        print("Payload Twitch invalide : type d'evenement manquant.")
        return
    print(f"Evenement Twitch recu : {event_type}")
    if event_type in TWITCH_EVENT_MAPPING:
        internal_event = TWITCH_EVENT_MAPPING[event_type]
        print(f"Evenement interne declenche : {internal_event}")
        trigger_event(arduino, internal_event)
        return
    if event_type == "channel.channel_points_custom_reward_redemption.add":
        reward = event.get("reward", {})
        reward_title = reward.get("title")
        if reward_title is None:
            print("Reward Twitch sans titre.")
            return
        print(f"Channel points redeem : {reward_title}")
        if reward_title == "Alerte rouge":
            send_command(arduino, "ON RED")
            return
        if reward_title == "Flash jaune":
            send_command(arduino, "BLINK YELLOW 5 200")
            return
        print(f"Reward non geree : {reward_title}")
        return
    print(f"Type d'evenement Twitch non gere : {event_type}")

def handle_manual_command(arduino: serial.Serial, user_input: str) -> None:
    validated_command = validate_manual_command(user_input)

    if validated_command is None:
        return

    print("Commande manuelle detectee.")
    send_command(arduino, validated_command)


def trigger_event(arduino: serial.Serial, event_name: str) -> None:
    event_config = get_event_config(event_name)

    if event_config is None:
        print(f"Evenement inconnu : {event_name}")
        print("Evenements disponibles :", ", ".join(EVENTS.keys()))
        return

    normalized_event = normalize_event_name(event_name)
    command = build_command_from_config(event_config)

    print(f"Evenement recu : {normalized_event}")
    print(f"Configuration : {event_config}")
    print(f"Commande generee : {command}")

    send_command(arduino, command)


def handle_user_input(arduino: serial.Serial, user_input: str) -> None:
    cleaned_input = normalize_text(user_input)

    if not cleaned_input:
        return

    if is_manual_command(cleaned_input):
        handle_manual_command(arduino, cleaned_input)
        return

    trigger_event(arduino, cleaned_input)


def print_startup_help() -> None:
    print("Passerelle prete.")
    print("Evenements disponibles :", ", ".join(EVENTS.keys()))
    print("Commandes manuelles : ON COLOR, OFF, BLINK COLOR COUNT DURATION")
    print("Couleurs valides :", ", ".join(sorted(VALID_COLORS)))
    print("Tape un evenement, une commande manuelle, ou 'quit' pour quitter.")

def run_fake_twitch_tests(arduino: serial.Serial) -> None:
    fake_follow = {
        "subscription": {"type": "channel.follow"},
        "event": {"user_name": "Viewer123"},
    }
    fake_sub = {
        "subscription": {"type": "channel.subscribe"},
        "event": {"user_name": "Viewer456"},
    }
    fake_raid = {
        "subscription": {"type": "channel.raid"},
        "event": {"from_broadcaster_user_name": "StreamerXYZ", "viewers": 42},
    }
    fake_bits = {
        "subscription": {"type": "channel.bits"},
        "event": {"user_name": "Viewer456"},
    }
    fake_reward_red = {
        "subscription": {
            "type": "channel.channel_points_custom_reward_redemption.add"
        },
        "event": {
            "user_name": "Viewer789",
            "reward": {
                "title": "Alerte rouge"
            }
        },
    }
    fake_reward_yellow = {
        "subscription": {
            "type": "channel.channel_points_custom_reward_redemption.add"
        },
        "event": {
            "user_name": "Viewer999",
            "reward": {
                "title": "Flash jaune"
            }
        },
    }
    tests = [
        fake_follow,
        fake_sub,
        fake_raid,
        fake_bits,
        fake_reward_red,
        fake_reward_yellow,
    ]
    for payload in tests:
        handle_twitch_event(arduino, payload)
        time.sleep(1)


def main() -> None:
    with serial.Serial(PORT, BAUD_RATE, timeout=1) as arduino:
        time.sleep(2)
        print_startup_help()

        while True:
            user_input = input("> ").strip()

            if user_input.lower() == "quit":
                print("Arret du programme.")
                break

            if user_input.lower() == "test_twitch":
                run_fake_twitch_tests(arduino)
                continue
            handle_user_input(arduino, user_input)


if __name__ == "__main__":
    main()

