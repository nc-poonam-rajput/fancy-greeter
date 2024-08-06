from src.greeting import greet_person


def test_greeting_returns_string():
    assert type(greet_person('Nadia')) == str


def test_greeting_greets_passed_person():
    assert greet_person('Nadia') == 'Good morning Nadia!'


def test_greeting_alternative_message_for_anon_person():
    assert greet_person('anon') == 'shhhh secret greeting'


def test_greeting_greets_Renee():
    assert greet_person('Renee') == 'Good morning Renee!'
