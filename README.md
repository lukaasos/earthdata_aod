# earthdata_aod

### Hi, i am Lucas Coringa, and this project focus on extract AOD values of .HDF files from EarthData - Nasa. Besides, this project shows how to filter the data (e.g. drop NaN, drop outliers etc.).

The "loop_hdf.ipynb" shows how to extract aod values of .HDF files and how to organize the time scale.

The "process_final" filter data and put in a dataframe. After this process, you can make your analysis.

Read the documentation of the MODIS product.

You will create a test csv file in "loop_hdf.ipynb", but you will use the others csv files to pass throug "process_final.ipynb".

#### you can download the data in https://urs.earthdata.nasa.gov/home, and the tutorial to download you can check in "tutorial_modis.pdf"