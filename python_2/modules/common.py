# dir(<module_name>) -- list content "names" defined by module

import math; # import entire modure
from os import walk; # import singe "name" (function/submodule)
from os import path;
from hashlib import md5 as cryptohasher; # import name with synonym

print("Sqrt: ", math.sqrt(9));
print("Traversal:");
for _, _, files in walk("../"):
    print("\t", files);

c_hasher = cryptohasher("chunk1".encode("utf-8"));
c_hasher.update("chunk2".encode("utf-8"));
print(c_hasher.digest());
