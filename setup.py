import setuptools
import os
import shutil


def rm(path: str):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

if __name__ == '__main__':
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="xoa-driver",
        version="1.0b3",
        description="Xena OpenAutomation high-level and low-level Python APIs and code examples for Xena TGA testers.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Artem Constantinov, Ron Ding, Leonard Yu",
        author_email="aco@xenanetworks.com, rdi@xenanetworks.com, hyu@xenanetworks.com",
        maintainer="Xena Networks",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenadevel/xena-open-automation-python-api",
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
