import inspect


def introspection_info(obj):
    obj = 6
    print(f'на часах {obj}')

print(type(introspection_info))

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

