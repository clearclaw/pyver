import os
from setuptools import setup, find_packages

exec open ("pyver/version.py")

setup (
    name = "pyver",
    version = __version__,
    description = "Git-based versioning for Python tools and modules.",
    long_description = file ("README.rst").read (),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        + "GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Utilities",
    ],
    keywords = "version semver git",
    author = "J C Lawrence",
    author_email = "claw@kanga.nu",
    url = "https://github.com/clearclaw/pyver",
    download_url = ("https://github.com/clearclaw/pyver/tarball/%s.%s"
                    % (__version_info__[0], __version_info__[1])),
    license = "GPL v3",
    packages = find_packages (exclude = ["tests",]),
    package_data = {
    },
    zip_safe = False,
    install_requires = [
    ],
    entry_points = {
    },
  )
