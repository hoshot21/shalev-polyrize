class Person:
    """Person class"""
    def __init__(self):
        self.age = 1

    def __repr__(self):
        return f'Person(age={self.age})'
