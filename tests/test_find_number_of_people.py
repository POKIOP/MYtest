''' File to test file "find_number_of_people" '''
import pytest

from source.d_load_csv import load_csv
from source.find_number_of_people import proceed_in_year, proceed_all_years, percent_of_passed, number_of_people_who_passed

@pytest.fixture(name='matura')
def fixture_get_csv():
    return load_csv('../source/matura.csv')
    

def test_proceed_in_year(matura):
    assert proceed_in_year(matura, region="Lubuskie", passs="przystąpiło", year = "2018" ) == 15750


def test_proceed_all_years(matura):
    assert proceed_all_years(matura, region = "Lubuskie", passs = "przystąpiło", sex = "both") == 77879


def test_number_of_people_who_passed(matura):
    assert number_of_people_who_passed(matura, region = "Lubuskie", passs = "zdało", sex = "both") == 61883


def test_percent_of_passed(matura):
    assert percent_of_passed(matura, region = "Lubuskie") == '79.46%'


def test_proceed_in_year_2(matura):
    assert proceed_in_year(matura, region="Polska", passs="przystąpiło", year = "2018" ) == 247840


def test_proceed_all_years_2(matura):
    assert proceed_all_years(matura, region = "Polska", passs = "przystąpiło", sex = "both") == 2935964


def test_number_of_people_who_passed_2(matura):
    assert number_of_people_who_passed(matura, region = "Polska", passs = "zdało", sex = "both") == 2295383


def test_percent_of_passed_2(matura):
    assert percent_of_passed(matura, region = "Polska") == '78.18%'

    

