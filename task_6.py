import time 

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_items(budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]['calories'] / x[1]['cost'],
        reverse=True
    )
    result = {}
    for name, props in sorted_items:
        count = budget // props['cost']
        if count > 0:
            result[name] = count
            budget -= count * props['cost']
    return result

def dp_items(budget):
    max_calories = [0] * (budget + 1)
    used_items = [{} for _ in range(budget + 1)]

    for b in range(1, budget + 1):
        for name, props in items.items():
            cost = props["cost"]
            cal = props["calories"]
            if cost <= b:
                if max_calories[b - cost] + cal > max_calories[b]:
                    max_calories[b] = max_calories[b - cost] + cal
                    used_items[b] = used_items[b - cost].copy()
                    used_items[b][name] = used_items[b].get(name, 0) + 1

    return used_items[budget]

# сновна перевірка
try:
    budget = int(input("Введіть бюджет: "))
    if budget < 0:
        print("Бюджет має бути невід'ємним числом.")
    else:
        # Жадібний алгоритм
        start_time = time.time()
        greedy_result = greedy_items(budget)
        greedy_time = time.time() - start_time

        # Динамічне програмування
        start_time = time.time()
        dp_result = dp_items(budget)
        dp_time = time.time() - start_time

        print(f"Жадібний алгоритм: {greedy_result}, Час виконання: {greedy_time:.6f} c.")
        print(f"Динамічне програмування: {dp_result}, Час виконання: {dp_time:.6f} c.")
except ValueError:
    print("Будь ласка, введіть ціле число для бюджету.")
        