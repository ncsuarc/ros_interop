from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# TODO: random todo that is no longer needed

setup_args = generate_distutils_setup(
    packages=["ros_interop"],
    package_dir={"": "src"},
    install_requires=["yaml", "py3exiv2", "sortedcollections"],
)

setup(**setup_args)