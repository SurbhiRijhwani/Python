class Pet:
    print("Pet class initialized")

class Pet_profile_builder:
    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food
        print("Pet profile builder initialized")

pet_obj= Pet()
pet1= Pet_profile_builder("Buddy", "Dog", 5, "Bone")
pet2= Pet_profile_builder("Mittens", "Cat", 3, "Fish")
print("Pet 1: Name: {}, Type: {}, Age: {}, Favourite Food: {}".format(pet1.name, pet1.animal_type, pet1.age, pet1.favourite_food))
print("Pet 2: Name: {}, Type: {}, Age: {}, Favourite Food: {}".format(pet2.name, pet2.animal_type, pet2.age, pet2.favourite_food))