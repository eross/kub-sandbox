# Kubernetes on WSL2

## node setup

[How To](https://kubernetes.io/blog/2020/05/21/wsl-docker-kubernetes-on-the-windows-desktop/)

Key commands

- kind create cluster --name wslkind
- kubectl get nodes
- kubectl get all --all-namespaces
- kind delete cluster --name wslkind
- kind create cluster --name wslkind --config kind-3nodes.yaml
- kubectl get nodes

Check the services for the whole cluster

- kubectl get all --all-namespaces

Delete the on node cluster

- kubectl delete cluster --name wslkind

Create 3 node cluster

```
cat << EOF > kind-3nodes.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
EOF
```

- kind create cluster --name wslkindmultinodes --config ./kind-3nodes.yaml
- kubectl get nodes
  See that services are duplicated
- kubectl get all --all-namespaces

## Dashboard setup

```
https://github.com/kubernetes/dashboard
```

```
# Install the Dashboard application into our cluster
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-rc6/aio/deploy/recommended.yaml
# Check the resources it created based on the new namespace created
kubectl get all -n kubernetes-dashboard
```
