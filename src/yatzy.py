class Yatzy:
    
    @staticmethod
    def ones(*dices):
        sum_ones = 0
        
        for dice in dices:
            if dice == 1:
                sum_ones += 1

        return sum_ones
    
    
    @staticmethod
    def twos(*dices):
        sum_twos = 0
        
        for dice in dices:
            if dice == 2:
                sum_twos += 1
        return sum_twos

    @staticmethod
    def threes(*dices):
        sum_three = 0
        
        for dice in dices:
            if dice == 3:
                sum_three += 1
        return sum_three
    
    @staticmethod
    def fours(*dices):
        sum_fours = 0
        
        for dice in dices:
            if dice == 4:
                sum_fours += 1
        return sum_fours
    
    
    @staticmethod
    def fives(*dices):
        sum_fives = 0
        
        for dice in dices:
            if dice == 5:
                sum_fives += 1
        return sum_fives
    
    @staticmethod
    def sixes(*dices):
        sum_sixes = 0
        
        for dice in dices:
            if dice == 5:
                sum_sixes += 1
        return sum_sixes
    
    @staticmethod
    def score_pair(*dices):
        
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
        dices = sorted(dices, reverse=True)
        score = 0
        full_house = 5
        for dice in tuple(dices):
            if dices.count(dice) == 3 or dices.count(dice) == 2:
                full_house -= 1
                if full_house == 3:
                    score += dice*2
                elif full_house == 0:
                    score += dice*3
        if full_house >= 1:
            score = 0

        
        return score
    
    @staticmethod
    def chance(*dices):
        total = 0
        for dice in dices:
            total += dice
        return total

    @staticmethod
    def yatzy(dice):
        counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
