from xml.etree import ElementTree


class Event:
    def __init__(self, node):
        self.name = ''


class Deck(Event):
    def __init__(self, node):
        Event.__init__(self, node)


class Selection(Event):
    def __init__(self, node):
        Event.__init__(self, node)


def load_all(filename):
    data = ElementTree.parse(filename).getroot()

    decks = dict()

    for d_node in data.find_all('deck'):
        deck = Deck(d_node)
        decks[deck.name] = deck

    for s_node in data.find_all('selection'):
        sel = Selection(s_node)
        decks[sel.name] = sel

    return decks