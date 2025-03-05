import cdsapi


max_lat, min_lat = 90, -90
min_lon, max_lon = -180, 180

variables = [
    "2m_temperature",
    "surface_pressure",
    "total_precipitation",
    "ice_temperature_layer_1",
    "ice_temperature_layer_2",
    "ice_temperature_layer_3",
    "ice_temperature_layer_4",
    "snow_depth",
    "snowfall",
    "snowmelt",
    "temperature_of_snow_layer",
]

file_name = "download.nc"
dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": variables,
    "year": ["2024"],
    "month": ["01"],
    "day": ["01"],
    "time": [f"{str(i).zfill(2)}:00" for i in range(24)],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [max_lat, min_lon, min_lat, max_lon],
}

client = cdsapi.Client()
client.retrieve(dataset, request).download(file_name)
