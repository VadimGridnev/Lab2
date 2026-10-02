total_second = int(input("Введите количество секунд: "))
hours = total_second // 3600
minutes = (total_second % 3600) // 60
seconds = total_second % 60
print(f"{hours} ч {minutes} мин {seconds} с")