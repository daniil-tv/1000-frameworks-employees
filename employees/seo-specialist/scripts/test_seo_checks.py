import unittest
from seo_checks import dedupe, overlap, validate
class Checks(unittest.TestCase):
    def test_dedupe(self):
        self.assertEqual(len(dedupe([{"query":" Foo "},{"query":"foo"}])["rows"]),1)
    def test_distinct_geo(self):
        self.assertEqual(len(dedupe([{"query":"foo","region":"A"},{"query":"foo","region":"B"}])["rows"]),2)
    def test_distinct_frequency(self):
        self.assertEqual(len(dedupe([{"query":"foo","frequency":"1"},{"query":"foo","frequency":"2"}])["rows"]),2)
    def test_overlap(self):
        self.assertEqual(overlap(["https://a.example/","https://b.example/"],["https://a.example/#x"])["jaccard"],0.5)
    def test_empty(self):
        with self.assertRaises(ValueError): overlap([],["https://a.example/"])
    def test_validate(self):
        self.assertEqual(validate([{"query":"a"}],["query","source"]),[{"row":2,"missing":["source"]}])
if __name__=="__main__": unittest.main()
