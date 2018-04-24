# -*- coding: utf-8 -*-
"""
Command line tool for verifying md5 hash sums.

Updating to use the python moduld hashlib instead of the windows certUtil tool
for platform independence.

Warning: MD5 has been broken. Is still useful for verifiying that a file did 
not get corrupted during download.

"""

import sys
import hashlib
from tkinter import Tk
from tkinter import filedialog


def get_file(myTitle=None):   
    """ Displays Tk dialog to select a file for processing 
    
    Parameters
    ----------
    myTitle : str
        String to use for the message displayed in the title bar. 
        
    Returns
    -------
    filename : string
        The name of the file on which to compute the digest.
        
    """
    
    Tk().withdraw()                
    filename = filedialog.askopenfilename(title=myTitle)
    return filename

                    

def verify_MD5(hash_string, filename):
    """ Function to compute md5 hash sum.

    Parameters
    ----------
    myTitle : str
        String to use for the message displayed in the title bar. 
        
    Returns
    -------
    filename : string
        The name of the file on which to compute the digest.
    """
    
    h = hashlib.md5()
    with open(filename,'rb') as f:
        for block in iter(lambda: f.read(128), b""):
            h.update(block) 
    computed_hash = h.hexdigest()

    print_results(hash_string,computed_hash)
  
    
def print_results(hash_string,computed_hash):
    """Print the results of the calculation to console
    
    Parameters
    ----------
    hash_string : str
        Original hash string that was posted. 
    computed_hash : str
        Digest that was computed on the received file.          
    
    """

    print ('Original Digest: ' + hash_string)
    print ('Computed Digest: ' + computed_hash)   
    
    if hash_string == computed_hash:
        print ('SUCCESS! Message digests match')
    else:
        print('FAIL!. Message digests do not match')



if __name__ == '__main__':
    
    hash_sum = sys.argv[1]
    fname = get_file('Please choose a file to verify MD5 hash')
    verify_MD5(hash_sum, fname)
    


