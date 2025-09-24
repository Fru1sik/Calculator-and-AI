import re

text = input("Жағдайды сипаттаңыз: ")

numbers = list(map(int, re.findall(r'\d+', text)))

words = text.split()
names = [word for word in words if word.istitle()]

take_words = ["алды", "алдырады", "алдым", "алдың", "алдым"]
give_words = ["берді", "бердім", "бердің", "береді"]

lower_words = [w.lower() for w in words]

state = {}

for name in names:
    action_taken = 0
    action_given = 0
    for i, w in enumerate(lower_words):
        if name.lower() in w:
            window = lower_words[max(0, i-3):i+4]
            for tw in take_words:
                if tw in window:
                    if numbers:
                        action_taken = numbers.pop(0)
            for gw in give_words:
                if gw in window:
                    if numbers:
                        action_given = numbers.pop(0)
    total = action_taken + action_given
    remaining = total - action_taken
    state[name] = {"Барлығы": total, "Алып кетті": action_taken, "Қалды": remaining}

for person, info in state.items():
    print(f"{person} - барлығы: {info['Барлығы']}")
    print(f"Алып кетті - {info['Алып кетті']}")
    print(f"Қалды - {info['Қалды']}")
    print()
