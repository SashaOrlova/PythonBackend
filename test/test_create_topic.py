import unittest
from unittest.mock import patch

from db import DB
from manager import Manager


class MyTestCase(unittest.TestCase):

    def test_empty_adding(self):
        manager = Manager()

        with patch.object(DB, "create_topic", return_value=1) as mock, self.assertRaises(Exception):
            manager.add_topic("")
            mock.assert_not_called()

    def test_adding(self):
        with patch.object(DB, "create_topic", return_value=1) as mock:
            manager = Manager()
            manager.add_topic("test")
            mock.assert_called_once()

    def test_add_many(self):
        with patch.object(DB, "create_topic") as mock:
            manager = Manager()
            manager.add_topic("test1")
            manager.add_topic("test2")
            manager.add_topic("test3")
            mock.assert_called()


if __name__ == '__main__':
    unittest.main()
