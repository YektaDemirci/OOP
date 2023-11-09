from typing import List
from suit import Card, Hand

class BlackJackCard(Card):
    def __init__(self, face_value, suit):
        super().__init__(face_value, suit)

    def value(self):
        if self.is_ace():
            return 1
        elif 11 <= self.face_value <= 13:
            return 10
        else:
            return self.face_value

    def min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.value()

    def max_value(self):
        if self.is_ace():
            return 11
        else:
            return self.value()

    def is_ace(self):
        return self.face_value == 1

    def is_face_card(self):
        return 11 <= self.face_value <= 13

class Hand:
    def __init__(self):
        self.cards = []

    def score(self):
        return sum(card.value() for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)

class BlackJackHand(Hand):
    def score(self):
        scores = self.possible_scores()
        max_under = float('-inf')
        min_over = float('inf')

        for score in scores:
            if score > 21 and score < min_over:
                min_over = score
            elif score <= 21 and score > max_under:
                max_under = score

        return min_over if max_under == float('-inf') else max_under

    def possible_scores(self):
        return [sum(card.value() for card in self.cards)]

    def busted(self):
        return self.score() > 21

    def is_21(self):
        return self.score() == 21

    def is_blackjack(self):
        return len(self.cards) == 2 and any(card.is_ace() for card in self.cards)
