#! /usr/bin/env python

import pkg_resources

def main ():
  f = pkg_resources.resource_string ("pyver", "version.py")
  with open ("version.py", "w") as w:
    w.write (f)

if __name__ == "__main__":
  main ()
