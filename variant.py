total = int(input("Общий обьем: "))
capacity = int(input("Вместимость одной единицы: "))
full = total // capacity
remainder = total % capacity
units_needed = (total + capacity - 1) // capacity
print(f"Полных единиц: {full}")
print(f"Остаток: {remainder}")
print(f"Минимальное число единиц: {units_needed}")