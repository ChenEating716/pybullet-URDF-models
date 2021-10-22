'''
Author: Yiting CHEN
Date: 2021-10-22 09:59:41
LastEditTime: 2021-10-22 10:25:42
contact me through chenyiting@whu.edu.cn
'''
import os
from setuptools import setup, find_packages

setup_py_dir = os.path.dirname(os.path.realpath(__file__))
need_files = []
datadir = "urdf_models"

hh = setup_py_dir + "/" + datadir

for root, dirs, files in os.walk(hh):
  for fn in files:
    ext = os.path.splitext(fn)[1][1:]
    if ext and ext in 'urdf sdf xml stl ini obj mtl png'.split(
    ):
      fn = root + "/" + fn
      need_files.append(fn[1 + len(hh):])


print("find_packages() \n {}".format(find_packages()))
print("find_packages() \n {}".format(find_packages('ycb_objects_models_sim')))

setup(
  name="pybullet-object-models",
  version="0.1",
  author="Elena Rampone",
  author_email="elena.rampone@iit.it",
  description="URDF-SDF models of textured YCB objects for simulation",
  license="LGPL",
  python_requires='>=3',
  keywords="urdf sdf model object simulation pybullet",
  package_dir={'': '.'},
  packages=find_packages(),
  package_data={'pybullet_object_models': need_files},
  url="https://github.com/eleramp/pybullet-object-models",
)