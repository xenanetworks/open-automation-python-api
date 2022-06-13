import setuptools

def main():
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="xoa-driver",
        description="Xena OpenAutomation (XOA) Python API is a driver providing user-friendly communication interfaces to Xena's physical and virtual Traffic Generation and Analysis (TGA) testers. It provides a rich collection of programming interfaces that can be used to either write test scripts or develop applications.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Artem Constantinov, Ron Ding, Leonard Yu",
        author_email="aco@xenanetworks.com, rdi@xenanetworks.com, hyu@xenanetworks.com",
        maintainer="Xena Networks",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenanetworks/open-automation-python-api",
        packages=setuptools.find_packages(),
        license='Apache 2.0',
        install_requires = ["loguru"],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
        python_requires=">=3.8",
    )

if __name__ == '__main__':
    main()