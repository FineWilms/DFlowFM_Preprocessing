# DFlowFM Boundary and forcing docker instructions
The following instructions will guide the user in running the gettide, getphysbio, and getforce docker containers. <br/>

The gettide container creates tidal boundary conditions for DFlowFM from the Finite Element Solution (FES) tide model. <br/>

The getphysbio container creates boundary contditions for DFlowFM from CMEMS NetCDF data for biological and physical ocean parameters. <br/>

The getforce container creates forcing data, in NetCDF format, from ERA5 reanalysis data for DFlowFM.

### Instructions for running the gettide container
The gettide container needs as input
* A folder  with FES2012 tidal constituent data.
* A polygon file, with a '.pli' extension, that contains the points at which the boundary conditions are needed.
* A text file, options_tide.txt, that contains the optional arguments for creating the tidal boundary. These options include:
  * The bounding box
  * The name of the folder containing the tidal constituent data (FES data)
  * The name of the polygonfile

For an example of such an 'options.txt' file, refer to the included test case, 'test_coastserv'.

The gettide container creates as output a folder called 'out' that contains:
* A file with the extension '.ext' that contains the quantity (in this case waterlevelbnd), the associated polygon filename that was used to create it and the name of the resulting boundary condition file that will be used in DFlowFM.
* A boundary condition file with the extension '.bc' which contains the water levels at the points specified in the polygon (.pli) file.

The following directory structure is needed in order to run gettide: <br/>
In order to run the gettide container, create a folder that contains within it a folder called 'in'. Within this 'in' folder:
* Place the folder called FES. This folder should contain all the tidal constituents in netcdf format and with naming convention: X_FES2012_SLEV.nc, where
X denotes one of the following 27 tidal constituents:
  * 2N2, Mf, P1, M2, MKS2 , Mu2, Q1, T2, J1, M3, Mm,  N2, R2,  K1,  M4,  MN4 , S1,  K2, M6, MS4 , Nu2, S2,  L2,  M8,  MSf ,  O1, S4. **Note that the names are case sensitive**
* Also, within the 'in' folder, place the polygon file with extension '.pli'

The gettide is then run by mounting the top folder and running the gettide code in the container. This is done with the following command:
```console
PS D:\Path_to_folder> docker run -v path_to_folder_that_contains_in:/app/data -t gettide:1.0
```
### Instructions on how to run the getphysbio container
Once gettide has been run, boundary conditions for the following parameters can also be obtained with the getphysbio container: 'OXY', 'NO3', 'PO4', 'Si', 'PON1', 'POP1', 'POC1', 'Green', 'Diat', 'salinity', 'temperature', 'uxuy', 'steric'.
* Within the 'in' folder, created previously in order to run the gettide container, place a folder called 'data' that contains the CMEMS netcdf data with the following naming convention: X_beginDate_endDate.nc
where X denotes: o2, no3, po4, si, chl, so, thetao, uo, vo, and zos.
* In addition to the 'data' folder, this folder should also contain the following the ascii files:
  * options_physbio.txt That contains the reference time (tref) of the DFLOWFM model in the format YYYY,MM,DD,hh,mm,ss; Interpolation options (interp and simultaneous), and a steric option which determines whether or not a steric (sealevel) boundary conditions will be created.
  * The polygon file with the locations at which the boundary should be provided.

Once all the input has been provided, the getphysbio container can be run with the following command:
```console
PS D:\Path_to_folder> docker run -v path_to_folder_that_contains_in:/app/data -t getphysbio:1.0
```
### Prerequisites
+ Docker desktop for windows. Obtainable from [docker for windows](https://docs.docker.com/docker-for-windows/install/).
+ A tar file of the docker image
+ A folder that contains a polygon (.pli) file with the coordinates of the boundary in lat/lon format and a folder, named 'data', that contains your downloaded CMEMS data.

### Instructions for running the getforces container
* Create a folder called 'in', and place the downloaded ERA5 data within this folder. The filenames should have the following format: ERA5_YYYY.nc
The container is then run by typing in the following command in the terminal:
```console
PS D:\Path_to_folder> docker run -v path_to_folder_that_contains_in:/app/data -t getforce:1.0
```




