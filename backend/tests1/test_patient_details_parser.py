import pytest

from backend.src1.parser_patient_details import Patient_details_Parser


# def test_get_name():
#     pp = Patient_details_Parser(document_text)
#     assert pp.get_name() == 'Kathy Crawford'
@pytest.fixture()
def doc_1_kathy():
    document_text = '''
17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No
List any Medical Problems (asthma, seizures, headaches}:

Migraine
    '''

    return Patient_details_Parser(document_text)


@pytest.fixture()
def doc_2_jerry():
    document_text = '''

Patient Medical Record

Patient Information Birth Date

Jerry Lucas June 27 1988

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201

United States Height:
170

In Case of Emergency
-_ OCC OO eee
Joe Lucas 4218 Wheeler Ridge Dr 
Buffalo, New York, 14201
Home phone United States
(990) 356-4561
Work phone
General Medical History
nn ee
Chicken Pox (Varicelia): Measles: .
NOT IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

Yes

List any Medical Problems (asthma, seizures, headaches):

N/A
        '''
    return Patient_details_Parser(document_text)


def test_get_patient_name(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_name() == 'Kathy Crawford'
    assert doc_2_jerry.get_name() == 'Jerry Lucas'


def test_get_phone_number(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_phone_number() == '(737) 988-0851'
    assert doc_2_jerry.get_phone_number() == '(279) 920-8204'

def test_parse(doc_1_kathy, doc_2_jerry):
    record_kathy = doc_1_kathy.parse()
    assert record_kathy['patient_name'] == 'Kathy Crawford'
    assert record_kathy['patient_phone_number'] == '(737) 988-0851'
    assert record_kathy['patient_status'] == 'No'
    assert record_kathy['patient_medical_problem'] == 'Migraine'



    record_jerry = doc_2_jerry.parse()
    assert record_jerry == {
        'patient_name': 'Jerry Lucas',
        'patient_phone_number': '(279) 920-8204',
        'patient_status': 'Yes',
        'patient_medical_problem': 'N/A'

    }
