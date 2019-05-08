def constructR0(dfa):

    global R
    numState = len(dfa)

    #3d-array, 0 init
    R = [[['0' for i in range(numState+1)] for j in range(numState+1)] for a in range(numState+1)]

    for i in dfa:
        for j in dfa[i]:
            k = dfa[i][j]
            if(R[i][k][0] == '0'):
                R[i][k][0] = j
            else:
                R[i][k][0] = R[i][k][0] + ' + ' + j
    #print(R)

def convert(i, j, k, dfa):
    #global variable
    global R
    
    #base case
    if(k == 0):
        #for good format
        if(len(R[i][j][0]) != 1):
            return '(' + R[i][j][0] + ')'
        else:
            return R[i][j][0]
    
    #memoization for faster
    if (R[i][j][k] != '0'):
      return R[i][j][k]
    
    R_ijk_1 = convert(i, j, k-1, dfa) #R_ijk_1
    R_ikk_1 = convert(i, k, k-1, dfa) #R_ikk_1
    R_kkk_1 = convert(k, k, k-1, dfa) #R_kkk_1
    R_kjk_1 = convert(k, j, k-1, dfa) #R_kjk_1

    if (R_ikk_1 == '0' or R_kjk_1 == '0'):
        return R_ijk_1
    
    R[i][j][k] = '(' + R_ijk_1 + ' + ' + R_ikk_1 + '(' + R_kkk_1 + ')*' + R_kjk_1 + ')'

    return R[i][j][k]

  
def convertNFA_RE(start, final, dfa):
    numState=len(dfa)
    #init_R(dfa)
    constructR0(dfa)
    Regex = ''
    j = len(final)
    for i in range(j):
        Regex += (convert(start, final[i], numState, dfa))
        if(i != j - 1):
            Regex += ' + '
    print(Regex)
    
#example input
bai_10 = {1: {'a': 2, 'b': 3,},
          2: {'a': 3, 'b': 2},
          3: {'a': 2, 'b': 3, 'c': 4},
          4: {}}

#demo
convertNFA_RE(1, [2], bai_10)

#formula: Automata Theory course, Jeff Ullman