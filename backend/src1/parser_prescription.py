from backend.src1.parser_generic import MedicalDocParser
import re


class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        # pass
        return{
            'patient_name': self.get_name(),
            'patient_address': self.get_address(),
            'patient_medicines': self.get_medicines(),
            'patient_drug_direction': self.get_directions(),
            'patient_refill': self.get_refill()
        }

    def get_name(self):
        pattern = "Name:(.*)Date"
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            return matches[0].strip()

    def get_address(self):
        pattern = "Address:(.*)\n"
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            return matches[0].strip()

    def get_medicines(self):
        pattern = "K[^\n]*(.*)Directions"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_directions(self):
        pattern = "Directions:[^\n]*(.*)Refill"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_refill(self):
        pattern = "Refill:(.*)times"   # to extract only the number of refill
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()


if __name__ == '__main__':
    document_text = '''

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
    pp = PrescriptionParser(document_text)
    print(pp.get_name())
    print(pp.get_address())
    print(pp.parse())
