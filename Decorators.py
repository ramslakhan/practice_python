
def new_decorator(func):
    print(func)
    def wrap_func():
        print("Code would be here, before executing the func")
        func()
        print("Code here will execute after the func()")
    return wrap_func


@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

print(func_needs_decorator)
func_needs_decorator()
#new_decorator.wrap_func()




