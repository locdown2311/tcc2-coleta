FROM python:3.7
ARG SSH_PRIV_KEY
WORKDIR /root
RUN mkdir ~/.ssh/
RUN echo "${SSH_PRIV_KEY}" > ~/.ssh/id_rsa
RUN chmod 600 ~/.ssh/id_rsa
RUN ssh-keyscan 200.239.152.79 > ~/.ssh/known_hosts

WORKDIR /usr/src/tcc/scripts
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY scripts/leituraControladoraRuckos.py .
COPY scripts/leituraRadius.py .
COPY scripts/readInput_ruckos.py .
COPY scripts/readSend_ruckos.py .
COPY seleciona.sh .
COPY entrypoint.sh .
WORKDIR /usr/src/tcc
RUN mkdir -p dados_brutos
RUN mkdir -p dados_filtrados

CMD [ "bash", "./entrypoint.sh" ]
