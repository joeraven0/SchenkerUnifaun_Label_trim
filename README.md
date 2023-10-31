# SchenkerUnifaun_Label_trim
Schenker Unifaun export labels as full A4. This python code trim labels to fit Zebra GK420D 192x102mm labels

Exact margins set to fit print from Adobe Reader.

Written in Python 3.12

Files in same folder as SchenkerUnifaun.py will be placed under folder crop_input and cropped pdf-files under crop_output. Set combine flag to 1 in code to combine output file, 0 to save to separate files.
```
C:\USERS\USER\DROPBOX\AUTOMATISERING\SCHENKER
│   a4trim.jpg
│   SchenkerTrim.bat
│   SchenkerUnifaun.py
│
├───crop_input
│       prt779552533_0.pdf
│       prt779552539_0.pdf
│
└───crop_output
        combined_20231031_194547.pdf
```
![alt text](a4trim.jpg)
## Setup
1. Change filepath where trp*.pdf files are located
2. Change bat filepath to where SchenkerUnifaun.py is located (optional if you want to run from bat-file)
