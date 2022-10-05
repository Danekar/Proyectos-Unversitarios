nodename=$(kubectl get nodes | sed -n '2 p' | awk '{print $1}')
kubectl taint node $nodename node-role.kubernetes.io/master-
