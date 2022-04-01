from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    setup(name='kolibridata',
        version='0.1',
        packages=find_packages(),
        author='Aneruth',
        author_email='ane1998@gmail.com',
        url='https://github.com/Aneruth/kolibri-data',
        package_data={'kolibridata': ['config/*.tmpl']},
    )