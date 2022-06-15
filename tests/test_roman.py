from hypothesis import assume
from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import sampled_from

from roman import __version__
from roman import convert

roman_letter_to_base_decimal = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def test_version():
    assert __version__ == '0.1.0'


def test_simple_numbers():
    assert convert.decimal_to_roman(1) == 'I'
    assert convert.decimal_to_roman(2) == 'II'
    assert convert.decimal_to_roman(3) == 'III'

    assert convert.decimal_to_roman(5) == 'V'
    assert convert.decimal_to_roman(6) == 'VI'
    assert convert.decimal_to_roman(7) == 'VII'
    assert convert.decimal_to_roman(8) == 'VIII'

    assert convert.decimal_to_roman(10) == 'X'
    assert convert.decimal_to_roman(11) == 'XI'
    assert convert.decimal_to_roman(12) == 'XII'
    assert convert.decimal_to_roman(13) == 'XIII'

    assert convert.decimal_to_roman(50) == 'L'
    assert convert.decimal_to_roman(51) == 'LI'
    assert convert.decimal_to_roman(52) == 'LII'
    assert convert.decimal_to_roman(53) == 'LIII'

    assert convert.decimal_to_roman(100) == 'C'
    assert convert.decimal_to_roman(101) == 'CI'
    assert convert.decimal_to_roman(102) == 'CII'
    assert convert.decimal_to_roman(103) == 'CIII'

    assert convert.decimal_to_roman(500) == 'D'
    assert convert.decimal_to_roman(501) == 'DI'
    assert convert.decimal_to_roman(502) == 'DII'
    assert convert.decimal_to_roman(503) == 'DIII'

    assert convert.decimal_to_roman(1000) == 'M'
    assert convert.decimal_to_roman(1001) == 'MI'
    assert convert.decimal_to_roman(1002) == 'MII'
    assert convert.decimal_to_roman(1003) == 'MIII'


@given(sampled_from('IVXLCDM'), integers(min_value=0, max_value=3))
@settings(print_blob=True, verbosity=Verbosity.verbose)
def test_simple_numbers_propbased(roman_letter, extra_i_count):
    assume(not (roman_letter == 'I' and extra_i_count == 3))  # exclude 'IIII'

    decimal = roman_letter_to_base_decimal[roman_letter] + extra_i_count

    roman_number = convert.decimal_to_roman(decimal)

    assert roman_number[0] == roman_letter
    assert len(roman_number[1:]) == extra_i_count
    assert all(letter == 'I' for letter in roman_number[1:])
