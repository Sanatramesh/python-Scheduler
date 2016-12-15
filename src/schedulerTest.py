'''
Created on Sep 18, 2012

@author: gsrinivasaraghavan
'''
import unittest
from testgenDecorator import for_examples
from scheduler import schedule, reset
from utils import areListsEqual

class TestScheduler(unittest.TestCase):

    def setUp(self):
        reset()

    @for_examples(([], []), ([("end", 0, ())], []), ([("kill", 0, ("some", 0, "high", "high", 0))], []))
    @for_examples(([("update", 0, ("some", 0, "high", "high", 0))], []))
    @for_examples(([("create", 10, ("some", 100, "high", "high", 290))], [("some",10,100), ("some",110,100), ("some",210,90)]))
    def testTrivals(self, triggers, refSchedule):
        '''
        Test trivial trigger lists
        '''
        l = schedule(triggers, 100)
        self.assertEqual(True, areListsEqual(refSchedule, l))


    @for_examples(([("create", 10, ("some", 100, "high", "high", 290)), ("kill", 120, "some")],
                   [("some",10,100), ("some",110,100)]))
    @for_examples(([("create", 10, ("some", 100, "high", "low", 290)), ("create", 105, ("another", 200, "low", "high", 150))],
                   [('some', 10, 100), ('some', 110, 100), ('another', 210, 100), ('some', 310, 90), ('another', 400, 50)]))
    @for_examples(([("create", 10, ("p1", 100, "high", "low", 290)),
                    ("create", 105, ("p2", 200, "low", "high", 150)),
                    ("update", 140, ("p1", 500, "low", "low", 200)),
                    ("create", 225, ("p3", 300, "high", "low", 500)),
                    ("create", 260, ("p4", 400, "medium", "high", 200)),
                    ("kill", 310, "p1")],
                   [('p1', 10, 100), ('p1', 110, 100), ('p2', 210, 100), ('p2', 310, 50), ('p3', 360, 100),
                    ('p4', 460, 100), ('p3', 560, 100), ('p4', 660, 100), ('p3', 760, 100), ('p3', 860, 100),
                    ('p3', 960, 100)]))
    def testComplexSchedules(self, triggers, refSchedule):
        '''
        Test trivial trigger lists
        '''
        l = schedule(triggers, 100)
        self.assertEqual(True, areListsEqual(refSchedule, l))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()