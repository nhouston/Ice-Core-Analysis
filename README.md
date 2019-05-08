Ice Core Analysis
------------------------

The project is written in Python using libraries such as OpenCv, NumPy, matplotlib, Pillow and glob. 


**These libraries are _necessary_ for the program to run and will _need to be installed before running the program._**


Python comes pre-installed on most devices however Python 3 will need to be installed to work in conjunction with the program. 

The steps to follow and install Python 3 can be found here:

https://www.python.org/downloads/

When installed, to make sure that Python 3 is being used as the default Python, an alias may need to be created to prevent Python 2.7 being used. 
```
alias python=python3
```
-------------------------

The libraries that the project uses can found and installed from these websites or using the provided commands on the command line:

OpenCV:
-------
https://opencv.org/releases/

NumpPy:
-------

**This command will also install the library matplotlib that is required by the program**
```
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```

Pillow:
-------

https://pillow.readthedocs.io/en/stable/installation.html

or install using the command:

```
pip install Pillow
```

Glob:
------

https://pypi.org/project/glob2/

or install using the command:

```
pip install glob2
```

Contained in the project
------------------------

The content in this project contains research steps for normalising the images, sharpening the images and detecting artefact lines in the images. It provides different methods for normalising the images with Histogram matching as the best option. Images will also be sharpended and noise removed.
Vertical artefact lines can also be detected however only their appearance can be reduced and not fully removed from the image. 

Areas that were completed were:
- Normalising the image
- Sharpening

Partially completed areas:
- The removal of vertical artefact lines

Subsequent steps for splicing and remergeing the images are also included in the project

Folders that are being used for the project are contained in a folder named ImageAnalysis. **This folder must be located in the users Documents Directory for the program to work.** The program will work for both Mac OS and Linux distributions. 

Image Files
------------------------

Image files that are related to the project will be handed in separately due to the file sizes in question. These can be obtained from OneDrive using the link provided:

https://prifysgolaber-my.sharepoint.com/:f:/g/personal/neh1_aber_ac_uk/EnRSi1OucOVOrvrSdQH-s-8Bq_-OQ0uSh7UvRB4za0I4VQ?e=sNSQAb


The images for the program can also be obtained from Bryn Hubbard from the Department of Geography & Earth Sciences. Extra images may also be available from Bryn.

These images for use in the project can be stored anywhere in a system but for best results locating the images in the project folder will yield this.

If storing outside the project folder the full directory to the image will be needed. 

**Running the program**
----------------------

Running the program takes place from the command line.

To run the program you must be in the project folder directory through command line:

To do this a command like below should be used:

```
cd Documents/ImageAnalysis.nosync
```

Once in the directory, the program can simply be run by typing the following command:

```
python menu.py
```

Running this command will the program in its entirety 




