podname=$(kubectl get pods | sed -n '2 p' | awk '{print $1}')
kubectl exec -it $podname -- bash
