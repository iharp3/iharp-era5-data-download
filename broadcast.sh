#!/bin/bash

# Iterate through the hostnames
for ((i=201; i<=210; i++)); do
    hostname="cs-spatial-${i}.cs.umn.edu"
    echo "Working on $hostname"
    ssh huan1531@"$hostname" << EOF
    cd /export/scratch
    rm -rf huan1531
    mkdir huan1531
    cd huan1531
    git clone https://github.com/iharp3/iharp-era5-data-download.git
    cd iharp-era5-data-download
    bash init_venv.sh
EOF
    echo "Done"
done
