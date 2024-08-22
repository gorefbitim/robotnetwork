from setuptools import setup, find_packages

setup(
    name='robotnetwork',
    version='0.1.3',
    packages=find_packages(),
    scripts=['venus/run_installer.bat'],  # Adjust path as necessary
    entry_points={
        'console_scripts': [
            'robotnetwork=src.app:main',
        ],
    },
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
        'requests',
        'configparser'
    ],
    # Metadata
    author="Ofer Rahat",
    author_email="leofer@gmail.com",
    description="A tool to relay http message from venus to slack.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gorefbitim/robotnetwork",
    classifiers=[
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: Microsoft :: Windows",
         "Operating System :: POSIX :: Linux",
    ],
)
