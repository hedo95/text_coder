# -*- coding: utf-8 -*-
import sys
import os
from lib.coder import *
from lib.decoder import *


'''

    There are so many ways to encode a text, here we'll see 2 of them
    Suggested alternatives could be: arithmetic coding, LZ 77, LZ 78, LZW...

    Main program 
'''

Text = str(input('Enter a text to code:\n'))

print(Text)

encoded1_text,size1,tree1 = coder(Text,treetype='complete')
encoded2_text,size2,tree2 = coder(Text,treetype='full')

print('\nBitstream complete tree: \n\n'+encoded1_text)
print('\nBytes: '+str(size1))

print('\nBitstream full tree: \n\n'+encoded2_text)
print('\nBytes: '+str(size2))

'''
    Now let's decode the text and check if decoder works as well as coder
'''

decoded1_text = decoder(encoded1_text,tree1)
print('\nDecoded text1 with decoder: \n'+ decoded1_text)

decoded2_text = decoder(encoded2_text,tree2)
print('\nDecoded text2 with decoder: \n'+ decoded2_text)
