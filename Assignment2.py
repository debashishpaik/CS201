# Reading the file holding the DFA
f = open("Assignment2_DFA.txt", "rt")#FILE WHERE DFA IS STORED

# printing the states
states_1 = []
print(f.readline().strip())
temp = (f.readline()).strip()
for i in temp:
    states_1.append(i)
print(states_1)


# printing the Final states
final_state_1 = []
print(f.readline().strip())
temp = (f.readline()).strip()
for i in temp:
    final_state_1.append(i)
print(final_state_1)

# creating the DFA
DFA_1 = []  # To store the DFA

f.readline()  # just to avoid the emptyline
f.readline()  # just to avoid the stateinput1input2
for i in f:
    arr = []
    for j in i.strip():
        arr.append(j)
    DFA_1.append(arr)
# print(DFA_1)

# function to check if the states are equivalent.


def check(a, b):
    label0 = False
    label1 = False
    for i in DFA_1:
        if i[0] == a:
            in_0_a = i[1]
            in_1_a = i[2]
        if i[0] == b:
            in_0_b = i[1]
            in_1_b = i[2]
    for i in prev_equivalence:  # compare both for each input
        if in_0_a in i and in_0_b in i:
            label0 = True
        if in_1_a in i and in_1_b in i:
            label1 = True

    # if both 0 and 1 input are True
    if label0 and label1:
        return True
    else:
        return False


# I have used the partitioning method. in which i find the zero equivalence,
# one equivalence ..... n equivalence till n and n-1 equivalence are identical
# thereby treating the equivalent states as 1 state a new DFA has been created
# finding the zero equivalent
zero_equivalence = []


# separate the non final states from final states
a = []  # to store all the nonfinal states
for i in states_1:
    if i not in final_state_1:
        a.append(i)
# basically we separated the final states and the non final states
zero_equivalence = [a, final_state_1]
prev_equivalence = zero_equivalence


# function to create a new equivalence

def equi_func(p_equi):
    new_equi = []
    for i in p_equi:
        arr = i
        while arr:
            reject = []  # this will collect the rest for another round
            accept = []  # this will append the equivalent states to new_equi
            accept.append(arr[0])
            for j in range(1, len(arr)):
                if check(arr[0], arr[j]):  # collecting equivalent states
                    accept.append(arr[j])
                else:
                    reject.append(arr[j])  # collecting the rest
            new_equi.append(accept)
            arr = reject  # updating the arr value so that it can parse through the reject states
    return new_equi


# perform next equivalence based on the Zero equivalence
curr_equivalence = []
for i in states_1:
    curr_equivalence = equi_func(prev_equivalence)
    if curr_equivalence == prev_equivalence:  # if two continuous equivalence are same we stop
        break
    prev_equivalence = curr_equivalence  # updating for next round


def output(a):  # we took the set of states and we will find the output in this function
    out_0 = []  # to store all 0 input output states
    out_1 = []  # to store all 1 input output states
    for i in a:
        in_0 = in_1 = None
        for j in DFA_1:  # we extracted the output per state
            if j[0] == i:
                in_0 = j[1]
                in_1 = j[2]
            if in_0 not in out_0 and in_0 is not None:  # to match the 0 union to exiting state
                out_0.append(in_0)
            if in_1 not in out_1 and in_1 is not None:  # to match the 1 union to exiting state
                out_1.append(in_1)
    return out_0, out_1


def plot(states_2):  # this basically creates the minimized dfa
    global DFA_2
    for i in states_2:
        arr = []
        arr.append(i)
        out_0, out_1 = output(i)  # returns both union outputs
        for j in states_2:
            if out_0[0] in j:
                arr.append(j)
        for j in states_2:
            if out_1[0] in j:
                arr.append(j)
        DFA_2.append(arr)


def final():  # to find all the final state of minimized DFA
    f_state = []  # to store the final state
    for i in final_state_1:  # all states containing initial final states are final states
        for j in states_2:
            if i in j:
                if j not in f_state:  # to prevent appending of same states multiple times
                    f_state.append(j)
    return f_state


# creating the minimized DFA
states_2 = curr_equivalence
final_state_2 = final()
DFA_2 = []
plot(states_2)


# Printing the minimized DFA
print("\nState\tInput 1\tInput 2")
for i in DFA_2:
    print(f"{i[0]}\t{i[1]}\t{i[2]}")

# printing the final states for minimized DFA
print("\nFINAL STATES")
for i in final_state_2:
    print(i)
