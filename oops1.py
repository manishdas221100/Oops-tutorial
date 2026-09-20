# init a class
class Employee:
    # special mthod/ magic method/ dunder method -- constructor

    def __init__(self):
        print("strted executing attributes")

        self.id = 123
        self.salary = 5000
        self.designation = "SDE"
        print("strted executing attributes initiated ")


    def travel(self, destination):
        print("this travel unction called manually")
        print(f"Employee ois traveling to {destination}")

# create an object ior instance of class
sam = Employee()
#sam.travel("Bali")
#print(sam.id)
print(type(sam))
