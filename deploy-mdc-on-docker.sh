#!/bin/bash
#Requisitos git, docker e docker-compose instalados.

#Baixar docker:
#https://docs.docker.com/get-docker/

#Baixar git:
#https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

#Baixar docker-compose
#https://docs.docker.com/compose/install/


########################################################
###### Parameters
########################################################
GIT_REPOSITORY01='https://github.com/lapig-ufg/mdc.git'

clear
echo "Verificando se o docker esta instalado no sistema!."
sleep 2
clear
echo "Verificando se o docker esta instalado no sistema!.."
sleep 2
clear
echo "Verificando se o docker esta instalado no sistema!..."
sleep 2
clear

if [[ $(which docker) ]]; then
    clear
    echo "Docker Instalado No Sistema!"
    sleep 2
  else
    clear
    echo "Docker Nao Instalado No Sistema!"
    sleep 2
    exit 0
fi

clear
echo "Verificando se o docker-compose esta instalado no sistema!."
sleep 2
clear
echo "Verificando se o docker-compose esta instalado no sistema!.."
sleep 2
clear
echo "Verificando se o docker-compose esta instalado no sistema!..."
sleep 2
clear

if [[ $(which docker-compose) ]]; then
    clear
    echo "Docker-Compose Instalado No Sistema!"
    sleep 2
  else
    clear
    echo "Docker-Compose Nao Instalado No Sistema!"
    sleep 2
    exit 0
fi

if [[ $(which git) ]]; then
    clear
    echo "Git Instalado No Sistema!"
    sleep 2
  else
    clear
    echo "Git Nao Instalado No Sistema!"
    sleep 2
    exit 0
fi

Inicio(){
clear
echo -e -n "Digite o local onde a estrutura de pastas do projeto MODIS Data Cube devera ser criada: "
read deseja

cd $deseja

if [ "$?" -ne 0 ]; then
clear
echo -e -n "Erro!, caminho informado inexistente!"
sleep 2
Inicio
fi

}

Inicio

cd $deseja

mkdir MDC_LAPIG

cd MDC_LAPIG

mkdir APP

cd APP

git clone https://github.com/lapig-ufg/mdc

mv mdc/ MRT/

cd /tmp/

pip install gdown

mkdir -p /tmp/gdown && cd /tmp/gdown

if [ -f "/tmp/gdown/mdc_lapig_1.1.tar.gz" ]; then
    clear
    echo "MDC_LAPIG_1.1.tar.gz existe!"
    sleep 2
else
    clear
    echo -e "MDC_LAPIG_1.1.tar.gz nao existe! \n\n"
    sleep 2
    clear
    echo -e "Baixando do drive MDC_LAPIG_1.1.tar.gz! \n\n"
    sleep 2
    cd /tmp/gdown
    #Download CONTAINER MDC
    gdown https://drive.google.com/u/0/uc?id=1xD9cLubLH2-NmEdTq1DswyOO0b5wNC81
fi

command01=$(docker images | grep "mdc_lapig_1.1")

valor=$(echo $?)

if [ "$valor" != "0" ];then    
  
   zcat mdc_lapig_1.1.tar.gz| docker import - mdc_lapig_1.1
fi

command=$(docker images | grep "mdc_lapig_1.1" | awk '{print $8'})

if [ "$command" == "0B" ];then    
  
    clear
    echo "Falha ao importar o container MDC_LAPIG_1.1!"
    sleep 3
    docker rm -f mdc_lapig_1.1
    docker rmi -f mdc_lapig_1.1
    cd /tmp/gdown.pl
    rm -rfv mdc_lapig_1.1.tar.gz
    ./gdown.pl https://drive.google.com/file/d/1xD9cLubLH2-NmEdTq1DswyOO0b5wNC81/view?usp=sharing mdc_lapig_1.1.tar.gz
    zcat mdc_lapig_1.1.tar.gz| docker import - mdc_lapig_1.1
else
  echo "Container Importado com Sucesso!"
fi

cat <<'EOF' > $deseja/docker-compose.yml
version: '3.7'

services:

    MDC_LAPIG:

      hostname: MDC_LAPIG
      container_name: MDC_LAPIG
      image: mdc_lapig_1.1 
      networks:
        rede_apps:
          ipv4_address: 172.18.0.17
      restart: always
      ports:
        - '6379:6379/udp'
        - '6379:6379/tcp'
      expose:
        - '6379'
      #command: /bin/bash
      command: bash -c "/APP/start.sh && /bin/bash"
      stdin_open: true
      tty: true
      volumes:
        - 'VALOR01:/APP'
        - '/etc/localtime:/etc/localtime'   
networks:
 rede_apps:
   external: true
   driver: bridge
EOF

sed -i "s|VALOR01|$deseja/MDC_LAPIG/APP|g" $deseja/docker-compose.yml

cat <<'EOF' > $deseja/MDC_LAPIG/APP/start.sh
#!/bin/bash

/etc/init.d/redis-server start &

EOF

chmod -R 777 $deseja/MDC_LAPIG


#Criando rede LAPIG
docker network create \
  --driver=bridge \
  --subnet=172.18.0.0/16 \
  --ip-range=172.18.0.0/24 \
  --gateway=172.18.0.254 \
  rede_apps

cd $deseja

docker-compose up -d
