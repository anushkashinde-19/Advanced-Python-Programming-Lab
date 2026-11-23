
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def display(self):
        print("Singleton Design Pattern")

# Create objects
obj1 = Singleton()
obj2 = Singleton()

obj1.display()

# Check whether both objects are same
if obj1 is obj2:
    print("Both objects are same")
else:
    print("Different objects")
