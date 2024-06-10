import pytest

from pystringutils.cases import UpperCase, LowerCase, SnakeCase, TitleCase, UpperCamelCase, LowerCamelCase, \
    ScreamingSnakeCase, RageCase, StudlyCase


@pytest.mark.parametrize("input_string,expected_output", [("hEllö", "HELLÖ"), ("WorLd", "WORLD")])
def test_to_upper(input_string, expected_output):
    assert UpperCase(input_string) == expected_output


@pytest.mark.parametrize("input_string,expected_output", [("hEllO", "hello"), ("WorLd", "world")])
def test_to_lower(input_string, expected_output):
    assert LowerCase(input_string) == expected_output


@pytest.mark.parametrize("input_string,expected_output", [("hEllO", "Hello"), ("WorLd", "World")])
def test_to_title(input_string, expected_output):
    assert TitleCase(input_string) == expected_output


@pytest.mark.parametrize("input_string,expected_output",
                         [("hEllO", "Hello"), ("WorLd", "World"), ("the_quick_brown_fox", "TheQuickBrownFox")])
def test_to_upper_camel(input_string, expected_output):
    assert UpperCamelCase(input_string) == expected_output


@pytest.mark.parametrize("input_string",
                         ["hEllO"])
def test_to_upper_camel(input_string):
    res = StudlyCase(input_string)
    assert len(res) == len(input_string)


@pytest.mark.parametrize("input_string,expected_output",
                         [("hEllO", "Hello"), ("WorLd", "World"), ("the_quick_brown_fox", "TheQuickBrownFox")])
def test_to_lower_camel(input_string, expected_output):
    assert LowerCamelCase(input_string) == expected_output


@pytest.mark.parametrize("input_string,expected_output", [("helloWorld", "hello_world"), ("IDMapping", "id_mapping"),
                                                          ("MayThe4thBeWithYou", "may_the_4th_be_with_you"),
                                                          ("a", "a")])
def test_to_snake(input_string, expected_output):
    assert SnakeCase(input_string) == expected_output


@pytest.mark.parametrize("input_string,expected_output", [("helloWorld", "HELLO_WORLD"), ("IDMapping", "ID_MAPPING"),
                                                          ("MayThe4thBeWithYou", "MAY_THE_4TH_BE_WITH_YOU"),
                                                          ("a", "A")])
def test_to_screaming_snake(input_string, expected_output):
    assert ScreamingSnakeCase(input_string) == expected_output


@pytest.mark.parametrize("input_string,expected_output", [("helloWorld", "hElLoWoRlD"), ("IDMapping", "iDmApPiNg")])
def test_to_screaming_snake(input_string, expected_output):
    assert RageCase(input_string) == expected_output
