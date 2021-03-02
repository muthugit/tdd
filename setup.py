from setuptools import setup, find_packages
__version__ = "0.0.1"

# global build_version
# build_version = '111'

setup(
    name="tdd",
    version=__version__,  # Upgrades, Updates, Fixes
    author="Muthupandian",
    author_email="contact@muthupandian.in",
    description="TDD",
    packages=["tdd"],
    include_package_data=True,
    url="",
    install_requires=[
        "pandas",
        "requests"
    ],
    classifiers=[
                    "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent",
                ],
    python_requires='>=3.6',
)
