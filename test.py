class User:
    def __init__(self, name):
        self.name = name

user_obj = User("mohamad")
print(hasattr(user_obj, 'name'))