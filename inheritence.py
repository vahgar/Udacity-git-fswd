
class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constructor Called")
        self.eye_color = eye_color
        self.last_name = last_name

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child Called")
        Parent.__init__(self,last_name,eye_color)
        self.toys = number_of_toys



miley_cyrus = Child("Cyrus","blue",5)

print(miley_cyrus.last_name)
print(miley_cyrus.toys)
