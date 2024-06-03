# allocate_resources.py
import json
import os

def load_metrics():
    with open('metrics.json', 'r') as f:
        metrics = json.load(f)
    return metrics

def allocate_resources(metrics):
    # Example policy: If CPU usage > 80%, scale up
    if metrics['cpu_usage'] > 80:
        os.system("kubectl scale --replicas=2 deployment/my-app")
    else:
        os.system("kubectl scale --replicas=1 deployment/my-app")

def main():
    metrics = load_metrics()
    allocate_resources(metrics)

if __name__ == "__main__":
    main()
