def decoder(bitstream,tree):
    '''
        Let's reverse tree and make easier access to chars
        For each codeword recognized, get its char in tree
        and concatenate to text
    '''
    if not isinstance(bitstream,str):
        raise ValueError('Bitstream must be a string')
    if not isinstance(tree,dict):
        raise ValueError('Tree must be a dict')
    tree = dict((value,key) for key,value in tree.items())
    text = ''
    codeword = ''
    for bit in bitstream:
        codeword += bit
        if codeword in tree.keys():
            text += tree[codeword]
            codeword = ''
    return text
