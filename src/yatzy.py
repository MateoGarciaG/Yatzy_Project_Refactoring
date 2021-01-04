class Yatzy:
    
    def __init__(self, *dices):
        self.dices = dices
        
        
    @staticmethod
    def ones(*dices):
        sum_ones = 0
        
        for dice in dices:
            if dice == 1:
                sum_ones += dice

        return sum_ones
    
    
    @staticmethod
    def twos(*dices):
        sum_twos = 0
        
        for dice in dices:
            if dice == 2:
                sum_twos += dice
        return sum_twos

    @staticmethod
    def threes(*dices):
        sum_three = 0
        
        for dice in dices:
            if dice == 3:
                sum_three += dice
        return sum_three
    

    def fours(self):
        sum_fours = 0
        
        for dice in self.dices:
            if dice == 4:
                sum_fours += dice
        return sum_fours
    
    

    def fives(self):
        sum_fives = 0
        
        for dice in self.dices:
            if dice == 5:
                sum_fives += dice
        return sum_fives
    

    def sixes(self):
        sum_sixes = 0
        
        for dice in self.dices:
            if dice == 6:
                sum_sixes += dice
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
                score += dice
                full_house -= 1

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
    def yatzy(*dices):
        score = 0
        if dices.count(dices[0]) == 5:
            score = 50
        else:
            return score

        return score


if __name__ == "__main__":
    print(Yatzy.full_house(6,6,5,5,6))