#!/usr/bin/env python3



from contextlib import suppress


password = "olivier"
AWS_SECRET = "AZEEZSDQRZ"

with suppress(ValueError):
  raise ValueError("You knew this would happen")
  
print("but here we are")