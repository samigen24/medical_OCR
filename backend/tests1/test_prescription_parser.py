# Test driven development approach is used in software development
# Test code is to verify your code is working properly
# Test are of 2 types: Unit and Division test.
# we'll focus more on "Unit Test"
# You'll need a module called pytest.
from backend.src1.parser_prescription2 import PrescriptionParser

# first approach
# def test_get_name():
#     pp = PrescriptionParser(document_text1)
#     assert pp.get_field('patient_name') == 'Marta Sharapova'    # to assert our expectation
#
#
# def test_get_address():
#     pp = PrescriptionParser(document_text1)
#     assert pp.get_field('patient_address') == '9 tennis court, new Russia, DC'    # to assert our expectation
#
#
# document_text1 = '''
#         Dr John Smith, M.D
#         2 Non-Important Street,
#         New York, Phone (000)-111-2222
#         Name: Marta Sharapova Date: 5/11/2022
#         Address: 9 tennis court, new Russia, DC
#         K
#
#         Prednisone 20 mg
#         Lialda 2.4 gram
#         Directions:
#         Prednisone, Taper 5 mg every 3 days,
#         Finish in 2.5 weeks a
#         Lialda - take 2 pill everyday for 1 month
#         Refill: 2 times
#             '''
# second approach is to create a function for the document
# make it more compact

import pytest


@pytest.fixture()
def doc_1_sharav():
    document_text1 = '''
        
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times


Process finished with exit code 0
    '''
    return PrescriptionParser(document_text1)

#


def test_get_name(doc_1_sharav):
    assert doc_1_sharav.get_field('patient_name') == 'Marta Sharapova'    # to assert our expectation
    # assert doc_1_daniel.get_field('patient_name') == 'Daniel Jordan'    # to assert our expectation


def test_get_address(doc_1_sharav):
    assert doc_1_sharav.get_field('patient_address') == '9 tennis court, new Russia, DC'    # to assert our expectation
    # assert doc_1_daniel.get_field('patient_address') == '12 Ipaja court, new Russia, DC'    # to assert our expectation


def test_get_medicines(doc_1_sharav):
    assert doc_1_sharav.get_field('patient_medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'   # to assert our expectation
    # assert doc_1_daniel.get_field('patient_medicines') == 'Paracetamol 20 mg'    # to assert our expectation


def test_parse(doc_1_sharav, doc_1_daniel):
    record_sharav = doc_1_sharav.parse()
    assert record_sharav['patient_name'] == 'Marta Sharapova'
    assert record_sharav['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_sharav['patient_medicines'] == 'Prednisone 20 mg\nLialda 2.4 gram'
    # assert record_sharav['patient_drug_direction'] == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    # assert record_sharav['patient_refills'] == '3'
    # #
    # record_daniel = doc_1_daniel.parse()
    # assert record_virat == {
    #     'patient_name': 'Daniel Jordan',
    #     'patient_address': '12 Ipaja court, New Delhi',
    #     'patient_medicines': 'Paracetamol 20 mg',
    #     'patient_drug_direction': 'Use two tablets daily for three months',
    #     'patient_refills': '3'
    #}
