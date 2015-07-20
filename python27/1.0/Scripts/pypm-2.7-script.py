#!python2.7.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pypm==1.4.3','console_scripts','pypm-2.7'
__requires__ = 'pypm==1.4.3'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pypm==1.4.3', 'console_scripts', 'pypm-2.7')()
    )
