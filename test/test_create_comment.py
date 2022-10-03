import unittest
from unittest.mock import patch

from db import DB
from manager import Manager


class MyTestCase(unittest.TestCase):
    def test_empty_adding(self):
        manager = Manager()

        with patch.object(DB, "create_comment", return_value=1) as mock, self.assertRaises(Exception):
            manager.add_comment(1, "")
            mock.assert_not_called()

    def test_wrong_topic(self):
        with patch.object(DB, "get_topic_number", return_value=0) as mock, self.assertRaises(Exception):
            manager = Manager()
            manager.add_comment(1, "test")
            mock.assert_called_once()

    def test_add(self):
        with patch.object(DB, "get_topic_number", return_value=2) as mock:
            manager = Manager()
            manager.add_comment(1, "test")
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
