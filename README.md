# md5-verification

This repository contains two python scripts for verifying files using a MD5 Hash Algorithm.  The first **_verify_MD5.py_** is a comand line utilty, where **_verify_Md5_gui.py_** is a GUI version with the same functionality. They each use the python hashlib library for computing the message digests.  Usage for both are described in more detail below. <br>

#### Usage: verify_MD5.py

This is a command line utility that is used for verifying MD5 hashes.  
To use, invoke a terminal (linux) or cmd.exe (windows) and run:
```python
  python verify_MD5.py 'checksum'
``` 


 where 'checksum is the MD5 Hash string that was provided with the downloaded file.  
 
 
 A file dialog will come up in which you can select the downloaded file to verify.  Once completed, the original and computed has sums will be displayed, as well as one of two messages:  
 
`'SUCCESS! Message digests match' ` 

or 

`'FAIL!. Message digests do not match'`


#### Usage: verify_md5_qt.py

This is a GUI for verifying MD5 hashes.  To start the program in a shell, go into the working directory and type

```python
  python verify_md5_qt.py
```

A GUI will come up which looks something like:  


  ![GUI Image](/images/MD5_gui_blank.png)
  
  
1. Click on the 'Browse' button to select the file to verify
2. Paste (or copy) the posted hash sum into the 'original hash sum' text area
3. Click on the 'Start' button.

If it finds a successful match, the output will be displayed in the output box as shown below.  


![GUI Image](/images/MD5_gui_2.png)


Otherwise, the message will indicated a failed match.



