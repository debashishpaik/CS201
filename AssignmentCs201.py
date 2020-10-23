class NFA:

    def __init__(self):
        self.Q = []  # list of finite states in the NFA
        self.Sigma = []  # alphabet set in the NFA Sigma
        self.q_0 = ''  # initial state of NFA
        self.F = []  # accepting states of NFA
        self.M = [[0 for i in range(len(self.Sigma))]
                  for j in range(len(self.Q))]
        self.q0 = []  # initial state of the required DFA 
        self.F_DFA = []  # accepting states of the DFA
        # list for storing the alphabets(symbols) except epsilon
        self.A1 = []

    def states(self):  # function for storing the states of the NFA
        n = int(input("Provide the number of states in your Non deterministic Finite Automaton : "))

        print("Give inputs i.e. the states in the form of a character ")
        print("give the initial state in the 1st input")
        for i in range(0, n):
            x = input("Give the "+str(i+1)+"th state : ")
            self.Q.append(x)

        # displaying the list of display the states of the NFA given a input by the user
        print(self.Q)

    def alpahabet(self):  # function for storing the alphabets(symbols) of the NFA
        n1 = int(input("Provide the number of elements in the alphabet set : "))

        print("Give inputs i.e. the alphabets in the form of a character or a single digit")
        for i in range(0, n1):

            if i == 0:
                x = input(
                    "Give the symbol for epsilon, i.e, the 1st alphabet : ")
                self.Sigma.append(x)

            else:
                x = input("Give the " + str(i + 1) + " th alphabet : ")
                self.Sigma.append(x)
                if i > 0:
                    self.A1.append(x)

        print(" list of display the symbols except the epsilon are : ")
        # displaying the alphabet list without the symbol for epsilon
        print(self.A1)
        print(" list of display the alphabets of the NFA: ")

        # displaying the alphabet list of the NFA taken as input by the user
        print(self.Sigma)

    def accepting_state_NFA(self):  # accepting the final states
        n2 = int(input("Give the number of accepting states in your NFA "))
        for i1 in range(0, n2):
            # storing the accepting states in the list 'F'
            self.F.append(input("give the "+str(i1+1) +
                                " accepting state of the NFA : "))
        print("The accepting states of the NFA are : ")
        print(self.F)

    def ini_state(self):
        self.q_0 = self.Q[0]  # storing the initial state of the NFA

    def matrix_store(self, i, j):  # method for defining the delta function of the NFA

        n = int(input(" give the number of states at which " + str(self.Q[i]) + " can transit after getting the symbol " + str(self.Sigma[j])+" : "))
        list = []

        for t in range(0, n):
            # appending display the states to which Q[i] can transit after getting the symbol Sigma[j]
            list.append(input("give the " + str(t+1) + " th state : "))

        # delta( Q[i] , Sigma[j] ) = list
        self.M[i][j] = list

    def transition_func_value_storing(self):
        # matrix for storing the corresponding set of states at which a certain state of the NFA will transit after getting a particular symbol contained in the alphabet set
        self.M = [[0 for i in range(len(self.Sigma))]
                  for j in range(len(self.Q))]
        for i in range(0, len(self.Q)):
            for j in range(0, len(self.Sigma)):
                # calling the method 'matrix_strore' in order to take inputs from the user
                self.matrix_store(i, j)

    def display(self):
        for i in range(0, len(self.Q)):
            for j in range(0, len(self.Sigma)):
                print(" The state " + str(self.Q[i])+" will transit to "+str(
                    self.M[i][j])+" states after being acted upon by the symbol  " + str(self.Sigma[j]))

        # print(self.M)          # displaying the matrix

    def dFA_ini_state(self):
        # getting the initial state of the NFA
        self.ini_state()
        store_lst = list(set(self.M[0][0]) | set(self.q_0))
        # evaluating the initial state of the desired DFA, i.e, the epsilon closure of the initial state of the NFA, which is q_0
        self.q0 = self.initial_state_DFA(store_lst)
        self.q0 = list(self.q0)
        print(" The initial state of the desired DFA is : ")
        # displaying the epsilon closure of the initial state of the NFA
        print(self.q0)

    def initial_state_DFA(self, store_lt):

        store_lst1 = store_lt
        for t in range(0, len(store_lst1)):
            store_lt = list(set(store_lt) | set(
                self.M[self.Q.index(store_lst1[t])][0]))

        # base case>>> no new states are added to the store_lst1 by applying the epsilon transition on every elements of the previous store_lst1
        if sorted(store_lt) == sorted(store_lst1):

            return store_lt
        else:  # recursive case

            store_lst1 = store_lt

            return self.initial_state_DFA(store_lst1)

    def delta_modified(self, lst, x):
        list1 = []
        for i in range(0, len(lst)):
            # union of display the set of states to which the elements in the list 'lst' transited after being acted upon by x
            list1 = list(set(self.M[self.Q.index(lst[i])]
                             [self.Sigma.index(x)]) | set(list1))

        #print(" the union of display the states to which " + str(lst)+ " transited after getting the symbol "+ str(x)+ " is :")
        # print(list1)
        return list1

    # method for evaluating the union of epsilon closures of display the elements in the list returned by the method 'delts_modified'
    def closure_delta_modified(self, l, y):
        lst1 = self.delta_modified(l, y)
        str_lst = []

        if lst1 != []:  # if lst1 is not empty
            for i in range(0, len(lst1)):
                ind = self.Q.index(lst1[i])
                str_lst = list(set(str_lst) | set(self.initial_state_DFA(list(set(self.M[ind][0]) | set(
                    [lst1[i]])))))  # union of the epsilon closure of display the states in the list 'l'
        #print("union of the closure of display the states present in "+ str(str_lst) + " is : ")
        # print(str_lst)
        return str_lst

    def dfa_states_store(self, i=0, lt=[], M_str=[]):

        # here A1 is the alphabet set consisting of display the alphabets except epsilon
        M_str.append([self.closure_delta_modified(lt[i], x) for x in self.A1])
        length = len(lt)
        for x in M_str[i]:
            if x != []:

                ctr = 0
                for j in range(0, len(lt)):
                    if sorted(x) == sorted(lt[j]):

                        ctr = ctr+1
                if ctr == 0:  # checking whether this state is already present in lst or not

                    # if this is a new state, then append it to lst
                    lt.append(x)
        length1 = len(lt)

        # if no new state is added to lst and no element in lst is left to be processed
        if length1 == length and i+1 == length1:
            # lst is the list of display states in the required DFA
            return [lt, M_str]
            # M_st is a matrix representing the modified transition function for the DFA

        else:  # recursive case

            i = i+1
            return self.dfa_states_store(i, lt, M_str)

    def accepting_states_DFA(self):

        L = self.dfa_states_store(0, [self.q0])
        l = len(L[0])

        for j in range(0, l):
            # checking whether the states in the constructed DFA has a non-empty intersection with the list of final states in the NFA, or not.
            if list(set(self.F) & set(L[0][j])) != []:
                # if the intersection is non-empty, we're storing the current state of DFA as one of the final state of the desired DFA
                self.F_DFA.append(L[0][j])

        #print("states of DFA : ")
        # print(L[0])
        # print(L[1])

        print("final state of DFA are : ")

        print(self.F_DFA)

    def states_of_DFA(self):

        L = self.dfa_states_store(0, [self.q0])
        l = len(L[0])

        x = int(input(print("Do you want to see the states of the constructed DFA from the given NFA? If 'yes : press 1, else : press 0.  Thank you")))

        if x == 1:
            print(" The states of the DFA are :")
            for i in range(0, l):
                print(" " + str(L[0][i])+" ")
        else:
            return

    def dfa_state_transition(self):
        L = self.dfa_states_store(0, [self.q0])
        l = len(L[0])

        x = int(input(print("Do you want to see the transition of the states of the constructed DFA, when acted upon by the alphabets? If 'yes : press 1, else : press 0.  Thank you")))

        if x == 1:
            for i in range(0, l):
                for j in range(0, len(self.A1)):
                    print(" The state "+str(L[0][i]) + " of the DFA will transit to "+str(
                        L[1][i][j])+" state after being acted upon by the alphabet "+str(self.A1[j]))

        else:
            return


nfa = NFA()
nfa.states()
nfa.alpahabet()
nfa.accepting_state_NFA()
nfa.transition_func_value_storing()
nfa.display()
nfa.dFA_ini_state()
#nfa.delta_modified(nfa.q0, nfa.Sigma[1])
#nfa.delta_modified(['d'], nfa.Sigma[2])

#nfa.closure_delta_modified(nfa.q0, nfa.Sigma[1])
#nfa.closure_delta_modified(nfa.q0, nfa.Sigma[0])
# print(nfa.dfa_states_store(0,[nfa.q0]))

nfa.accepting_states_DFA()
nfa.states_of_DFA()
nfa.dfa_state_transition()
