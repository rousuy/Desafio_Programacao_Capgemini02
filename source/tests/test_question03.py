from questions.question03 import encrypt_message


def test_is_message_equals(capfd):
    """
    checks if the output format received by function x will be the same
    as expected given the expected variable
    """
    encrypt_message('tenha um bom dia')
    out, err = capfd.readouterr()
    assert out == 'taoa eum nmd hbi '
