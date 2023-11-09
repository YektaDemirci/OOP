class Suit
    attr_reader :value
  
    def initialize(value)
      @value = value
    end
  
    Club = Suit.new(0)
    Diamond = Suit.new(1)
    Heart = Suit.new(2)
    Spade = Suit.new(3)
  
    def self.getSuitFromValue(value)
      case value
      when 0 then Club
      when 1 then Diamond
      when 2 then Heart
      when 3 then Spade
      else nil
      end
    end
  end
  
  class Card
    attr_accessor :available
    attr_reader :faceValue, :suit
  
    def initialize(faceValue, suit)
      @available = true
      @faceValue = faceValue
      @suit = suit
    end
  
    def value
      raise NotImplementedError, "Subclasses must implement the 'value' method"
    end
  
    def suit
      @suit
    end
  
    def isAvailable
      @available
    end
  
    def markUnavailable
      @available = false
    end
  
    def markAvailable
      @available = true
    end
  end
  
  class Deck
    attr_accessor :cards, :dealtIndex
  
    def initialize
      @cards = []
      @dealtIndex = 0
    end
  
    def setDeckOfCards(deckOfCards)
      @cards = deckOfCards
    end
  
    def shuffle
      @cards.shuffle!
      @dealtIndex = 0
    end
  
    def remainingCards
      @cards.size - @dealtIndex
    end
  
    def dealHand(number)
      return nil if remainingCards < number
  
      hand = @cards[@dealtIndex, number]
      @dealtIndex += number
      hand
    end
  
    def dealCard
      return nil if remainingCards.zero?
  
      card = @cards[@dealtIndex]
      @dealtIndex += 1
      card
    end
  end
  
  class Hand
    attr_accessor :cards
  
    def initialize
      @cards = []
    end
  
    def score
      @cards.sum(&:value)
    end
  
    def addCard(card)
      @cards << card
    end
  end