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
            score = 15
        else:
            score = 0
        return score
    

    @staticmethod
    def large_straight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def full_house( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
    
    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
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


