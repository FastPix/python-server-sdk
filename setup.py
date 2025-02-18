from setuptools import setup, find_packages

setup(
    name="fastpix",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        'async': [
            'aiohttp>=3.8.0',
        ]
    },
    description="FastPix SDK with both sync and async support",
    author="Subbaraju Chekuri",
    author_email="subbaraju.c@fastpix.io",
    url="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)
