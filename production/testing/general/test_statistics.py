import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

import unittest
from production.general import statistics

class TestStatsBlock(unittest.TestCase):
    """
    Test the object initialisation and set pos method
    update method will be tested manually
    """

    #constructor: StatsBlock(self, header: str, subheaders: list[str], data: list[float|str])
    def test_initialise(self):
        
        b = statistics.StatsBlock("Header", ["Subheader"], ["Data"])
        self.assertIsNotNone(b)

    def test_subheaders_count(self):
        """
        Ensure subheader and data len are same so it pair up
        """
        #len(subheader) == len(data)
        b = statistics.StatsBlock("Header", ["Subheader1","Subheader2"], ["Data1","Data2"])
        self.assertEqual(len(b.subheaders),len(b.data))
        self.assertEqual(len(b.subheaders),2)

        #len(subheader) > len(data)
        b = statistics.StatsBlock("Header", ["Subheader1","Subheader2"], ["Data"])
        self.assertEqual(len(b.subheaders),len(b.data))
        self.assertEqual(len(b.subheaders),1)

        #len(subheader) < len(data)
        b = statistics.StatsBlock("Header", ["Subheader1"], ["Data1,Data2"])
        self.assertEqual(len(b.subheaders),len(b.data))
        self.assertEqual(len(b.subheaders),1)

    def test_set_data(self):
        #Ensure all data is converted into string and converted into 2 decimal places if it's float
        b = statistics.StatsBlock("Header", ["Subheader"], ["Data"])
        self.assertEqual(b.data[0], "Data")

        b = statistics.StatsBlock("Header", ["Subheader"], [100])
        self.assertTrue(type(b.data[0]),'str')
        self.assertEqual(b.data[0], "100")

        b = statistics.StatsBlock("Header", ["Subheader"], [99.123])
        self.assertEqual(b.data[0], "99.12")
    
    def test_format(self):
        return False


if __name__ == '__main__':
    unittest.main()