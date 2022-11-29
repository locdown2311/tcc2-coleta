#!/bin/bash
rm -rf 10.0.*
rm -rf pfSenseRadios.icea.ufop
ssh igor@200.239.152.79 'rm -rf /home/logs/10.0.* && rm -rf /home/logs/pfSenseRadios.icea.ufop'
