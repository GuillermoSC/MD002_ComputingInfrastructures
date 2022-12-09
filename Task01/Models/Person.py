class Person:

    gender: str
    name: dict
    email: str
    age: int
    years_registered: int
    country: str

    def __init__(self, data: dict):
        self.gender = data['gender']
        self.name = data['name']
        self.email = data['email']
        self.age = data['dob']['age']
        self.years_registered = data['registered']['age']
        self.country = data['location']['country']

    def is_female(self):
        return self.gender == 'female'


def get_age(p: Person) -> int:
    return p.age


def get_name_len(p: Person) -> int:
    return len(p.name['first'])


def get_years_registered(p: Person) -> int:
    return p.years_registered


def get_gender_value(p: Person) -> int:
    return 1 if p.gender == 'male' else 0
