from setuptools import setup, find_packages

setup(
    name="shalev-polyrize",
    version="1",
    author="shalev",
    author_email="svkh98@gmail.com",
    description="Shalev's Polyrize",
    url="https://github.com/hoshot21/shalev-polyrize",
    packages=find_packages(),
    install_requires=['sanic', 'sanic_jwt', 'requests'],
    python_requires='>=3.8',
)
