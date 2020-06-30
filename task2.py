time_user = int(input("Введите время в секундах:"))
time_hour = time_user // 3600
time_min = (time_user % 3600) // 60
time_sec = (time_user % 3600) % 60
print(f"В часах, минутах и секундах это сосавит:\n{time_hour:02d}:{time_min:02d}:{time_sec:02d}")
