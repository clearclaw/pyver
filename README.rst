pyver
=====

Automatic/hands-free PEP 440 versioning of Python tools and modules that
use Git as a development SCM.

pyver provides a simple way to provide consistent and auditable
versioning of Python tools and packages, throughout their development
lifecycle, without any overt developer attention after initial adoption.
This includes installations from egg packages, and both direct installs
and "develop" installs using setuptools and setup.py.

Yep, accurate versioning even for ``develop`` installs.

Implementation
==============

Apply an annotated tag of the form #.# to your git repository:

::

    git tag -a 1.0 -m "Initial version"

Edit your setup.py as follows, eg for "my\_package":

::

    from setuptools import setup, find_packages
    import pyver

    __version__, __version_info__ = pyver.get_version (pkg = "my_package")

    setup (name = "my_package",
        version = __version__,
        description = "Something that does something...",
        ...etc.

By default pyver generates a *local version identifier* per PEP 440:

::

    major.minor.patch+commit_id[.dirty]

If you need a PEP 440 compliant *public version identifier* (eg for
PyPI), then set public to True in the call to get\_version():

::

    from setuptools import setup, find_packages
    import pyver

    __version__, __version_info__ = pyver.get_version (pkg = "my_package", public = True)

    setup (name = "my_package",
        version = __version__,
        description = "Something that does something...",
        ...etc.

And that will produce *public version identifiers*:

::

    major.minor.patch[.dev1]

Unfortunately the git commit fingerprint can't be expressed in the
patch-level for public versions per PEP 440, and so that has to be
dropped. See PEP 440 for details:
http://legacy.python.org/dev/peps/pep-0440/

Next, add the following two lines to the **init**.py at the root of your
package:

::

    import pyver
    __version__, __version_info__ = pyver.get_version (pkg = __name__)

And that's it. Done!

Usage
=====

Now when you install your package it will be versioning using the tag
for the major and minor number, and the number of commits since the tag
for the patch (plus the fingerprint and dirty state of the last commit
for the patch level if using the default *local version identifiers*).
And, if you installed from a tree with uncommitted changes, or perhaps
are using a "develop" install with uncommitted changes, then the
patchlevel will have a "-dirty" suffix.

Of course pyver is versioned with pyver:

::

    $ python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyver
    >>> pyver.__version__
    '0.1.1+gc80d6f1'
    >>> pyver.__version_info__
    ('0', '1', '1+gc80d6f1')

But if I touch a file in the repository (such as this README I'm editing
now), then the version will change:

::

    $ python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyver
    >>> pyver.__version__
    '0.1.3+gc1a0f15.dirty'
    >>> pyver.__version_info__
    ('0', '1', '3+gc1a0f15', 'dirty')

Likewise for PEP 440 public versions if public is passed as true (as it
is now for pyver (a recent change)):

::

    $ python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyver
    >>> pyver.__version__
    '0.1.1'
    >>> pyver.__version_info__
    ('0', '1', '1')

and while we can't capture the git commit fingerprint in a public
version per PEP 440, the dirty state is still caught as "dev1" in a
dirty repository:

::

    $ python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyver
    >>> pyver.__version__
    '0.1.3.dev1'
    >>> pyver.__version_info__
    ('0', '1', '3', 'dev1')

Managing versions
=================

The intent and expectation is that the major and minor version values
will be managed by the business (generally Product). As such the minor
and major version numbers are managed by the annotated tag.

The patchlevel however is the developer's world. The developer does work
and the patchlevel automagically moves forward in a clear and
documentary way that can be audited and traced back to a single unique
point in the Git tree without the developer doing anything.

And that's the key: the default is hands-free and provably correct and
auditable, and the rare/special business case is the only change that
requires explicit action.
