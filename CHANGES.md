<h3>Change log</h3>

4/30/18:
1. Reverted to use only md5 algorithm.  Next version will have more (sha256, etc.)
2. Added the verify_md5_gui.py script which provides a GUI interface.
3. Made some tweaks to the ui file.


4/24/18:
1. Updated verify_MD5.py to use the python hashlib library instead of the windows certUtil tool for platform independence.
2. Created verify_hash.py to work with both md5 and sha256 algorithms.
3. Created a hashsumverify.ui file.



