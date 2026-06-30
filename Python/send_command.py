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
def main() -> None:
    with serial.Serial(PORT, BAUD_RATE, timeout=1) as arduino:
        time.sleep(2)
        print_startup_help()
        while True:
            user_input = input("> ").strip()
            if user_input.lower() == "quit":
                print("Arret du programme.")
                break
            handle_user_input(arduino, user_input)
if __name__ == "__main__":
    main()