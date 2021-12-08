# Κωνσταντίνα Έλληνα 1115201600046

prior = {}
class PQ:
    def __init__(self): # initialize list
        self.heap = []
        self.count = 0

    def Push(self, item, priority): # add an item in the list
            self.heap.append(item)
            self.count += 1
            prior[f'{item}'] = priority # save its priority on a dictionary

    def Pop(self): # pop an item off the list based on the minimum priority
        t = 0
        min1 = "a"
        for i in prior:
            if t == 0: # initialize minim
                minim = prior[i]
                t = 1
            if prior[i] <= minim: # find minimum priority
                minim = prior[i]
                min1 = i
        t = 0
        k = 0
        for i in prior: # find the indexing of the item on the list
            if i == min1:
                k = t
            t = t + 1
        
        del self.heap[k] # delete the item from the list
        p = prior.pop(min1) # pop out the item from prior
        self.count -= 1
        
        return p # return the popped item so i can use it in PQSort function
    

    def isEmpty(self): # check if the list is empty
        return(self.count == 0)
    
    def update(self, item, priority): # function of update
        t = 0 # counter for length of the prior
        for i in prior:
            if item == i: # item on the existing list
                if priority < prior[i]: # change to lower priority if needed
                    prior[f'{item}'] = priority
            else:
                t = t + 1
                
        if t == len(prior): # item not on the list
            self.Push(item, priority) # so push it with its priority
            
            
def PQSort(L): # function for sorted list
    K = []
    for i in range(len(L)):
        Q.Push(L[i], L[i]) # push the items of the list with priority its own number so i can sort them according to theirselfs.

    for i in range(len(L)):
        p = Q.Pop() # pop each time the lowest priority so the lowest number
        K.append(p) # append to the list of sorted
        
    return K # return the sorted list
    
# This is an indicative main for PQSort results.

#Q = PQ()   
#L = [3, 5, 2, 7, 8, 10, 4]
#P = PQSort(L)
#print(P)
