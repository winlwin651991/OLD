
from platform import uname
from os import system as xd
xd('git pull')
bit=uname().machine.lower()
if 'aarch' in bit:
    import OLD
    OLD.menu()
else:
    exit(' 32bit Device not Supported ')
