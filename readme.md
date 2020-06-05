# DFlowFM Boundary and forcing docker instructions
The following instructions will guide the user in running the gettide, getphysbio, and getforce docker containers <br/>

### Instructions on how to run the gettide container
The gettide container needs as input
+ A folder  with all your tidal constituent data
+ A polygon file, with a '.pli' extension, that contains the points at which you would like the tidal values
The gettide container creates as output a folder called 'out' that contains:
+ A file with the extension '.ext' that contains the quantity (in this case waterlevelbnd), the associated polygon filename that was used to create it and the name of the resulting forcing file that will be used in DFlowFM.
+ A file with the extension '.bc' that containes the water levels at the points specified at the positions given in the polygon (.pli) file.
+options.txt that contains the optional arguments for creating the tidal boundary:
++ The boundingbox
++ The name of the folder containing the tidal constuent data (FES data)
++The name of the polygonfile
++ . See test_costserv for an example
In order to run the gettide container, create a folder that contains wihtin it a folder called 'in'. Within this folder,
+place the folder called FES. This folder should contain all the tidal constituents in netcdf format and with naming convention: X_FES2012_SLEV.nc, where
X denotes one of the following 27 tidal constituents:
'2N2',   
            'Mf'   ,
            'P1'   ,
            'M2'   , 'MKS2' , 'Mu2'  , 'Q1'   , 'T2'  , 'J1'  , 'M3'  , 'Mm'  ,  'N2'  ,
            'R2'  ,  'K1'  ,  'M4'  ,  'MN4' ,  'S1'  ,  'K2'  ,  'M6'  , 'MS4' ,  'Nu2' ,
            'S2'  ,  'L2'  ,  'M8'  ,  'MSf' ,  'O1'  ,  'S4'.
**Note that the names are case sensitive**
Also, within the 'in' folder, place the polygon file with extension '.pli'

The gettide is then run by mounting the top folder and running the gettide code in the container. This is done with the following command:
```console
PS D:\Path_to_folder> docker run -v path_to_folder_that_contains_in:/app/data -t gettide:1.0
```
### Instructions on how to run the getphysbio container
Once gettide has been run, boundary conditions for the following parameters can also be obtained with the getphysbio container:
+'OXY', 'NO3', 'PO4', 'Si', 'PON1', 'POP1', 'POC1', 'Green', 'Diat', 'salinity', 'temperature', 'uxuy', 'steric'.
+Within the 'in' folder, created previously in order to run the gettide container, place a folder called 'data' that contains the CMEMS netcdf data with the following naming convention: X_beginDate_endDate.nc
where X denotes: o2, no3, po4, si, chl, so, thetao, uo, vo, zos
+In addition to the 'data' folder, this folder should also contain the following the ascii files:

+options_physbio.txt That contains the reference time (tref) of the DFLOWFM model in the format YYYY,MM,DD,hh,mm,ss; Interpolation options (interp and simultaneous), and a steric option which determines whether or not a steric (sealevel) boundary conditions will be created.
+The polygon file with the locations at which the boundary should be provided.

Once all the input has been provided, the getphysbio container can be run with the following command:
```console
PS D:\Path_to_folder> docker run -v path_to_folder_that_contains_in:/app/data -t getphysbio:1.0
```

The container creates DFlowFM boundary conditions (.bc) files from CMEMS netcdf files at a boundary, specified by the user as a polygon file (with .pli extension).
### Prerequisites
+ Docker desktop for windows. Obtainable from [docker for windows](https://docs.docker.com/docker-for-windows/install/).
+ A tar file of the docker image
+ A folder that contains a polygon (.pli) file with the coordinates of the boundary in lat/lon format and a folder, named 'data', that contains your downloaded CMEMS data.

### Usage
+ Launch Windows Powershell from Start Menu
+ Navigate to where you saved the docker image tar file (fmbe.tar) and run the following command:
```console
PS D:\Path_to_tar> docker load -i fmbe.tar
```
+ Ensure that your image has been successfully created from the tar file by running
```console
PS D:\Path_to_tar> docker images
```
+The above should output a docker repository with the name finewilms/fmbe

+ Run the docker container to convert the CMEMS data to boundary condition input
```console
PS D:\Path_to_folder> docker run -v path_to_folder_with_pli:/app/data -t finewilms/fmbe:1.0
```
