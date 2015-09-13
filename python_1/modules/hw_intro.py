# dir(<module_name>) -- list content "names" defined by module

import math; # import entire modure
from os import walk; # import singe "name" (function/submodule)
from os import path;
from hashlib import md5 as cryptohasher; # import name with synonym

print("Sqrt: ", math.sqrt(9));
print("Traversal:");
for _, _, files in walk("../"):
    print("\t", files);

hasher = cryptohasher();
hasher.update(b"chunk1");
hasher.update(b"chunk2");
hasher.update("chunk3".encode('utf-8'));
print(hasher.hexdigest());
