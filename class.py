class MyClass():
     # class variable outside the constructor
    my_class_variable = 0

    def __init__(self):
        # instance variable inside the constructor
        self.my_instance_variable = None

    def instance_method(self):
        print(self)

    @staticmethod
    def static_method():
        print("nothing")

    @classmethod
    def class_method(cls):
        print(cls)

my_object = MyClass()
my_object.instance_method()
MyClass.static_method()
MyClass.class_method()
