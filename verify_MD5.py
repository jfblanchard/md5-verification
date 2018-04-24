# -*- coding: utf-8 -*-
"""
Functions for performing a MD5 hash sum verification.

#Calls the windows program certUtil.
Updating to use the python moduld hashlib for platform independence.
Todo:  Support more hashes besides md5
make a drop down menu of hash types

Warn the user that MD5 has been broken.

"""

import sys
import hashlib
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

                    

def verify_MD5(hash_string, filename):
    """ Function to compute hash sums.
    
    """
    
    hashes = hashlib.algorithms_available
    
    #h = hashlib.new('md5')
    h = hashlib.new('sha256')
    
    with open(filename,'rb') as f:
        for block in iter(lambda: f.read(128), b""):
            h.update(block)
        
    computed_sum = h.hexdigest()

    print ('MD5 Hash Sum: ' + hash_string)
    print ('Computed: ' + computed_sum)
    
    print_results(hash_string,computed_sum)
    
def print_results(hash_string,computed_sum):
    """Print the results of the calculation
    """
    
    if hash_string == computed_sum:
        print ('SUCCESS! Sums match')
    else:
        print('FAIL!. Sums do not match')


def test_hash_sum():
    """Test function currently using the one from the python docs."""
    
    test_string = 'Nobody knows the trouble Ive seen'

    m = hashlib.new('md5')
    m.update(test_string.encode('utf-8'))
    computed = m.hexdigest()
    
    answer = '2e7bb7e7d27b8cda5492e24345dd1c69'
    kali = 'ed88466834ceeba65f426235ec191fb3580f71d50364ac5131daec1bf976b317'
    print_results(computed,answer)
    

if __name__ == '__main__':
    
    hash_sum = sys.argv[1]
    fname = get_file('Please choose a file for checksum')
    verify_MD5(hash_sum, fname)
    


