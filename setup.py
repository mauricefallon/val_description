from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
import subprocess
from datetime import datetime
import getpass
import socket

d = generate_distutils_setup(
    packages=['val_description'],
    package_dir={'': 'src'}
)

user = getpass.getuser()
machine = socket.gethostname()
branch = subprocess.check_output('git rev-parse --abbrev-ref HEAD'.split()).strip()
gitsha = subprocess.check_output('git rev-parse HEAD'.split()).strip()
revision = len(subprocess.check_output('git rev-list remotes/origin/master..'.split()).strip().splitlines())
timestamp = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')

build_info = '{}@{} - {}:{}'.format(user, machine, branch, gitsha)
source_url = subprocess.check_output('git config --get remote.origin.url'.split()).strip()
version = '{}.{}-{}-{}'.format(d['version'], revision, timestamp, gitsha[:8])

long_description = """{}
  This package contains a python implementation of val_description.
  Build_Info: {}.
  Source_Url: {}.
  Complete_Version: {}
""".format(d['description'], build_info, source_url, version)

d['long_description'] = long_description

setup(**d)
