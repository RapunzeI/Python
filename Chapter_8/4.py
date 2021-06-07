class Animal:
    def __init__(self, species = 'animal', language = 'make sounds'):
        self.spec = species
        self.lang = language

    def speak(self):
        return "I am a {} and I {}.".format(self.spec, self.lang)

snoopy = Animal('dog', 'bark')
tweety = Animal('canary')
animal = Animal()

print(snoopy.speak())
print(tweety.speak())
print(animal.speak())