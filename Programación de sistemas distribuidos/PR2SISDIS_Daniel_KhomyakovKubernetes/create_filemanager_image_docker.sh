#Daniel Khomyakov y Raul Martinez Llorente

sudo docker build ./filemanager
idimgfm=$(sudo docker images | grep '<none>' | awk '{print $3}')
sudo docker tag $idimgfm raulmllorente/filemanager:1.0
