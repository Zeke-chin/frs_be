FROM ubuntu:18.04 AS builder
RUN sed -i 's#archive.ubuntu.com#mirrors.aliyun.com#g' /etc/apt/sources.list  \
    && sed -i 's#security.ubuntu.com#mirrors.aliyun.com#g' /etc/apt/sources.list

ENV LANG=zh_CN.UTF-8 LANGUAGE=zh_CN:zh LC_ALL=zh_CN.UTF-8 DEBIAN_FRONTEND=noninteractive

RUN rm -rf  /etc/apt/sources.list.d/  && apt update

RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    iputils-ping \
    wget \
    zsh \
    build-essential \
    cmake \
    git \
    curl \
    vim \
    ca-certificates \
    libjpeg-dev \
    zip \
    unzip \
    libpng-dev \
    openssh-server \
    autojump \
    language-pack-zh-hans \
    ttf-wqy-zenhei \
    libgl1-mesa-glx  \
    libglib2.0-0 \
    locales \
    nfs-common \
    libmagic1 \
    ranger \
    tmux



RUN locale-gen zh_CN.UTF-8
RUN dpkg-reconfigure locales

ENV TZ Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    echo "Asia/Shanghai" > /etc/timezone

CMD ["supervisord", "-n"]

FROM builder as builder1

ENV PYTHON_VERSION 3
RUN chsh -s `which zsh`
RUN curl -o ~/miniconda.sh -O  https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda${PYTHON_VERSION}-latest-Linux-x86_64.sh  && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

RUN ln /opt/conda/bin/conda /usr/local/bin/conda
RUN conda init zsh
