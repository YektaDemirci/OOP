class BlackJackHand < Hand
    def score
      scores = possible_scores
      max_under = Float::INFINITY * -1
      min_over = Float::INFINITY
  
      scores.each do |score|
        if score > 21 && score < min_over
          min_over = score
        elsif score <= 21 && score > max_under
          max_under = score
        end
      end
  
      max_under == Float::INFINITY * -1 ? min_over : max_under
    end
  
    private
  
    def possible_scores
    end
  
    def busted
      score > 21
    end
  
    def is_21
      score == 21
    end
  
    def is_blackjack
    end
  end
  
  class BlackJackCard < Card
    def initialize(c, s)
      super(c, s)
    end
  
    def value
      return 1 if is_ace?
      return 10 if face_value.between?(11, 13)
  
      face_value
    end
  
    def min_value
      is_ace? ? 1 : value
    end
  
    def max_value
      is_ace? ? 11 : value
    end
  
    def is_ace?
      face_value == 1
    end
  
    def is_face_card?
      face_value.between?(11, 13)
    end
  end