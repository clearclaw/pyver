pyver
=====

Automatic/hands-free versioning of Python tools and modules that use
Git as a development SCM.

pyver provides a simple way to provide consistent and auditable
versioning of Python tools and packages, throughout their development
lifecycle, without any overt developer attention after initial
adoption.  This includes installations from egg packages, and both
installs and "develop" using setuptools and setup.py.

Yep, accurate versioning even for `develop` installs.

Implementation
==============

Apply an annotated tag of the form #.# to your git repository:

    git tag -a 1.0 -m "Initial version"

Edit your setup.py as follows, eg for "my_package":

```
from setuptools import setup, find_packages
import pyver

__version__, __version_info__ = pyver.get_version (pkg = "my_package")

setup (name = "my_package",
    version = __version__,
    description = "Something that does something...",
    ...etc.
```

Done!

Usage
=====

Now when you install your package it will be versioning using the tag
for the major and minor number, and the number of commits since the
tag plus the fingerprint of the last commit for the patch level.  And,
if you installed from a tree with uncommitted changes, or perhaps are
using a "develop" install, the patchlevel will have a "-dirty" suffix.

Of course pyver is versioned with pyver:

```
$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyver
>>> pyver.__version__
'0.1.1-gc80d6f1'
>>> pyver.__version_info__
('0', '1', '1-gc80d6f1')
```

But if I touch a file in the repository (such as this README I'm
editing), then the version will change:

```
$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyver
>>> pyver.__version__
'0.1.3-gc1a0f15-dirty'
>>> pyver.__version_info__
('0', '1', '3-gc1a0f15-dirty')
```

Managing versions
=================

The intent and expectation is that the major and minor version values
will be managed by the business (generally Product Marketing).  As
such the minor and major version numbers are managed by the annotated
tag.  

The patchlevel however is the developer's world.  The developer does
work and the patchlevel automagically moves forward in a clear and
documentary way that can be audited and traced back to a single unique
point in the Git tree without the developer doing anything.  

And that's the key: the default is hands-free and provably correct and
auditable, and the rare/special business case is the only change that
requires explicit action.
