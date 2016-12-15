"""
Priority module - must contain a function with the name 'priority'
priority function is used by the scheduler module

"""

def priority(p):
    """
    Returns an integer priority for any process tuple 'p' given an input
    Higher the integer returned, higher the priority
    Here it returns an integer in the scale 1...10
    Example priority function code given below
    This could be replaced by any function that takes a process tuple and returns an integer
    """
    pMem = (10 - p[1]/100) if p[1] <= 1000 else 0
    pUrgency = 10 if (p[3] == 'high') else (5 if (p[3] == 'medium') else 3)
    pIO  = 2 if (p[3] == 'high') else (5 if (p[3] == 'medium') else 8)
    return (pMem + pUrgency + pIO)