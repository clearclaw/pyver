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

import importlib, inspect, os, pkg_resources, subprocess

DEFAULT_GITCMD = "git describe --long --tags --match [0-9]*.[0-9]* --dirty"

def get_version (pkg = __name__):
  try:
    cwd = os.getcwd ()
    try:
      mod = __import__ (pkg)
      path = os.path.dirname (mod.__file__)
      os.chdir (path)
    except ImportError as e:
      cwd = os.getcwd ()
    o = subprocess.check_output (
      DEFAULT_GITCMD.split (),
      stderr = subprocess.PIPE,
      shell = False).decode ().strip ()
    s = o.replace ("-", ".", 1)
    os.chdir (cwd)
  except: # pylint: disable-msg=W0702
    s = pkg_resources.get_distribution (pkg.split (".")[0]).version
  return s, tuple (s.split ("."))
