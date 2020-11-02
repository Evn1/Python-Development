def field(items, *args):
    assert len(args) > 0
    for d in items:
        if(len(args) == 1):
            if d.get(args[0]) is None:
                continue
            yield d.get(args[0])
        else:
            for arg in args:
                if d.get(arg) is None:
                    continue
                yield d.get(arg)

goods = [
    {'title': 'Ковер', 'price': None, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
print(list(field(goods, 'title', 'price')))

