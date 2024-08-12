Project to extract and filter AOD data from .HDF files

## Hi, I’m Lucas Coringa, and this project is focused on extracting Aerosol Optical Depth (AOD) values from .HDF files provided by NASA’s EarthData. Additionally, the project demonstrates how to filter and clean the data, such as removing NaN values and outliers.

In the "loop_hdf.ipynb" notebook, you'll find instructions on how to extract AOD values from .HDF files and organize the data on a time scale. In this notebook, the criterion of Remer et al (2013) was used.

The "process_final.ipynb" notebook filters the extracted data and structures it into a DataFrame, preparing it for further analysis.

Make sure to review the MODIS product documentation before you begin.

You'll create a test CSV file in "loop_hdf.ipynb," but the subsequent CSV files will be processed using "process_final.ipynb."

### You can download the necessary data from EarthData, and refer to "tutorial_modis.pdf" for guidance on the download process.