import unittest
from unittest.mock import patch, Mock

class TestGame(unittest.TestCase):

    def setUp(self):
        # Initialize the board before each test
        self.mocked_board = [
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0]
        ]

    @patch('js.document.getElementById')
    def test_slideLeft(self, mocked_get_element_by_id):
        mocked_tile = Mock()
        mocked_tile.innerText = ""
        mocked_tile.classList.value = ""
        
        
        with patch('js.board', new=self.mocked_board):
            slideLeft()

            self.assertEqual(mocked_get_element_by_id.call_count, 16)
            mocked_get_element_by_id.assert_called_with('0-0')
            mocked_get_element_by_id.return_value.updateTile.assert_called_with(mocked_tile, 2)

    @patch('js.document.getElementById')
    def test_slideRight(self, mocked_get_element_by_id):
        mocked_tile = Mock()
        mocked_tile.innerText = ""
        mocked_tile.classList.value = ""
        

        with patch('js.board', new=self.mocked_board):
            slideRight()

            self.assertEqual(mocked_get_element_by_id.call_count, 16)
            mocked_get_element_by_id.assert_called_with('0-0')
            mocked_get_element_by_id.return_value.updateTile.assert_called_with(mocked_tile, 2)

    def test_setTwo(self):
        with patch('js.board', new=self.mocked_board):
            setTwo()

            self.assertIn(2, [tile for row in self.mocked_board for tile in row])

    def test_hasEmptyTile(self):
        with patch('js.board', new=self.mocked_board):
            result = hasEmptyTile()

            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
