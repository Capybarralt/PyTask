def camel_to_snake(name):
    start = 0
    end = len(name)
    while start < end:
        if name[start].isupper():
            name = name.replace(name[start], '_' + name[start].lower())
            end = len(name)
        start += 1
    if name[0] == '_':
        name = name[1:]
    return name

def snake_to_camel(name):
    name = name.title() \
               .replace('_', '')
    return name
