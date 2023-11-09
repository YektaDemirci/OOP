from enum import Enum
from abc import ABC, abstractmethod
import random

class Suit(Enum):
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3

    def __new__(cls, value):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    @staticmethod
    def get_suit_from_value(value):
        return Suit(value) if 0<= value < 4 else None
    
class Card(ABC):
    def __init__(self, face_value, suit):
        self.available = True
        self.face_value = face_value
        self.suit = suit

    @abstractmethod
    def value(self):
        pass

    def is_available(self):
        return self.available

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True

class Deck(ABC):
    def __init__(self):
        self.cards = []
        self.dealt_index = 0

    def set_deck_of_cards(self, deck_of_cards):
        self.cards = deck_of_cards
    
    def shuffle(self):
        random.shuffle(self.cards)
        self.dealt_index = 0
    
    def remaining_cards(self):
        return len(self.cards) - self.dealt_index
    
    def deal_hand(self, number):
        if self.remaining_cards() >= number:
            hand = self.cards[self.dealt_index:self.dealt_index + number]
            self.dealt_index += number
            return hand
        else:
            return None
    
    def deal_card(self):
        if self.remaining_cards() > 0:
            card = self.cards[self.dealt_index]
            self.dealt_index += 1
            return card
        else:
            return None

class Hand(ABC):
    def __init__(self):
        self.cards = []

    def score(self):
        return sum(card.value() for card in self.cards)
    
    def add_card(self, card):
        self.cards.append(card)