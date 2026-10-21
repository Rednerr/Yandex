try:
    import on_table
except ImportError:
    raise AssertionError('Модуль `practicum` не обнаружен.')

EXPECTED_FUNC_NAME = 'say_hello'

def test_say_hello_exists():
    assert hasattr(on_table, EXPECTED_FUNC_NAME), (
        f'Функция `{EXPECTED_FUNC_NAME}` не обнаружена в модуле `practicum`')