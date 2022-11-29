#!/bin/bash
# Path: entrypoint.sh

cd /usr/src/tcc/dados_brutos ;
./baixaLogs.sh ;
#run leituraGeral.py first
python ../scripts/leituraGeral.py

#run each .py file in /scripts, skip if leituraGeral.py and requirements.txt
for file in /usr/src/tcc/scripts/*.py; do
    if [ "$file" != "/usr/src/tcc/scripts/leituraGeral.py" ] ; then
        python "$file"
    fi
done
