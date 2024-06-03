# monitor.py
import psutil
import json
import time

def get_system_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }
    return metrics

def save_metrics(metrics):
    with open('metrics.json', 'w') as f:
        json.dump(metrics, f)

def main():
    while True:
        metrics = get_system_metrics()
        save_metrics(metrics)
        time.sleep(10)  # Collect data every 10 seconds

if __name__ == "__main__":
    main()
