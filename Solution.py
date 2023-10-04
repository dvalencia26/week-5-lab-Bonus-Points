import pandas as pd
import random


data = {
    "CharacterName": ["Arwen", "Frodo", "Gimli", "Legolas"],
    "Terrain": ["Forest", "Mountain", "Swamp", "Village"],
    "Stamina": [100, 100, 100, 100]
}
df = pd.DataFrame(data)

# Forest: +10 stamina.
# Mountain: -20 stamina.
# Swamp: -30 stamina.
# Village: +15 stamina.


def stamina_adjustment(terrain):
    adjustments = {
        "Forest": random.randint(5, 15),     # Randomly adjust between 5 and 15 for Forest
        "Mountain": random.randint(-25, -15),  # Randomly adjust between -25 and -15 for Mountain
        "Swamp": random.randint(-35, -25),     # Randomly adjust between -35 and -25 for Swamp
        "Village": random.randint(10, 20)      # Randomly adjust between 10 and 20 for Village
    }
    return adjustments.get(terrain, 0)


#adjustments: {'Forest': 6, 'Mountain': -24, 'Swap': -26, 'Village': 20}
# Adjust the each character's Stamina column based on the Stamina Adjustment function (that was "saved in the previous step)


def main():
    global df
    df["Stamina Adjustment"] = df["Terrain"].apply(stamina_adjustment)
    df["Stamina"] = df["Stamina"] + df["Stamina Adjustment"]
    print(df)


if __name__ == '__main__':
    main()
