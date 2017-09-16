#!C:\Users\trish\PycharmProjects\Acadview\mmu3rd\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ParallelDots==1.0.7','console_scripts','paralleldots'
__requires__ = 'ParallelDots==1.0.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ParallelDots==1.0.7', 'console_scripts', 'paralleldots')()
    )
