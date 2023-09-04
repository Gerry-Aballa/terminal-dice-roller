import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


    

def roll_dice():
    """Simulate rolling a 6-sided die and return the result."""
    return random.randint(1, 6)

def display_dice(die_value):
    """Display the ASCII art for the given die value."""
    if die_value in DICE_ART:
        die_face = DICE_ART[die_value]
        for line in die_face:
            print(line)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        user_input = input("Press Enter to roll the dice or 'q' to quit: ").strip()
        
        if user_input == 'q':
            print("Goodbye!")
            break
        
        if user_input == '':
            die_value = roll_dice()
            display_dice(die_value)
        else:
            print("Invalid input. Press Enter to roll or 'q' to quit.")

if __name__ == "__main__":
    main()
