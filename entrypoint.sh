#!/bin/bash
# Path: entrypoint.sh

cd /usr/src/tcc/dados_brutos ;

#run leituraGeral.py first
python ../scripts/leituraGeral.py
#run seleciona.sh for each file in /scripts, skip if leituraGeral.py and requirements.txt
for file in /usr/src/tcc/scripts/*; do
    if [ "$file" != "/usr/src/tcc/scripts/leituraGeral.py" ] && [ "$file" != "/usr/src/tcc/scripts/requirements.txt" ]; then
        python $file
    fi
done
