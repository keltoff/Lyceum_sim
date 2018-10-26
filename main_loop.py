import deck


def repeat(items):
    while True:
        for i in items:
            yield i


def date_iterator():
    # for day in zip(repeat(['Po', 'Ut', 'St', 'Ct', 'Pa', 'So', 'Ne']), repeat(range(1, 30))):
    for day in repeat(['Po', 'Ut', 'St', 'Ct', 'Pa', 'So', 'Ne']):
        wday, date = day, 1

        yield 'morning', day

        if wday in ['So', 'Ne']:
            yield 'afternoon', day
        else:
            yield 'school', day

        yield 'lunch', day
        yield 'afternoon', day
        yield 'evening', day
        yield 'late', day
        yield 'sleep', day


def loop(handlers):
    for event, day in date_iterator():
        print('{}: {}'.format(event, day))
        handler = handlers.get(event)
        if handler:
            handler.        k = raw_input('? ')


if __name__ == '__main__':
    handlers = deck.load_all('cards.xml')
    loop(handlers)