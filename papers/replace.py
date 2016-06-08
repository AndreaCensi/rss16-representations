#!/usr/bin/env python
import os
for filename in os.listdir("."):
  if filename.startswith("Beyond"):
    new_filename = filename.replace("\\", "_")
    os.rename(filename, new_filename)
