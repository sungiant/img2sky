import os
import subprocess

script_dir = os.path.dirname (os.path.realpath (__file__))
build_dir = os.path.join (script_dir, 'build')
projects_dir = os.path.join (script_dir, 'projects')

if not os.path.isdir (projects_dir):
    os.mkdir (projects_dir)

if os.name == 'nt':
    subprocess.call (['cmake', '-G', 'Visual Studio 16 2019', build_dir], cwd = projects_dir)
elif os.name == 'posix':
    subprocess.call (['cmake', '-G', 'Xcode', build_dir], cwd = projects_dir)
else:
    raise NotImplementedError
