#Daniel Khomyakov y Raul Martinez Llorente

kubectl apply -f filemanager.yaml
sleep 10
fmpod=$(kubectl get pods | grep 'filemanager' | awk '{print $1}'| head -n 1)
kubectl cp filemanager/dirpruebabackup/. $fmpod:/dirprueba
