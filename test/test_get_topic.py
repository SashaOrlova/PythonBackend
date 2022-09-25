import unittest
from unittest.mock import patch, MagicMock

from db import DB
from manager import Manager


class MyTestCase(unittest.TestCase):
    def test_wrong_topic(self):
        with patch.object(DB, "get_topic_number", return_value=0) as mock, self.assertRaises(Exception):
            manager = Manager()
            manager.get_comments(1)
            mock.assert_called_once()

    @patch.multiple('db.DB',
                    get_topic_number=MagicMock(return_value=2),
                    get_comments=MagicMock(return_value={
                        'topic': 'Test',
                        'comment': []
                    }))
    def test_empty_topic(self):
        manager = Manager()
        res = manager.get_comments(1)
        self.assertEqual(res['topic'], 'Test')
        self.assertEqual(res['comment'], [])

    @patch.multiple('db.DB',
                    get_topic_number=MagicMock(return_value=2),
                    get_comments=MagicMock(return_value={
                        'topic': 'Test',
                        'comment': ['Test1', 'Test2']
                    }))
    def test_topic(self):
        manager = Manager()
        res = manager.get_comments(1)
        self.assertEqual(res['topic'], 'Test')
        self.assertEqual(res['comment'], ['Test1', 'Test2'])


if __name__ == '__main__':
    unittest.main()
