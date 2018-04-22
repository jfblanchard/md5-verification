# md5-verification

This contains a function for verifying MD5 hashsums.  It is simply a python wrapper for the windows utility CertUtil, and consequently certUtil must be available and it currently works on windows only.  I plan change this soon.

To use, invoke cmd.exe and run:

<code>
  python verify_MD5.py 'checksum
   
</code>
<br>
 where 'checksum is the MD5 Hash sum that was provided with the downloaded file.
 
 A file gui will come up in which you can select the downloaded file to verify.  Once completed, the original and computed has sums will be displayed, as well as one of two messages:
 
<code>
 FAIL!. Sums do not match.
</code>
 or
<code>
 'SUCCESS! Sums match'
</code>
