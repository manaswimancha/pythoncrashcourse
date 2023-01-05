import unittest
from python_repos import APICall

class TestPythonRepos(unittest.TestCase):
    
    def setUp(self):
        self.call = APICall()

    def test_status(self):
        self.a = self.call.call_api(self.call.url,self.call.headers)
        self.assertEqual(self.a[0], 200)
        
    def test_matches_len(self):
        self.a = self.call.call_api(self.call.url,self.call.headers)
        self.assertTrue(self.a[1]["total_count"]==len(self.a[1]["items"]) or self.a[1]["incomplete_results"]==True)
        
    def test_not_empty(self):
        self.a = self.call.call_api(self.call.url,self.call.headers)
        self.assertGreater(self.a[1]["total_count"], 0)

if __name__ == '__main__':
    unittest.main()