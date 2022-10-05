#Daniel Khomyakov y Raul Martinez Llorente

FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get update
EXPOSE 3302
COPY mainServidor /mainServidor
RUN chmod +x mainServidor
CMD /mainServidor
COPY dirpruebabackup /dirprueba
