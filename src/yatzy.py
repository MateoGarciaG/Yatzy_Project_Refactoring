class Yatzy:
    """Class Yatzy: This class consist of a serie of methods that let us to play the Yatzy's game
    """
    
    #* Constructor Class Yatzy
    def __init__(self, *dices):
        self.dices = dices
        
    #* Static Method ones()
    @staticmethod
    def ones(*dices):
        """ones(): scores the sum of the dice 1

        Returns:
            int: sum of the dice 1
        """
        sum_ones = 0
        
        for dice in dices:
            if dice == 1:
                sum_ones += dice

        return sum_ones
    
    
    @staticmethod
    def twos(*dices):
        """twos(): scores the sum of the dice 2

        Returns:
            int: sum of the dice 2
        """
        sum_twos = 0
        
        for dice in dices:
            if dice == 2:
                sum_twos += dice
        return sum_twos

    @staticmethod
    def threes(*dices):
        """threes(): scores the sum of the dice 3

        Returns:
            int: sum of the dice 3
        """
        sum_three = 0
        
        for dice in dices:
            if dice == 3:
                sum_three += dice
        return sum_three
    

    def fours(self):
        """fours(): scores the sum of the dice 4

        Returns:
            int: sum of the dice 4
        """
        sum_fours = 0
        
        for dice in self.dices:
            if dice == 4:
                sum_fours += dice
        return sum_fours
    
    

    def fives(self):
        """fives(): scores the sum of the dice 5

        Returns:
            int: sum of the dice 5
        """
        sum_fives = 0
        
        for dice in self.dices:
            if dice == 5:
                sum_fives += dice
        return sum_fives
    

    def sixes(self):
        """sixes(): scores the sum of the dice 6

        Returns:
            int: sum of the dice 6
        """
        sum_sixes = 0
        
        for dice in self.dices:
            if dice == 6:
                sum_sixes += dice
        return sum_sixes
    
    @staticmethod
    def score_pair(*dices):
        """score_pair(): scores the sum of the two highest matching dice

        Returns:
            int: sum of the two highest matching dice
        """
        score = 0
        dices = sorted(dices, reverse=True)
        
        for dice in tuple(dices):
            if dices.count(dice) == 2:
                score = dice*2
                break
            else:
                continue
        
        return score
    

    @staticmethod
    def two_pair(*dices):
        """two_pair(): If there are two pairs of dice with the same number, the
        player scores the sum of these dice.

        Returns:
            int: scores the sum of these dice
        """
        dices = sorted(dices, reverse=True)
        score = 0
        total_two_pair = 4
        for dice in tuple(dices):
            if dices.count(dice) >= 2:
                total_two_pair -= 1
                if total_two_pair == 2 or total_two_pair == 0:
                    score += dice*2
        if total_two_pair >= 2:
            score = 0

        
        return score
        
    @staticmethod
    def three_of_a_kind(*dices):
        """three_of_a_kind(): If there are three dice with the same number, the player scores the sum of these dice. 

        Returns:
            int: scores the sum of these dice
        """
        score = 0
        dices = sorted(dices, reverse=True)
        for dice in tuple(dices):
            if dices.count(dice) >= 3:
                score = dice*3
                break
            else:
                continue
                
        return score
    
    
    @staticmethod
    def four_of_a_kind(*dices):
        """four_of_a_kind(): If there are four dice with the same number, the player scores the sum of these dice. 

        Returns:
            int: scores the sum of these dice
        """
        score = 0
        dices = sorted(dices, reverse=True)
        for dice in tuple(dices):
            if dices.count(dice) >= 4:
                score = dice*4
                break
            else:
                continue
                
        return score
    
    

    @staticmethod
    def small_straight(*dices):
        """small_straight(): Let us read if the dices are a small_straight: 1,2,3,4,5

        Returns:
            int: scores the sum of these dice
        """
        straight = 15
        score = 0
        
        for dice in dices:
            score += dice
        
        if score == straight:
            score = straight
        else:
            score = 0
        return score
    

    @staticmethod
    def large_straight(*dices):
        """large_straight(): Let us read if the dices are a large_straight: 2,3,4,5,6

        Returns:
            int: scores the sum of these dice
        """
        straight = 20
        score = 0
        
        for dice in dices:
            score += dice
        
        if score == straight:
            score = straight
        else:
            score = 0
        return score
    

    @staticmethod
    def full_house(*dices):
        """full_house(): Let us read If the dice are two of a kind and three of a kind, the player scores the sum of all the dice. 

        Returns:
            int: scores the sum of these dice
        """
        dices = sorted(dices, reverse=True)
        score = 0
        full_house = 5
        for dice in tuple(dices):
            if dices.count(dice) == 3 or dices.count(dice) == 2:
                score += dice
                full_house -= 1

        if full_house >= 1:
            score = 0
            
        return score
    
    @staticmethod
    def chance(*dices):
        """chance(): Let us read If The player scores the sum of all dice, no matter what they read.

        Returns:
            int: scores the sum of these dice
        """
        total = 0
        for dice in dices:
            total += dice
        return total

    @staticmethod
    def yatzy(*dices):
        """yatzy(): Let us read If all dice have the same number

        Returns:
            int: scores 50
        """
        score = 0
        if dices.count(dices[0]) == 5:
            score = 50
        else:
            return score

        return score
