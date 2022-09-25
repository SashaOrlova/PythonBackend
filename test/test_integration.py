import unittest

from manager import Manager


class FlaskrTestCase(unittest.TestCase):

    def test_add_topic(self):
        manager = Manager()
        res = manager.add_topic("Test")
        self.assertEqual(res, 1)
        comments = manager.get_comments(1)
        self.assertEqual(comments["topic"], "Test")

    def test_add_comment(self):
        manager = Manager()
        res = manager.add_topic("Test")
        self.assertEqual(res, 1)
        manager.add_comment(1, "Test1")
        comments = manager.get_comments(1)
        self.assertEqual(comments["topic"], "Test")
        self.assertEqual(comments["comments"], ["Test1"])

    def test_different_topics(self):
        manager = Manager()
        res1 = manager.add_topic("Test1")
        self.assertEqual(res1, 1)
        res2 = manager.add_topic("Test2")
        self.assertEqual(res2, 2)
        manager.add_comment(1, "Test3")
        manager.add_comment(1, "Test4")
        manager.add_comment(2, "Test5")

        comments_1 = manager.get_comments(1)
        self.assertEqual(comments_1["topic"], "Test1")
        self.assertEqual(comments_1["comments"], ["Test3", "Test4"])

        comments_2 = manager.get_comments(2)
        self.assertEqual(comments_2["topic"], "Test2")
        self.assertEqual(comments_2["comments"], ["Test5"])


if __name__ == '__main__':
    unittest.main()
