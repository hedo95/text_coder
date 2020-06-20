import sys
from lib.coder import *
from lib.decoder import *


text = """ 
Packages are a way of structuring Python’s module namespace by using “dotted module names”. 
For example, the module name A.B designates a submodule named B in a package named A. 
Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, 
the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.
Suppose you want to design a collection of modules (a “package”) for the uniform handling of sound files and sound data. 
There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au) 
so you may need to create and maintain a growing collection of modules for the conversion between the various file formats. 
There are also many different operations you might want to perform on sound data (such as mixing, adding echo, 
applying an equalizer function, creating an artificial stereo effect),
so in addition you will be writing a never-ending stream of modules to perform these operations. 
"""

coder = Coder(text)
tree = coder.HuffmanTree()
bitstream,tree,Bytes = coder.bitstream(tree=tree)
print('\n'+bitstream)
print('\nBytes: '+str(Bytes))

decoder = Decoder(bitstream,tree)
print('\nDecoded text: '+ decoder.text())
