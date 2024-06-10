from __future__ import annotations

import random


class Case(str):
    @classmethod
    def validate(cls, s: str) -> bool:
        return cls.validate_no_whitespace(s)

    @classmethod
    def validate_no_whitespace(cls, s):
        return " " not in s


class UpperCase(Case):

    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        return s.upper()


class TitleCase(Case):

    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        return s.title()


class LowerCase:

    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        return s.lower()


class UpperCamelCase(Case):

    def __new__(cls, s: str, sep: str = "_"):
        assert Case.validate(s), f"Unsupported input string {s}"
        return "".join([chunk.capitalize() for chunk in s.split(sep)])


class LowerCamelCase(Case):

    def __new__(cls, s: str, sep: str = "_"):
        assert Case.validate(s), f"Unsupported input string {s}"
        chunks = s.split(sep)
        return chunks[0].lower() + "".join([chunk.capitalize() for chunk in chunks[1:]])


"""
HelloThere -> hello_there
MayThe4thBeWithYou ->  may_the_4th_be_with_you
IDMapping -> id_mapping
"""


class SnakeCase(Case):

    @staticmethod
    def split_camel_case(s: str):
        # Find all indices of uppercase characters not preceded by an upper case character
        # use double negation to deal with numbers
        cuts = [i for i, a, b in zip(range(1, len(s)), s[1:], s[2:]) if not b.isupper() and not a.islower()]
        return [0] + cuts + [len(s)]

    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        cuts = SnakeCase.split_camel_case(s)
        return "_".join([
            s[a:b].lower() for a, b in zip(cuts, cuts[1:])
        ])


class ScreamingSnakeCase(SnakeCase):
    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        cuts = SnakeCase.split_camel_case(s)
        return "_".join([s[a:b].upper() for a, b in zip(cuts, cuts[1:])])


class KebabCase(SnakeCase):
    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        cuts = SnakeCase.split_camel_case(s)
        return "-".join([s[a:b].lower() for a, b in zip(cuts, cuts[1:])])


class RageCase(Case):
    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        return "".join([c.upper() if i % 2 else c.lower() for i, c in enumerate(s)])


class StudlyCase(Case):
    def __new__(cls, s: str):
        assert Case.validate(s), f"Unsupported input string {s}"
        return "".join(map(lambda c: random.choice([c.upper, c.lower])(), s))
