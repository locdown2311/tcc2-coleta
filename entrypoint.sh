#!/bin/bash
# Path: entrypoint.sh

cd /usr/src/tcc/dados_brutos ;

#run leituraGeral.py first
python ../scripts/leituraGeral.py
#run seleciona.sh for each file in /scripts, skip if leituraGeral.py
for file in ../scripts/*; do
    if [ "$file" != "../scripts/leituraGeral.py" ]; then
        echo "Running $file"
        python $file
    fi
done
