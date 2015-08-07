#! /usr/bin/env python

try:
  import pyver # pylint: disable=W0611
except ImportError:
  import pip
  pip.main (['install', 'pyver'])
  import pyver # pylint: disable=W0611
