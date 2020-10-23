def del_NFA(state, alphabet):
    pass#transition function of the NFA. Returns a list

Q_N=[0,1,2,3,4,5,6]#replace with the actual states of the NFA
E = [0,1]#replace with alphabets
F=[0,1] #Replace with accept states of the NFA
NFA = [Q_N, E, 0, F]


Q_D=[]  #States of the DFA
F_DFA=[] #Accepting states of the DFA
start_DFA=[0] #start state of DFA = start state of NFA
#Getting the power set of Q_N, and filling
#it in Q_D
for i in range(len(Q_N)):
    for j in range(i+1, len(Q_N)):
        # adding a subset in the form of a list.
        #Each list represents a single state
        Q_D.append([Q_N[i], Q_N[j]]) 
        

d = {} #Dictionary to store DFA's transition function

        
def construct_del_DFA(): 
#Transition Function of the DFA
    for i in Q_D:#For each state in the DFA,
                   #we figure out the transitions
       for k in E:#For each alphabet    
           to = []
           for j in i:    
                #For each DFA state corresponding to
                #multiple NFA states, find E(q)
               tos = del_NFA(j,k)
               for l in tos:
                   if(any(l in sublist for sublist in F)):
                      accepting=true
                   #Add each unique state of the NFA
                   #return value to our DFA transition
                   if(not(any(l in sublist for sublist in to) )):
                       #If this state is not already accounted for,
                       #add it
                       to.append(l)
        #Making the dictionary entry for this state and letter
       d[tuple(i, k)] = (to.sort()).copy() 
       if(accepting):
           F_DFA.append((to.sort()).copy())
        
        
def del_DFA(state, alphabet):
    t=tuple(state, alphabet)
    return d[t]

construct_del_DFA()
DFA = [Q_D, E, start_DFA, F_DFA]