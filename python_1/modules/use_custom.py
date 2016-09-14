from sys import path as module_pathes
import os

print("Default module search pathes: ")
for path in module_pathes:
    print("\t", path)

try:
    import my_math
except ImportError:
    print('Python: What the hell did you try to import? I don\'t know "my_math"!')

# import custom.my_math # this works

print("Module path patching...")
# alter pathes to be able to load custom module
import math
custom_module_path = os.path.join(os.getcwd(), "custom")
# os.path.abspath(os.path.dirname(__file__))
module_pathes.insert(0, custom_module_path)

import my_math
print("Python: D'oh, now I see my_math...")

print(" 9 / 5 to upper =", my_math.div_ceil(9, 5))

from my_math import sqrt
from math import sqrt

print("(my_math, math) Sqrt: ", sqrt(9))

from my_math import sqrt

print("(my_math, math, my_math) Sqrt: ", sqrt(9))

from my_math import gcd

print("gcd(21, 14) == ", gcd(21, 14))

# As your can see -- last import "wins" in case of name clashing.
# NB: if you try to rename my_math module to math to completely full python
#     if wouldn't work, since looks like math is one of buildins modules
