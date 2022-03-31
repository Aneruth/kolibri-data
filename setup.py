from ensurepip import version
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="kolibriData",
    version = 0.1,
    author="Aneruth",
    author_email="ane1998@gmail.com",
    include_package_data=True,
    description="Config package for kolibri",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    url="",
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.json', '*.npy', '*.db'],
    },
    packages=setuptools.find_packages(exclude=['data', '*.data', '*.data.*']),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta',
    ],
    python_requires='>=3.7',
)