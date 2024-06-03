# EdgeWise Resource Manager

EdgeWise Resource Manager is a dynamic resource allocation tool designed for edge computing devices. It monitors resource usage in real-time and adjusts resource allocation based on predefined policies to ensure optimal performance and efficiency.

## Features

- Real-time monitoring of CPU, memory, and disk usage.
- Dynamic resource allocation based on predefined policies.
- Containerized deployment using Docker.
- Orchestration with Kubernetes.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Building and Pushing Docker Images](#building-and-pushing-docker-images)
  - [Deploying to Kubernetes](#deploying-to-kubernetes)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Kubernetes
- Python 3.8+
- kubectl (Kubernetes command-line tool)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhaypawar/edgewise.git
   cd edgewise
   ./deploy.sh
   ```

2. **Deploy to Kubernetes**:
```bash
kubectl apply -f k8s-deployment.yaml
```

## Usage

### Building and Pushing Docker Images

The deploy.sh script handles the building and pushing of Docker images to Docker Hub. Ensure you replace your-dockerhub-username in the deploy.sh script and the Kubernetes deployment file with your actual Docker Hub username.

```bash
#!/bin/bash
# deploy.sh

# Build Docker images
docker build -t edge-monitor -f Dockerfile.monitor .
docker build -t resource-allocator -f Dockerfile.allocator .

# Push Docker images to a registry (Docker Hub in this case)
docker tag edge-monitor your-dockerhub-username/edge-monitor
docker tag resource-allocator your-dockerhub-username/resource-allocator

docker push your-dockerhub-username/edge-monitor
docker push your-dockerhub-username/resource-allocator

# Deploy to Kubernetes
kubectl apply -f k8s-deployment.yaml
```

### Deploying to Kubernetes

Apply the Kubernetes deployment file to set up the EdgeWise Resource Manager on your cluster.

```yaml
# k8s-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: edge-computing-manager
spec:
  replicas: 1
  selector:
    matchLabels:
      app: edge-computing-manager
  template:
    metadata:
      labels:
        app: edge-computing-manager
    spec:
      containers:
      - name: monitor
        image: your-dockerhub-username/edge-monitor
        volumeMounts:
        - mountPath: /app/metrics.json
          name: metrics-volume
      - name: allocator
        image: your-dockerhub-username/resource-allocator
        volumeMounts:
        - mountPath: /app/metrics.json
          name: metrics-volume
      volumes:
      - name: metrics-volume
        emptyDir: {}
```

### To deploy, run:

```bash
kubectl apply -f k8s-deployment.yaml
```

## Repository Structure
```txt
edgewise-resource-manager/
    monitor.py: Script to monitor CPU, memory, and disk usage.
    allocate_resources.py: Script to allocate resources based on monitored metrics.
    Dockerfile.monitor: Dockerfile for the monitoring module.
    Dockerfile.allocator: Dockerfile for the resource allocation module.
    deploy.sh: Bash script to build, tag, and push Docker images, and deploy to Kubernetes.
    k8s-deployment.yaml: Kubernetes deployment configuration.
```

## Contributing

We welcome contributions! Please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.


## Additional Notes:

1. **Replace Placeholders**: Ensure you replace `your-github-username` and `your-dockerhub-username` with your actual GitHub and Docker Hub usernames.
2. **Monitoring Script**: Adjust the `time.sleep(10)` interval in `monitor.py` if needed for more or less frequent monitoring.
3. **Resource Allocation Policy**: Update the resource allocation logic in `allocate_resources.py` to match your specific requirements or policies.

This updated README provides a complete overview and detailed instructions to set up and use the EdgeWise Resource Manager.
