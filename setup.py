from setuptools import setup, find_packages

__version__ = "unknown"

exec open ("pyver/version.py")

setup (
    name = "pyver",
    version = __version__,
    description = "Git-based versioning for Python tools and modules.",
    long_description = file ("README.md").read (),
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
    license = "GPL v3",
    packages = find_packages (exclude = ["tests",]),
    package_data = {
    },
    zip_safe = True,
    install_requires = [
    ],
    entry_points = {
    },
  )
