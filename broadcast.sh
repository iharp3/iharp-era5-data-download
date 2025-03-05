#!/bin/bash

# Iterate through the hostnames
for ((i=201; i<=210; i++)); do
    hostname="cs-spatial-${i}.cs.umn.edu"
    echo "Working on $hostname"
    year=$((2015-201+$i))
    ssh huan1531@"$hostname" << EOF
        cd /export/scratch
        rm -rf huan1531
        mkdir huan1531
        cd huan1531
        git clone https://github.com/iharp3/iharp-era5-data-download.git
        cd iharp-era5-data-download
        bash init_venv.sh
        source venv/bin/activate
        echo "Downloading data for $year"
        echo $year
        # tmux kill-server
        tmux new-session -d -s ${year} "python download.py -t download_${year}.toml" || echo "Failed to create tmux session for year ${year}"
EOF
    echo "Done"
done
