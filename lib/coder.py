class Coder:

    alphabet = {}

    def __init__(self, text):
        self.text = text
        for char in self.text[:]:
            if char not in self.alphabet:
                self.alphabet[char] = 1
            else:
                self.alphabet[char] += 1
    
    def getprobabilities(self):
        Nchars = len(self.text)
        result = {}
        for char,times in self.alphabet.items():
            result[char] = times/Nchars
        return sorted(result.items(), key=lambda item: item[1], reverse=True)
    
    def binarytree(self):
        probs = self.getprobabilities()
        codeword_0 = '0'
        codeword_1 = '1'
        counter = 0
        result = {}
        for char,prob in probs:
            if counter % 2 == 0:
                result[char] = codeword_0 + '1'
                codeword_0 += '0'
            else:
                result[char] = codeword_1 + '0'
                codeword_1 += '1'
            counter += 1
        return result
    
    def HuffmanTree(self):
        probs = self.getprobabilities()
        codeword = '1'
        result = {}
        counter = 0
        for char,prob in probs:
            if counter == 0:
                result[char] = '0'
            elif counter < len(self.text) - 1:
                result[char] = codeword + '0'
                codeword += '1'
            else:
                result[char] = codeword[:-2] + '1'
            counter += 1
        return result
    
    def bitstream(self,tree=None):
        if tree is None:
            tree = self.binarytree()
        bitstream = ''
        for char in self.text:
            bitstream += tree[char]
        Bytes = len(bitstream) / 8
        return bitstream,tree,Bytes
