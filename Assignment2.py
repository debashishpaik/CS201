import xlrd
import os

class Minimization:



    

    def __init__(self):
        self.file_location='' #file location of the excel file

        self.Q =[] #['a','b','c','d','e','f'] list of finite states in the DFA
        self.A =[] #['0','1'] # alphabet set in the DFA
        self.q_0 = '' #'a'  # initial state of DFA
        self.F = [] # ['b','c','e']  # accepting states of DFA
        self.M =[] #[['d','b'],['c','f'],['c','f'],['a','e'],['c','f'],['f','f']]
        self.P_0=[] # for storing the initial partition
        self.q_1=''
        self.q_2=''
        self.P_new=[] # list for storing the states of the newly formed minimized DFA
        self.q_0_new=[] # list for storing the initial state of the newly formed minimized DFA
        self.F_new=[] # accepting states of the newly formed minimized DFA
        self.delta_new=[] # matrix for storing the new transition values(states) of the new states after being acted upon by the given alphabets 

        #self.T_L=[]

    def file_loc(self):
        self.file_location =input('give the location of the excel file'+ " :")

        #self.file_location ='.\DFA.xlsx'





    def states(self):  # function for storing the states of the DFA

        workbook=xlrd.open_workbook(self.file_location)
        sheet=workbook.sheet_by_index(0)  #sheet in which the states of the DFA are present in the first row, in the form of single characters

        self.Q=sheet.row_values(0)
        print(self.Q)



    def alpahabet(self):  # function for storing the alphabets(symbols) of the DFA
        workbook = xlrd.open_workbook(self.file_location)
        sheet = workbook.sheet_by_index(1)  # sheet in which the alphabets of the DFA are present in the first row, in the form of single characters
        self.A= sheet.row_values(0)
        print(self.A)

    def ini_state(self):
        workbook = xlrd.open_workbook(self.file_location)
        sheet = workbook.sheet_by_index(2)  # sheet in which the first shell is occupied by the initial state of the DFA
        self.q_0= sheet.row_values(0)
        print(self.q_0)

    def delta_function_matrix(self):
        workbook = xlrd.open_workbook(self.file_location)
        sheet = workbook.sheet_by_index(3)
        self.M = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        print(self.M)



    def accepting_state_DFA(self):  # storing the final states
        workbook = xlrd.open_workbook(self.file_location)
        sheet = workbook.sheet_by_index(4)  # sheet in which the final states of the DFA are present in the first row.
        self.F = sheet.row_values(0)
        print(self.F)

    def zero_level_partition(self):
        S=[]

        for i in range(0,len(self.Q)):
            if self.Q[i] not in self.F:
                S.append(self.Q[i])  # S is the list of all states that are not accepting

        self.P_0=[S,self.F] #zero level partition formed
        print(self.P_0)




    def partition(self,P):

        P1=[]
        T=[]
        U=[]

        for i in range(0,len(P)):
            T=self.partition_1(P[i],P) #partition of P[i]
            U=U+T
            #print(U) #new partition
            
            
        ctr=0
        for i in range(0,len(U)):
            
            if U[i] in P:
                ctr=ctr+1
        if ctr==len(U):
            
            print(P)
            self.P_new=P
            return P
                        #base case
                                #P contains lists, each of which can be thought of as the states of the new minimized DFA
        else:
            self.partition(U)  # i.e if new partitions are created, iterate the function once more


    def partition_1(self, P_i, P):
        L=[]
        t=0
        lst=[]
        j=0
        i=0

        for i in range(0, len(P_i)):
            #print(len(P_i))
            lst=[P_i[i]]
            #print(lst)

            for j in range(0,len(P_i)):
                ctr=0

                if j!=i:
                    
                    for k in range(0, len(self.A)):

                        self.q_1= self.transition(P_i[i],self.A[k])
                        self.q_2= self.transition(P_i[j],self.A[k])
                        #print(self.A[k])
                        #print(P_i[i]+" "+P_i[j])
                        #print( self.q_1 +" "+self.q_2 )

                        flag=0

                        for l in range(0,len(P)):

                            if self.q_1 in P[l] and self.q_2 in P[l]: #checking whether q1 and q2 are present in some partition of P
                            
                                flag=1  #indicating q1 & q2 belongs to A where A is an element in the list P

                    

                        if flag==1:
                        
                            ctr=ctr+1

                    if ctr== len(self.A):
                        #print(ctr)
                        lst.append(P_i[j])
                        #print(lst)

            if L==[]:
                #print(len(L))
                L.append(lst)
                #print(L)
            else:

                for i in range(0,len(L)):
                    #print(len(L))
                    #print(L)
                    if set(lst)!=set(L[i]):
                        t=t+1
                        #print(t)
                if t==len(L):
                    L.append(lst)
                    #print(L)

        #print(L)
        return L #returning the collection of all the partitions of P_i where P_i is an element of P

    def transition(self, q, s):
        state_index= self.Q.index(q)
        
        
        alphabet_index=self.A.index(s)
        
        #print(self.M[state_index][alphabet_index])

        return self.M[state_index][alphabet_index]  #returning the state at which 'q' will reach after acting upon the alphabet 's'
    
    def final_states_new(self):
        for i in range(0,len(self.P_new)):
            if self.subset(self.P_new[i],self.F):
                self.F_new.append(self.P_new[i])
        print(" The accepting states of the newly formed minimized DFA---->"+ str(self.F_new))

    def subset(self,L_1,L_2):
        ctr=0
        for i in range(0,len(L_1)):
            if L_1[i] in L_2:
                ctr=ctr+1
        if ctr==len(L_1):
            return True
        else:
            return False

    def new_initial_state(self):
        for i in range(0,len(self.P_new)):
            if self.q_0[0] in self.P_new[i]:
                self.q_0_new=self.P_new[i]
        print("The initial state of the modified DFA---->"+str(self.q_0_new))

    def transit_value_storing(self):
        for i in range(0,len(self.P_new)):
            self.delta_new.append(self.new_transition(self.P_new[i]))
    
    def new_transition(self,L):
        lst=[]
        trans_L=[]

        for i in range(0,len(self.A)):
            lst=self.new_transition_func(L,self.A[i])
            
            trans_L.append(lst)
            print("delta( " + str(L)+" , "+str(self.A[i])+" )--->"+str(lst))
        
        #print(trans_L)
        return trans_L
    
    def new_transition_func(self, L, c):
        state_0=L[0]
        state_T=self.M[self.Q.index(state_0)][self.A.index(c)]
        #print(state_T)

        for i in range(0,len(self.P_new)):
            if state_T in self.P_new[i]:
                #print(i)
                break
        #print(self.P_new[i])
        return self.P_new[i]









M= Minimization()
M.file_loc()
M.states()
M.alpahabet()
M.ini_state()
M.delta_function_matrix()
M.accepting_state_DFA()

M.zero_level_partition()

#M.partition_1()
#M.transition()
M.partition(M.P_0)
M.final_states_new()
M.new_initial_state()
M.transit_value_storing()
#M.new_transition_func(['a','d'],M.A[1])
#M.new_transition(['a','d'])







