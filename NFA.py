#demo
nfa={'q0':{'0':['q1'], 'lamda':['q1']},
     'q1':{'0':['q0', 'q2'], '1':['q1','q2']},
     'q2':{'0':['q2'], '1':['q1']}}

list_vertices = []

def accept(nfa, start, ends, str):
  k = 0
  for states in nfa:
    if ('lamda' in nfa[states]):
      k = k + len(nfa[states]['lamda'])
      
  max_length = k + (1 + k)*len(str)
  return acceptNFA(nfa, 'q0', ['q1'], str, 0, 0, max_length)

def acceptNFA(nfa, start, ends, str, i, edges, max_length):
  if (edges > max_length and str != ''):
    return False
  if (i >= len(str)):
    if (start in ends):
      list_vertices.append(start)
      return True
    if lamdaNFA(nfa, start, ends, str, i, edges+1, max_length):
      return True
    return False
  if (str[i] in nfa[start]):
    nextStates=nfa[start][str[i]]
  elif lamdaNFA(nfa, start, ends, str, i, edges, max_length):
    return True
  else:
    return False
  for curr in nextStates:
    if acceptNFA(nfa, curr, ends, str, i+1, edges+1, max_length):
      list_vertices.append(start)
      return True
  if lamdaNFA(nfa, start, ends, str, i, edges, max_length):
    list_vertices.append(start)
    return True
  return False
  
  
def lamdaNFA(nfa, start, ends, str, i, edges, max_length):
  if ('lamda' in nfa[start]):
    for curr in nfa[start]['lamda']:
      if acceptNFA(nfa, curr, ends, str, i, edges+1, max_length):
        list_vertices.append(start)
        return True
  return False
      
      
      
if accept(nfa,'q0',['q1'],'10111'):
  print('Accepted, the traverse order is:')
  print(list(reversed(list_vertices)))
else:
  print('Rejected')