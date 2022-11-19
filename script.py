import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import netCDF4 as nc
import geopandas as geo
import dask
import rioxarray
import gc
import glob
from mpl_toolkits.basemap import Basemap

year_list = range(1981,2022)  #still  incomplete loop

fn = 'D:/t2m/t2m_025x025_2001_x1h.nc'  #here we read only one, every file is 17GB.
ds = xr.open_dataset(fn)
#all_files=xr.open_mfdataset('D:/t2m/*.nc', parallel=True) opción 2
tco = ds.t2m # Dimensions: 
tco1_min = tco.resample(time="D").min()
tco_mean_min=np.mean(tco1_min, axis=0)
tco1_max = tco.resample(time="D").max()
tco_mean_max=np.mean(tco1_max, axis=0)
tco_mean_max.rio.to_raster("2001_max.tif")
tco_mean_min.rio.to_raster("2001_min.tif")

#plot raster
import rasterio as rr
from rasterio.plot import show
raster = rr.open("1981_max.tif")
show(raster)
