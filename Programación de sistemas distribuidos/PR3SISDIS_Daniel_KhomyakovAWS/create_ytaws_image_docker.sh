sudo docker build ./
idimgfm=$(sudo docker images | grep '<none>' | awk '{print $3}')
sudo docker tag $idimgfm raulmllorente/ytaws:1.0
