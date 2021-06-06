from os.path import dirname, basename, isfile, join
import glob
import pdb;pdb.set_trace()
# import dependencies


py_modules = glob.glob(join(dirname(__file__), "*.py"))
modules = [ basename(f)[:-3] for f in py_modules if isfile(f) and f.endswith('_prerequisite.py')]

PROJECT_APPS = []
for project in modules:
    module = __import__("dependencies."+project)
    obj = getattr(module, project)
    PROJECT_APPS.extend(obj.INSTALLED_APPS)


