import unittest
from lint_text import lint
class TestLint(unittest.TestCase):
    def test_cliche(self): self.assertTrue(any(x[0]=="cliche" for x in lint("На сегодняшний день работаем.")))
    def test_repeat(self): self.assertTrue(any(x[0]=="repeated_word" for x in lint("мы мы проверили")))
    def test_clean(self): self.assertEqual(lint("Мы проверили отчёт."),[])
    def test_space(self): self.assertTrue(any(x[0]=="space_before_punctuation" for x in lint("Да , конечно.")))
if __name__=="__main__": unittest.main()
