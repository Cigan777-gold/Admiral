import psutil
import time

def get_server_io_status():
    """Получение статуса сервера через psutil"""
    # CPU метрики
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)
    cpu_freq = psutil.cpu_freq()
    
    # I/O метрики
    disk_io = psutil.disk_io_counters()
    net_io = psutil.net_io_counters()
    
    # Загрузка памяти
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    # Load average
    load_avg = psutil.getloadavg()
    
    return {
        'cpu': {
            'total_percent': cpu_percent,
            'per_core': cpu_per_core,
            'frequency_current': cpu_freq.current if cpu_freq else None,
            'load_avg_1min': load_avg[0],
            'load_avg_5min': load_avg[1],
            'load_avg_15min': load_avg[2]
        },
        'memory': {
            'total': memory.total,
            'available': memory.available,
            'percent': memory.percent,
            'used': memory.used,
            'swap_percent': swap.percent
        },
        'io': {
            'disk_read_bytes': disk_io.read_bytes,
            'disk_write_bytes': disk_io.write_bytes,
            'disk_read_count': disk_io.read_count,
            'disk_write_count': disk_io.write_count,
            'net_bytes_sent': net_io.bytes_sent,
            'net_bytes_recv': net_io.bytes_recv
        }
    }

# Определение уровня перегруженности
def get_server_overload_level():
    status = get_server_io_status()
    
    # Определение порогов
    cpu_load = status['cpu']['total_percent']
    load_avg = status['cpu']['load_avg_1min']
    memory_load = status['memory']['percent']
    cpu_cores = psutil.cpu_count()
    
    # Нормализованный load average (относительно количества ядер)
    normalized_load = load_avg / cpu_cores
    # print (normalized_load)
    # print(cpu_load)
    # print(memory_load)
    
    if cpu_load > 90 or normalized_load > 1.5 or memory_load > 90:
        return "CRITICAL"
    elif cpu_load > 70 or normalized_load > 1.0 or memory_load > 80:
        return "HIGH"
    elif cpu_load > 50 or normalized_load > 0.7 or memory_load > 70:
        return "MEDIUM"
    else:
        return "LOW"

# Мониторинг в реальном времени
def monitor_server(interval=5):
    """Постоянный мониторинг сервера"""
    try:
        while True:
            level = get_server_overload_level()
            status = get_server_io_status()
            
            print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}]")
            print(f"Overload Level: {level}")
            print(f"CPU: {status['cpu']['total_percent']:.1f}%")
            print(f"Load Average: {status['cpu']['load_avg_1min']:.2f}")
            print(f"Memory: {status['memory']['percent']:.1f}%")
            print(f"Disk I/O: R={status['io']['disk_read_bytes']/1024/1024:.1f}MB, "
                  f"W={status['io']['disk_write_bytes']/1024/1024:.1f}MB")
            print(f"Network: ↓{status['io']['net_bytes_recv']/1024/1024:.1f}MB, "
                  f"↑{status['io']['net_bytes_sent']/1024/1024:.1f}MB")
            
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nМониторинг остановлен")

# Использование
if __name__ == "__main__":
    # Единичная проверка
    status = get_server_io_status()
    # level = get_server_overload_level()
    # print(f"Server status: {level}")
    
    # Для постоянного мониторинга раскомментировать:
    monitor_server(interval=5)