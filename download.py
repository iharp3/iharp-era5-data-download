import argparse
import cdsapi
import tomllib


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--toml", required=True, help="TOML file")
    args = ap.parse_args()
    toml_file = args.toml

    # load requests: one area, one variable, all years
    era5_requests = []
    with open(toml_file, "rb") as f:
        config = tomllib.load(f)
        years = config["time"]["years"]
        for area in config["area"]:
            short_name = config["area"][area]["short_name"]
            max_lat, min_lat = config["area"][area]["lat"]
            min_lon, max_lon = config["area"][area]["lon"]
            for var in config["variable"]["variables"]:
                print(area, var)
                print(years)
                print(short_name)
                print(max_lat, min_lat, min_lon, max_lon)
                request = {
                    "product_type": ["reanalysis"],
                    "variable": [var],
                    "year": years,
                    "month": [str(i).zfill(2) for i in range(1, 13)],
                    "day": [str(i).zfill(2) for i in range(1, 32)],
                    "time": [f"{str(i).zfill(2)}:00" for i in range(24)],
                    "data_format": "netcdf",
                    "download_format": "unarchived",
                    "area": [max_lat, min_lon, min_lat, max_lon],
                }
                file_name = f"{var}_{short_name}_{years[0]}-{years[-1]}.nc"
                era5_requests.append((request, file_name))
    print(era5_requests)

    client = cdsapi.Client()
    dataset = "reanalysis-era5-single-levels"
    for request, file_name in era5_requests:
        print(f"Downloading {file_name}")
        print(request)
        client.retrieve(dataset, request).download(file_name)
