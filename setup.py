'''
Author: Yiting CHEN
Date: 2021-10-22 09:59:41
LastEditTime: 2021-10-22 10:25:42
contact me through chenyiting@whu.edu.cn
'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urdf_models",
    version="0.0.1",
    author="Yiting CHEN",
    author_email="chenyiting716@gmail.com",
    description="A simple python module for loading URDF models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChenEating716/pybullet-URDF-models",
    project_urls={
        "Bug Tracker": "https://github.com/ChenEating716/pybullet-URDF-models/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Ubuntu",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
