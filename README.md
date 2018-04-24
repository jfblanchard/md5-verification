# md5-verification

<h4>verify_MD5.py</h4>

This is a command line utility that is used for verifying MD5 hashes.  It utilizes the python hashlib library.  

To use, invoke cmd.exe and run:

<code>
  python verify_MD5.py 'checksum'
   
</code>

 where 'checksum is the MD5 Hash string that was provided with the downloaded file.
 
 A file dialog will come up in which you can select the downloaded file to verify.  Once completed, the original and computed has sums will be displayed, as well as one of two messages:
 
<code>
 'SUCCESS! Message digests match'
</code>
<br> or <br>
<code>
 'FAIL!. Message digests do not match'
</code>
