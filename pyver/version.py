#! /usr/bin/env python

"""
Uses `git describe` to dynamically generate a version for the
current code.  The version is effecvtively a traditional tri-tuple
ala (major, minor, patch), with the addenda that in this case the
patch string is a combination of the number of commits since the
tag, plus the ID of the last commit.  Further, the patch will be
extended with "-dirty" if there are uncommitted changes in the
current codeset.

  eg 1.0.1-gd5aa65e-dirty

Assumes that the tags fit the regex [0-9]*.[0-9]*
"""

import contextlib, logging, os, pkg_resources, subprocess

LOG = logging.getLogger (__name__)
DEFAULT_GITCMD = "git describe --long --tags --match [0-9]*.[0-9]* --dirty"

class VersionError (Exception):
  pass

@contextlib.contextmanager
def chdir (dname):
  cwd = os.getcwd ()
  try:
    if dname is not None:
      os.chdir (dname)
    yield dname
  finally:
    os.chdir (cwd)

def get_version (pkg = __name__, public = False):
  s = None
  try:
    mod = __import__ (pkg)
    path = os.path.dirname (mod.__file__) or "./"
    with chdir (path) as cwd: # pylint: disable=W0612
      o = subprocess.check_output (
        DEFAULT_GITCMD.split (),
        stderr = subprocess.PIPE,
        shell = False).decode ().strip ()
      s = o.replace ("-", ".", 1).replace ("-", "+", 1).replace ("-", ".", 1)
  except OSError:
    try:
      s = pkg_resources.get_distribution (pkg.split (".")[0]).version
    except Exception as e:
      m = "Problem getting pkg resources: %s" % e
      LOG.error (m)
      raise VersionError (m)
  finally:
    if s is None:
      m = "Failed to determine installed version."
      LOG.error (m)
      raise VersionError (m)
  if public:
    vals = s.split (".")
    patch = ((vals[2][:vals[2].find ("+")])
             if vals[2].find ("+") != -1 else vals[2])
    info = ((vals[0], vals[1], patch, "dev1")
            if len (vals) == 4 else (vals[0], vals[1], patch))
    return ".".join (info), info
  else:
    return s, s.split (".")

__version__, __version_info__ = get_version (pkg = "pyver",
                                             public = True) # PyPI
