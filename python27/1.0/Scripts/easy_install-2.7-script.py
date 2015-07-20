#!python2.7.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==5.2','console_scripts','easy_install-2.7'
__requires__ = 'setuptools==5.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('setuptools==5.2', 'console_scripts', 'easy_install-2.7')()
    )
