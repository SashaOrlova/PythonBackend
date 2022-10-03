import unittest
from unittest.mock import patch, MagicMock

from db import DB
from manager import Manager


class MyTestCase(unittest.TestCase):
    def test_wrong_topic(self):
        with patch.object(DB, "get_topic_number", return_value=0) as mock, self.assertRaises(Exception):
            manager = Manager()
            manager.get_stat(1)
            mock.assert_called_once()

    @patch.multiple('db.DB',
                    get_topic_number=MagicMock(return_value=2),
                    get_comments=MagicMock(return_value={
                        'topic': 'Test',
                        'comment': []
                    }))
    def test_empty_topic(self):
        manager = Manager()
        comment_number, symbols_number = manager.get_stat(1)
        self.assertEqual(comment_number, 0)
        self.assertEqual(comment_number, 0)

    @patch.multiple('db.DB',
                    get_topic_number=MagicMock(return_value=2),
                    get_comments=MagicMock(return_value={
                        'topic': 'Test',
                        'comment': ['Test1', 'Test2']
                    }))
    def test_topic(self):
        manager = Manager()
        comment_number, symbols_number = manager.get_stat(1)
        self.assertEqual(comment_number, 'Test')
        self.assertEqual(symbols_number, ['Test1', 'Test2'])


if __name__ == '__main__':
    unittest.main()
