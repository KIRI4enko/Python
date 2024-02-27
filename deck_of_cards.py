'''
    Колода карт(Объектно-ориентированное программирование), перемешивание, раздача
    Deck of Cards (Object Oriented Programming), mixing, distribution
'''
import random


class Card:
    suit_list = ['БУБИ', 'ЧЕРВЫ', 'ПИКИ', 'КРЕСТИ']
    nums_list = list(map(str, range(6, 11))) + ['Валет', "Дама", "Король", "Туз"]

    def __init__(self, suit_number: int, value: int):
        self.suit = Card.suit_list[suit_number]
        self.value = Card.nums_list[value]

    def __str__(self):
        return f'{self.value} {self.suit}'


class DeckOfCards:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for value in range(9):
                self.deck.append(Card(suit_number=suit, value=value))

    def __str__(self):
        return '\n'.join(list(map(str, self.deck)))

    def Shuffle_Deck(self):
        random.shuffle(self.deck)

    def Peak_Card(self):
        return self.deck.pop(0)





Deck = DeckOfCards()
Deck.Shuffle_Deck()
P1 = []
P2 = []
for i in range(6):
    P1.append(Deck.Peak_Card())
    P2.append(Deck.Peak_Card())

print(*P1,sep='\n')
print('=='*100)
print(*P2,sep='\n')

