# -*- coding: utf-8 -*-
"""
Functions for performing a MD5 hash sum verification.

Calls the windows program certUtil.
Nexst version will run from the python language for platform independance.

Warn the user that MD5 has been broken.

"""

import subprocess, sys
from tkinter import Tk
from tkinter import filedialog


#bring up a dialog to select a file-----------------------------------------
def get_file(myTitle=None):
    
    """ Displays Tk GUI to select a file for processing 
    
    Parameters
    ----------
    myTitle : str
        String to use for the message displayed. 
    """
    
    Tk().withdraw()                #keep the root window from appearing
    filename = filedialog.askopenfilename(title=myTitle)       #select top level directory
    return filename

                    

def verify_MD5(hash_sum, filename):
    


    out = subprocess.check_output('certUtil -hashfile '+filename +' MD5')
    start = out.find(b'\n') + 1 #starts right after the first '\n'
    end = out.find(b'CertUtil')-2
                  
    md5_string = str('')
    for i in range(start, end, 2):
        md5_string = md5_string + out[i:i+2].decode('utf-8')
    
    md5_string = md5_string[0:-1]           #remove the \r at end
    md5_string = md5_string.replace(' ','')   #remove white spaces...make optional?

    print ('MD5 Hash Sum: ' + md5_string)
    print ('Computed: ' + md5_string)
    if md5_string == hash_sum:
        print ('SUCCESS! Sums match')
    else:
        print('FAIL!. Sums do not match')

    

if __name__ == '__main__':
    
    hash_sum = sys.argv[1]
    fname = get_file('Please choose a file for MD5 checksum')
    verify_MD5(hash_sum, fname)
    


