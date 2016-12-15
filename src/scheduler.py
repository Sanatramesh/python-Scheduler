"""
Scheduler module - must contain a function with the name 'schedule'
It must also import a priority  module that will contain the priority function

"""

from priority import priority

def indices(n):
    return 2*n+1,2*n+2

def restoreheap(l,parent,n):
    left, right=indices(parent)
    if (right<n):
        if (priority(l[parent])< max(priority(l[left]),priority(l[right]))):
            if (priority(l[left])>priority(l[right])):
                l[parent],l[left]=l[left],l[parent]
                restoreheap(l,left,n)
            else:
                l[parent],l[right]=l[right],l[parent]
                restoreheap(l,right,n)
    elif (left<n):
        if(priority(l[parent])<priority(l[left])):
            l[parent],l[left]=l[left],l[parent]
    return l
        
        
def makeHeap(l):
    n=len(l)
    for i in range (0,n):
        left ,right=indices(n-1-i)
        if (right<n):
            if (priority(l[n-i-1])< max(priority(l[left]),priority(l[right]))):
                if (l[left]>l[right]):
                    l[n-1-i],l[left]=l[left],l[n-1-i]
                    restoreheap(l,left,n)
                else:
                    l[n-1-i],l[right]=l[right],l[n-1-i]
                    restoreheap(l,right,n)
        elif (left<n):
            if(priority(l[n-1-i])<priority(l[left])):
                l[n-1-i],l[left]=l[left],l[n-1-i]
    
    return l  

def clearprocessHeap(t,timeslice):
    global currentTime
    global P
    global S    
    while ((t[0]=="end" or t[1]>currentTime) and len(P)!=0):
        P=makeHeap(P)
        p=P[0]
        
        if (p[4]>0 and p[4]>timeslice):
            S.append((p[0],currentTime,timeslice))
            P.append((p[0],p[1],p[2],p[3],p[4]-timeslice,currentTime))
            currentTime+=timeslice
            P.pop(0)
        #elif (p[3]>0):
         #   P[0]=(p[0],p[1],p[2],p[3],currentTime)
        else:
            S.append((p[0],currentTime,p[4]))
            currentTime+=p[4]
            P.pop(0)
        
        
def reset():
    global P
    global S
    global currentTime
    P=[]
    S=[]
    currentTime=0
    
    

def schedule(triggers, timeslice):
    """
    Top level function that gets called when this code is tested.
    'triggers'- is a list of triggers; each trigger is a tuple (action, timestamp, val) 
    'timeslice' - is the length of each CPU time slice in milli-seconds
    This returns 'scheduleList' - list of (processName, cpuUsedFrom, cpuUsedFor) tuples
    """
    
    global currentTime
    global P
    global S
    currentTime=0
    P=[]
    S=[]    
    
    
    for t in triggers:
        clearprocessHeap(t,timeslice)
        if t[0]=="create":
            P.append((t[2][0],t[2][1],t[2][2],t[2][3],t[2][4],currentTime))
        elif t[0]=="update":
            for process in P:
                if process[0]==t[2][0]:
                    P[P.index(process)]=(t[2][0],t[2][1],t[2][2],t[2][3],t[2][4],currentTime)
        else:
            for process in P:
                if process[0]==t[2]:
                    P.remove(process)
        currentTime=max(currentTime,t[1])
    clearprocessHeap(("end",0,()),timeslice)
    return S


if __name__ == '__main__':
    print schedule([("create", 10, ("p1", 100, "high", "low", 290)),
                    ("create", 105, ("p2", 200, "low", "high", 150)),
                    ("update", 140, ("p1", 500, "low", "low", 200)),
                    ("create", 225, ("p3", 300, "high", "low", 500)),
                    ("create", 260, ("p4", 400, "medium", "high", 200)),
                    ("kill", 310, "p1")],100)