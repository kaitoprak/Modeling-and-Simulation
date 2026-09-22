import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Task 4: Dice Roll Simulation
# ==========================================

np.random.seed(42)

# Number of simulations
num_rolls = 1_000_000

# ------------------------------------------
# 1. Simulate two dice
# ------------------------------------------

dice_1 = np.random.randint(
    1, 7, size=num_rolls
)

dice_2 = np.random.randint(
    1, 7, size=num_rolls
)

# Total of two dice
sums = dice_1 + dice_2

# ------------------------------------------
# 2. Calculate probabilities for sums 2-12
# ------------------------------------------

possible_sums = np.arange(2, 13)

simulated_probabilities = []

for value in possible_sums:

    probability = np.mean(sums == value)

    simulated_probabilities.append(probability)

# Theoretical probabilities
theoretical_counts = np.array([
    1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1
])

theoretical_probabilities = (
    theoretical_counts / 36
)

# ------------------------------------------
# 3. Display results
# ------------------------------------------

print("==========================================")
print("TWO DICE SIMULATION")
print("==========================================")

for i in range(len(possible_sums)):

    print(
        f"Sum {possible_sums[i]:2d} | "
        f"Simulated = {simulated_probabilities[i]:.4f} | "
        f"Theoretical = {theoretical_probabilities[i]:.4f}"
    )

# Probability of rolling 7
probability_7 = np.mean(sums == 7)

print()
print(f"Probability of rolling 7:")
print(f"Simulated   : {probability_7:.4f}")
print(f"Theoretical : {6 / 36:.4f}")

# ------------------------------------------
# 4. Visualize dice sum distribution
# ------------------------------------------

plt.figure(figsize=(10, 6))

x = possible_sums

width = 0.35

plt.bar(
    x - width / 2,
    simulated_probabilities,
    width=width,
    label="Simulated"
)

plt.bar(
    x + width / 2,
    theoretical_probabilities,
    width=width,
    label="Theoretical"
)

plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability")
plt.title("Probability Distribution of Two Dice")
plt.xticks(x)
plt.legend()
plt.grid(axis="y")

plt.show()


# ==========================================
# CRAPS SIMULATION
# ==========================================

def roll_two_dice():
    """
    Roll two six-sided dice.
    Returns the sum.
    """
    die_1 = np.random.randint(1, 7)
    die_2 = np.random.randint(1, 7)

    return die_1 + die_2


def simulate_craps(num_games):
    """
    Simulate the game of craps.

    Rules:
    - Come-out roll 7 or 11 -> WIN
    - Come-out roll 2, 3, or 12 -> LOSE
    - 4, 5, 6, 8, 9, 10 -> establish POINT
    - Continue rolling:
        point -> WIN
        7 -> LOSE
    """

    wins = 0
    losses = 0

    for _ in range(num_games):

        # First roll
        first_roll = roll_two_dice()

        # Immediate outcomes
        if first_roll in [7, 11]:
            wins += 1
            continue

        if first_roll in [2, 3, 12]:
            losses += 1
            continue

        # Establish point
        point = first_roll

        # Continue rolling
        while True:

            roll = roll_two_dice()

            if roll == point:
                wins += 1
                break

            if roll == 7:
                losses += 1
                break

    return wins, losses


# ------------------------------------------
# 5. Run Craps simulation
# ------------------------------------------

num_games = 1_000_000

wins, losses = simulate_craps(num_games)

win_probability = wins / num_games
loss_probability = losses / num_games

print()
print("==========================================")
print("CRAPS SIMULATION")
print("==========================================")

print(f"Number of Games : {num_games}")
print(f"Wins             : {wins}")
print(f"Losses           : {losses}")

print(f"Win Probability  : {win_probability:.4f}")
print(f"Loss Probability : {loss_probability:.4f}")

# Theoretical probability of winning craps
theoretical_win_probability = 244 / 495

print()
print(
    f"Theoretical Win Probability : "
    f"{theoretical_win_probability:.4f}"
)

# ------------------------------------------
# 6. Visualize Craps results
# ------------------------------------------

plt.figure(figsize=(8, 6))

labels = ["Win", "Lose"]
values = [win_probability, loss_probability]

plt.bar(
    labels,
    values
)

plt.ylabel("Probability")
plt.title("Monte Carlo Simulation of Craps")
plt.grid(axis="y")

plt.show()