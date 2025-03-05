#!/bin/bash

# Iterate through the hostnames
for ((i=501; i<=512; i++)); do
    hostname="cs-spatial-${i}.cs.umn.edu"
    echo "Working on $hostname"
    ssh huan1531@"$hostname" << EOF
        cd /export/scratch
        cd huan1531
        rm -rf iharp-era5-data-download
        rm -rf iharp-era5_data_download
EOF
    echo "Done"
done
