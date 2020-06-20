class Decoder:

    def __init__(self, bitstream, tree):
        self.bitstream = bitstream
        self.tree = dict((value,key) for key,value in tree.items())
    
    def text(self):
        codeword = ''
        text = ''
        for bit in self.bitstream:
            codeword += bit
            if codeword in self.tree.keys():
                text += self.tree[codeword]
                codeword = ''
        return text
