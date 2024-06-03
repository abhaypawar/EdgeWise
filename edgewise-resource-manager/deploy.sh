#!/bin/bash
# deploy.sh

# Build Docker images
docker build -t edge-monitor -f Dockerfile.monitor .
docker build -t resource-allocator -f Dockerfile.allocator .

# Push Docker images to a registry (Docker Hub in this case)
docker push your-dockerhub-username/edge-monitor
docker push your-dockerhub-username/resource-allocator

# Deploy to Kubernetes
kubectl apply -f k8s-deployment.yaml
