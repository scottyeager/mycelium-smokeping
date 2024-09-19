FROM lscr.io/linuxserver/smokeping

RUN apk add openssh

RUN wget https://github.com/threefoldtech/mycelium/releases/download/v0.5.4/mycelium-x86_64-unknown-linux-musl.tar.gz && \
    tar -C /usr/local/bin -xf mycelium-x86_64-unknown-linux-musl.tar.gz && \
    rm mycelium-x86_64-unknown-linux-musl.tar.gz

COPY config /config

WORKDIR /config
# Add an "or true" so Docker will continue if Targets.body is ommitted
RUN cat Targets.head Targets.body Targets.tail > Targets || true

COPY etc /etc
