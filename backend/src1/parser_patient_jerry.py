from backend.src1.parser_generic import MedicalDocParser
import re


class Patient_details_Parser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        # pass
        return{
            'patient_name': self.get_name(),
            'patient_phone_number': self.get_phone_number(),
            'patient_status': self.get_status(),
            'patient_medical_problem': self.get_medical_problem(),

        }

    def get_name(self):
        pattern = "Date\s\n(.*)(?:Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)"
        matches = re.findall(pattern, self.text)
        # pattern1 = "((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)"
        # date_matches = re.findall(pattern1, self.text)
        # date = date_matches[0]
        # matches.replace(date, '').strp()
        if len(matches) > 0:
            return matches[0].strip()

    def get_phone_number(self):
        pattern = "Date\s\n.*\s\n(.\d{3}.\s\d{3}.\d{4})"
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            return matches[0].strip()

    def get_status(self):
        pattern = "Have you had the Hepatitis B vaccination.\s\n(.*)List"
        # pattern = "Have you had the Hepatitis B vaccination\?\s\n.*(Yes|No)"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_medical_problem(self):
        pattern = "List any Medical Problems .*?:\n\s(.*)"  #"List.*\n(.+)"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()


if __name__ == '__main__':
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
    pp = Patient_details_Parser(document_text)

    print(pp.parse())
