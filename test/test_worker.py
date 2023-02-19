from unittest.mock import patch
from app.tasks import process_message

@patch('app.tasks.Message')
def test_process_message(mock_message):
    mock_message.objects.get.return_value = mock_message()
    mock_message.objects.get().delete.return_value = None
    process_message('Test message')
    mock_message.objects.get.assert_called_once_with(message='Test message')
    mock_message.objects.get().delete.assert_called_once_with()