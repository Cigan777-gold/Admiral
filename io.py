import psutil

cpu_times = psutil.cpu_times_percent(interval=1)

print(f"IO wait: {cpu_times.iowait}%")