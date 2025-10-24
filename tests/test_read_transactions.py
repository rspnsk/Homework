from unittest.mock import mock_open, patch

import pandas as pd

from src.read_transactions import read_file_csv, read_file_excel

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


# тест для функции read_file_excel если файл пустой

@patch('pandas.read_excel')
def test_read_file_excel_empty_file(mock_read_excel):
    # Подготавливаем пустой DataFrame
    mock_df = pd.DataFrame(columns=['id', 'state'])
    mock_read_excel.return_value = mock_df

    # Ждём пустой результат
    expected_result = []

    # Читаем несуществующие данные
    result = read_file_excel('dummy_path.xlsx')

    # Утверждаем, что результат действительно пустой
    assert result == expected_result


# тест для функции read_file_excel если файл не существует

@patch('pandas.read_excel')
def test_read_file_excel_file_not_found(mock_read_excel):
    # Настроим так, чтобы попытка чтения приводила к ошибке FileNotFoundError
    mock_read_excel.side_effect = FileNotFoundError()

    # Ожидаем пустой результат
    expected_result = []

    # Пробуем считать несуществующий файл
    result = read_file_excel('nonexistent_file.xlsx')

    # Проверяем, что результат пуст
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
