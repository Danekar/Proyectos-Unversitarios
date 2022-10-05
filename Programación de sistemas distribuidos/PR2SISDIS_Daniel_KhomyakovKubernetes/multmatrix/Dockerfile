#Daniel Khomyakov y Raul Martinez Llorente

FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get update
EXPOSE 3301
COPY mainServidorMultMatrix /mainServidorMultMatrix
RUN chmod +x /mainServidorMultMatrix
CMD /mainServidorMultMatrix
