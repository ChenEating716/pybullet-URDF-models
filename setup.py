import os
from setuptools import setup, find_packages

setup_py_dir = os.path.dirname(os.path.realpath(__file__))
need_files = []
datadir = "urdf_models"

hh = setup_py_dir + "/" + datadir

for root, dirs, files in os.walk(hh):
  for fn in files:
    ext = os.path.splitext(fn)[1][1:]
    if ext and ext in 'urdf obj mtl jpg'.split(
    ):
      fn = root + "/" + fn
      need_files.append(fn[1 + len(hh):])


print("find_packages() \n {}".format(find_packages()))
print("find_packages() \n {}".format(find_packages('urdf_models')))

setup(
  name="urdf_models",
  version="0.1",
  author="Yiting CHEN",
  author_email="chenyiting716@gmail.com",
  description="A simple python module for convenient URDF model loading",
  license="MIT",
  python_requires='>=3',
  keywords="pybullet urdf models",
  package_dir={'': '.'},
  packages=find_packages(),
  package_data={'urdf_models': need_files},
  url="https://github.com/ChenEating716/pybullet-URDF-models",
)
