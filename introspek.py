import inspect



def introspection_info(number_info):
    print(number_info)

number_info = {'a': 'b', 'c': 'd'}
introspection_info(number_info)




print(type(introspection_info))
print(type(number_info))

print(dir(introspection_info))
print(hasattr(introspection_info, 'obj'))

print(callable(introspection_info))

print(isinstance(introspection_info, str))

introspection_info_module = inspect.getmodule(introspection_info)
print(type(introspection_info_module), introspection_info_module)
class Objects:
    pass
class Inospection_info(Objects):
    pass

print(issubclass(Inospection_info, Objects))
print(issubclass(Objects, Inospection_info))

