import functools


# def decorator(func):
#     # @functools.wraps(func)
#     def my_run():
#         print('prepare:')
#         f = func
#         func()
#         print('game over!')
#         return f
#     return my_run
#
# @decorator
# def run():
#     print('run')
#
# def walk():
#     print('walk')
#
# # f = run()
# print(run.__name__)
#
# print(walk.__name__)
# # walk()

def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()


