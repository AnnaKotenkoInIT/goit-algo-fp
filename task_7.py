import random
import matplotlib.pyplot as plt

simulations_list = [10, 100, 1000, 10000, 100000, 1000000]

analytical_probs = {
    2: 1/36 * 100,
    3: 2/36 * 100,
    4: 3/36 * 100,
    5: 4/36 * 100,
    6: 5/36 * 100,
    7: 6/36 * 100,
    8: 5/36 * 100,
    9: 4/36 * 100,
    10: 3/36 * 100,
    11: 2/36 * 100,
    12: 1/36 * 100
}

sums = list(range(2, 13))

sum_counts = {i: 0 for i in range(2, 13)}

for num_simulations in simulations_list:
    sum_counts = {i: 0 for i in sums}

    for _ in range(num_simulations):
        total_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[total_sum] += 1

    monte_carlo_probs = {k: v / num_simulations * 100 for k, v in sum_counts.items()}

    print(f"\nКількість симуляцій: {num_simulations}")
    print(f"{'Сума':<5} {'Монте-Карло (%)':<18} {'Аналітична (%)':<15}")
    for s in sums:
        print(f"{s:<5} {monte_carlo_probs[s]:<18.2f} {analytical_probs[s]:<15.2f}")

    # Виведення графіку
    mc_values = [monte_carlo_probs[s] for s in sums]
    an_values = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10, 5))
    plt.plot(sums, mc_values, marker='o', label='Монте-Карло')
    plt.plot(sums, an_values, marker='x', label='Аналітична')
    plt.title(f"Ймовірність сум при киданні двох кубиків\n(симуляції: {num_simulations})")
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.legend()
    plt.grid(True)
    plt.show()