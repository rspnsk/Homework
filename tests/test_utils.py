import json
from unittest.mock import mock_open, patch
from src.utils import read_transactions


@patch('builtins.open', new_callable=mock_open, read_data=json.dumps([{"key": "value"}]))
def test_read_transactions(mock_file):
    result = read_transactions('fake_path.json')
    assert result == [{"key": "value"}]
    mock_file.assert_called_once_with('fake_path.json', 'r', encoding='utf-8')


def test_read_transactions_file_not_found():
    result = read_transactions('non_existent_file.json')
    assert result == []
