import numpy as np

def getalphabet(text):
    '''
        Function that count how many times appears
        every char in text
    '''
    result = {}
    for char in text[:]:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result

def getprobabilities(alphabet):
    '''
        Let's calculate the occurrence probability for each char
        in alphabet
    '''
    if not isinstance(alphabet,dict):
        raise ValueError("Alphabet must be a dictionary")
    size = len(alphabet.items())
    for char,times in alphabet.items():
        alphabet[char] = times/size
    # return a dictionary, ordered by probabilities in desc order
    return {char:prob for char,prob in sorted(alphabet.items(), key=lambda item: item[1], reverse=True)}

def completetree(probabilities):
    '''
        Let's set a codeword for each char in alphabet
        The idea of codeword assignment is codeword length must be
        inversely proportional to its occurrence probability
        to bitstream to have minimum size

        The complete tree is a binary tree type
    '''
    if not isinstance(probabilities,dict):
        raise ValueError("Probabilities must be a dictionary")
    codeword_0 = '0'
    codeword_1 = '1'
    counter = 0
    result = {}
    for char,prob in probabilities.items():
        if counter % 2 == 0:
            result[char] = codeword_0 + '1'
            codeword_0 += '0'
        else:
            result[char] = codeword_1 + '0'
            codeword_1 += '1'
        counter += 1
    return result


def fulltree(probabilities):
    ''' 
        Same goal as getcompletetree() 
    '''
    if not isinstance(probabilities,dict):
        raise ValueError("Probabilities must be a dictionary")
    codeword = '1'
    result = {}
    counter = 0
    for char,prob in probabilities.items():
        if counter == 0:
            result[char] = '0'
        elif counter < (len(probabilities.items()) - 1):
            result[char] = codeword + '1'
            codeword += '0'
        else:
            result[char] = codeword[:-2] + '1'
        counter += 1
    return result

def generateBitstream(text,tree):
    '''
        Let's create the bitstream from original text
        through the binary tree 
        And calculate its size
    '''
    if not isinstance(tree,dict):
        raise ValueError("Tree must be a dictionary")
    bitstream = ''
    for char in text[:]:
        bitstream += tree[char]
    # Round result up
    Bytes = np.ceil(len(bitstream) / 8)
    return bitstream,int(Bytes)



def coder(text,treetype='complete'):
    '''
        Function that encodes the text
    '''
    treetypes = ['full','complete']
    if not isinstance(text,str):
        raise ValueError('Text must be a string')
    if treetype not in treetypes:
        raise ValueError('Must select a tree type')
    
    alphabet = getalphabet(text)
    probabilities = getprobabilities(alphabet)
    if treetype == 'full':
        tree = fulltree(probabilities)
    else:
        tree = completetree(probabilities)
    bitstream,Bytes = generateBitstream(text,tree)
    return bitstream,Bytes,tree
