#!/bin/bash
# Path: entrypoint.sh

#run leituraGeral.py first
python leituraGeral.py
#run seleciona.sh for each file in /scripts, skip if leituraGeral.py
for file in /scripts/*; do
    if [ "$file" != "/scripts/leituraGeral.py" ]; then
        echo "Running $file"
        /seleciona.sh $file
    fi
done
