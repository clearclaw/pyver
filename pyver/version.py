#! /usr/bin/env python

from pyver.metaversion import get_version

__all__ = ("__version__", "__version_info__")
__version__, __version_info__ = get_version (pkg = "pyver",
                                             public = True) # PyPI
