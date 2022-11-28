#!/bin/bash
script_name=$1
if [ -f $script_name ]; then
    echo "O arquivo $script_name existe"
    python ${script_name}
else
    echo "O arquivo $script_name não existe"
fi