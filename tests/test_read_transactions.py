from unittest.mock import patch, mock_open
import pandas as pd
from src.read_transactions import read_file_excel, read_file_csv


# тест для функции read_file_excel

@patch('pandas.read_excel')
def test_read_file_excel(mock_read_excel):
    # Создаём DataFrame, который будет возвращать mock
    mock_data = {
        'id': [650703],
        'state': ['EXECUTED'],
        'date': ['2023-09-05T11:30:32Z'],
        'amount': [16210],
        'currency_name': ['Sol'],
        'currency_code': ['PEN'],
        'from': ['Счет 58803664561298323391'],
        'to': ['Счет 39745660563456619397'],
        'description': ['Перевод организации']
    }
    mock_df = pd.DataFrame.from_dict(mock_data)
    mock_read_excel.return_value = mock_df

    expected_result = [
        {
            'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        }
    ]

    result = read_file_excel('dummy_path.xlsx')
    assert result == expected_result


# тест для функции read_file_csv

@patch('builtins.open', new_callable=mock_open,
       read_data='id;state;date;amount;currency_name;currency_code;from;to;description\n'
                 '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;'
                 'Счет 39745660563456619397;Перевод организации')
def test_read_file_csv(mock_open):
    expected_result = [
        {
            'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        }
    ]
    result = read_file_csv('dummy_path.csv')
    assert result == expected_result
