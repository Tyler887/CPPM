from distutils.core import setup
import py2exe
self.app_title = "Cross-Platform Package Manager"
self.title = "Cross-Platform Package Manager"

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "cppm.py"}],
    zipfile = None,
)
