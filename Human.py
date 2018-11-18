class Human(object):
    species = 'H. sapiens'

    def __init__(self, name):
        self.name = name
        self.age = 0

    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*grunt*"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age

