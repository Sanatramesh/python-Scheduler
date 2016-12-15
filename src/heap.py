def indices(n):
    return 2*n+1,2*n+2

def restoreheap(l,parent,n):
    left, right=indices(parent)
    if (right<n):
        if (l[parent]< max(l[left],l[right])):
            if (l[left]>l[right]):
                l[parent],l[left]=l[left],l[parent]
                restoreheap(l,left,n)
            else:
                l[parent],l[right]=l[right],l[parent]
                restoreheap(l,right,n)
    elif (left<n):
        if(l[parent]<l[left]):
            l[parent],l[left]=l[left],l[parent]
    return l
        
        
def makeHeap(l):
    n=len(l)
    for i in range (0,n):
        left ,right=indices(n-1-i)
        if (right<n):
            if (l[n-i-1]< max(l[left],l[right])):
                if (l[left]>l[right]):
                    l[n-1-i],l[left]=l[left],l[n-1-i]
                    restoreheap(l,left,n)
                else:
                    l[n-1-i],l[right]=l[right],l[n-1-i]
                    restoreheap(l,right,n)
        elif (left<n):
            if(l[n-1-i]<l[left]):
                l[n-1-i],l[left]=l[left],l[n-1-i]
    
    return l


def heap():
    l=[1,6,6,6,6,6]
    print makeHeap(l)



if __name__ == "__main__":
    heap()                
        
                