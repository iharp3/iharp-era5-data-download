# iharp-era5-data-download


cd /export/scratch/huan1531/iharp-era5_data_download/

source venv/bin/activate

tmux new -d -s 2015 "python download.py -t download_2015.toml"
tmux new -d -s 2016 "python download.py -t download_2016.toml"
tmux new -d -s 2017 "python download.py -t download_2017.toml"
tmux new -d -s 2018 "python download.py -t download_2018.toml"
tmux new -d -s 2019 "python download.py -t download_2019.toml"
tmux new -d -s 2020 "python download.py -t download_2020.toml"
tmux new -d -s 2021 "python download.py -t download_2021.toml"
tmux new -d -s 2022 "python download.py -t download_2022.toml"
tmux new -d -s 2023 "python download.py -t download_2023.toml"
tmux new -d -s 2024 "python download.py -t download_2024.toml"
