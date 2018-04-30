# md5-verification

#### 1. verify_MD5.py

This is a command line utility that is used for verifying MD5 hashes.  It utilizes the python hashlib library.  

To use, invoke a terminal (linux) or cmd.exe (windows) and run:

<code>
  python verify_MD5.py 'checksum'
</code>  
 where 'checksum is the MD5 Hash string that was provided with the downloaded file.  
<br> 
 A file dialog will come up in which you can select the downloaded file to verify.  Once completed, the original and computed has sums will be displayed, as well as one of two messages:
 
<code>
 'SUCCESS! Message digests match'  
</code>
or  
<code>
 'FAIL!. Message digests do not match'   
</code>
<br>

#### 2. verify_md5_qt.py

This is a GUI for verifying MD5 hashes.  To start the program in a shell, go into the working directory and type

```python
  python verify_md5_qt.py
```

A GUI will come up which looks something like:  
<br>

  ![GUI Image](/images/MD5_gui_blank.png)

<br>

1. Click on the 'Browse' button to select the file to verify
2. Paste (or copy) the posted hash sum into the 'original hash sum' text area
3. Click on the 'Start' button.

The output will be displayed in the output box as shown below.  
![GUI Image](/images/MD5_gui_2.png)


