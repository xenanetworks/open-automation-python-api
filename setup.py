import setuptools
import os
import shutil


def rm(path: str):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

if __name__ == '__main__':
    setuptools.setup(
        name="xoa-driver",
        version="1.0b1",
        description="Xena Open Automation pydriver is a python wrapper of binary xmp (Xena Management Protocol) which enables users to call xmp in an easy way.",
        author="Artem Constantinov, Ron Ding, Leonard Yu",
        author_email="aco@xenanetworks.com, rdi@xenanetworks.com, hyu@xenanetworks.com",
        maintainer="Xena Networks",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenadevel/valhalla-bifrost/",
        packages=setuptools.find_packages(),
        license='Apache 2.0',
        install_requires = ["loguru"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
        python_requires=">=3.8",
    )
    # rm("./build")
    # rm("./dist")
    # rm("./valhalla_bifrost.egg-info")
