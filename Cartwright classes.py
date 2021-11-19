from random import randint


class Human():

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def make_excuse(self):
        excuses = ['I died', 'My dog killed me', 'I missed my train', 'I slept in', "I don't like your class",
                   'Snow blocked me door', ' My mum told me to go late', ' I had a doctor appointment', "I had a dentist's appointment"]
        print(f'Sorry sir, {excuses[randint(0,len(excuses))]}')


Adrian = Human('Adrian', '16', 'Male')

Adrian.make_excuse()
