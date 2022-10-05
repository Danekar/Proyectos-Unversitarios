#Daniel Khomyakov y Raul Martinez Llorente

sudo docker build ./multmatrix
idimgmul=$(sudo docker images | grep '<none>' | awk '{print $3}')
sudo docker tag $idimgmul raulmllorente/multmatrix:1.0
