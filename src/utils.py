'''
For Python iMTech Mid Semester Exam - 26 Sep, 2012
Utility module with a set of generic useful functions
'''

def areListsEqual(l1, l2):
    """
    Check if two lists are equal to each other - have the same elements in the same order
    """
    same = (len(l1) == len(l2))
    if same:
        for i, r in enumerate(l1):
            same = (l2[i] == r)
            if not same:
                break
    return same