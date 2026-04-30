from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n")
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n")

        if command.upper() == "X":
            break

        parts = command.split()

        if len(parts) == 2:
            action = parts[0].upper()
            feet = int(parts[1])

            if action == "A":
                aircraft.climb(feet)
            elif action == "D":
                aircraft.descend(feet)

    print(f"Final altitude: {aircraft.altitude} feet")


if __name__ == "__main__":
    main()