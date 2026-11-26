import unittest
from check_revision import check
class TestRevision(unittest.TestCase):
    def test_allowed(self): self.assertTrue(check("aBCd","aXd",1,3))
    def test_prefix(self): self.assertFalse(check("aBCd","zXd",1,3))
    def test_suffix(self): self.assertFalse(check("aBCd","aXz",1,3))
    def test_overlap(self): self.assertFalse(check("aaaa","aa",2,2))
    def test_insert(self): self.assertTrue(check("ab","aXb",1,1))
    def test_invalid(self):
        with self.assertRaises(ValueError): check("ab","ab",2,1)
if __name__=="__main__": unittest.main()
