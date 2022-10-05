kubectl create deployment ytaws --image=raulmllorente/ytaws:1.0
sudo nano /etc/kubernetes/manifests/kube-apiserver.yaml #modificar con '- --service-node-port-range=1-22767 despues de - --service-cluster-ip-range=10.96.0.0/12'
sleep 60
kubectl apply -f mariadbApache.yaml
