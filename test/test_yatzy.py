from src.yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

#* Casos test del método estático  ones()
def test_ones():
        assert Yatzy.ones(1,2,3,4,5) == 1
        assert Yatzy.ones(1,2,1,4,5) == 2
        assert Yatzy.ones(6,2,2,4,5) == 0
        assert Yatzy.ones(1,2,1,1,1) == 4
        assert Yatzy.ones(1,1,1,1,1) == 5
        assert Yatzy.ones(1,2,1,1,2) == 3

#* Casos test del método estático  twos()
def test_twos():
        assert Yatzy.twos(1,2,3,2,6) == 4
        assert Yatzy.twos(2,2,2,2,2) == 10
        assert Yatzy.twos(3,2,2,2,5) == 6
        assert Yatzy.twos(2,2,2,2,3) == 8
        assert Yatzy.twos(4,1,2,6,3) == 2
        assert Yatzy.twos(6,3,3,4,5) == 0

#* Casos test del método estático  thress()
def test_threes():
        assert Yatzy.threes(1,2,3,2,3) == 6
        assert Yatzy.threes(2,3,3,3,3) == 12
        assert Yatzy.threes(2,1,3,1,4) == 3
        assert Yatzy.threes(2,3,3,3,5) == 9
        assert Yatzy.threes(2,5,6,1,1) == 0
        assert Yatzy.threes(3,3,3,3,3) == 15

#* Casos test del método no estático fours()
def test_fours():
        assert Yatzy(4,4,4,5,5).fours() == 12
        assert Yatzy(4,4,5,5,5).fours() == 8
        assert Yatzy(4,5,5,3,6).fours() == 4
        assert Yatzy(4,4,5,4,4).fours() == 16
        assert Yatzy(4,4,4,4,4).fours() == 20
        assert Yatzy(1,5,3,2,6).fours() == 0

#* Casos test del método no estático  fives()
def test_fives():
        assert Yatzy(4,4,4,5,5).fives() == 10
        assert Yatzy(4,4,5,5,5).fives() == 15
        assert Yatzy(4,5,5,5,5).fives() == 20
        assert Yatzy(5,5,5,5,5).fives() == 25
        assert Yatzy(4,5,3,2,6).fives() == 5
        assert Yatzy(4,1,2,6,4).fives() == 0

#* Casos test del método no estático  sixes()
def test_sixes():
        assert Yatzy(4,4,4,5,5).sixes() == 0
        assert Yatzy(4,4,6,5,5).sixes() == 6
        assert Yatzy(6,5,6,6,5).sixes() == 18
        assert Yatzy(6,6,6,6,5).sixes() == 24
        assert Yatzy(6,6,6,6,6).sixes() == 30
        assert Yatzy(2,3,2,6,6).sixes() == 12

#* Casos test del método estático  score_pair()
def test_one_pair():
        assert Yatzy.score_pair(3,4,3,5,6) == 6
        assert Yatzy.score_pair(5,3,3,3,5) == 10
        assert Yatzy.score_pair(5,3,6,6,1) == 12
        assert Yatzy.score_pair(1,3,6,1,5) == 2
        assert Yatzy.score_pair(2,2,4,6,1) == 4
        

#* Casos test del método estático  two_pair()
def test_two_pair():
        assert Yatzy.two_pair(3,3,5,4,5) == 16
        assert Yatzy.two_pair(3,3,6,6,6) == 18
        assert Yatzy.two_pair(3,3,6,5,4) == 0
        assert Yatzy.two_pair(3,2,2,4,4) == 12
        assert Yatzy.two_pair(1,1,5,5,6) == 12
        assert Yatzy.two_pair(3,3,2,2,4) == 10
        assert Yatzy.two_pair(6,6,5,1,1) == 14
        assert Yatzy.two_pair(3,3,4,4,6) == 14
        assert Yatzy.two_pair(6,6,5,1,5) == 22

#* Casos test del método estático  three_of_a_kind()
def test_three_of_a_kind():
        assert Yatzy.three_of_a_kind(3,3,3,4,5) == 9
        assert Yatzy.three_of_a_kind(5,3,5,4,5) == 15
        assert Yatzy.three_of_a_kind(3,3,3,3,5) == 9
        assert Yatzy.three_of_a_kind(2,3,2,2,5) == 6
        assert Yatzy.three_of_a_kind(6,3,5,6,6) == 18
        assert Yatzy.three_of_a_kind(1,1,3,1,5) == 3
        assert Yatzy.three_of_a_kind(4,1,4,1,4) == 12

#* Casos test del método estático  four_of_a_kind()
def test_four_of_a_kind():
        assert Yatzy.four_of_a_kind(3,3,3,3,5) == 12
        assert Yatzy.four_of_a_kind(5,5,5,4,5) == 20
        assert Yatzy.four_of_a_kind(3,3,3,3,3) == 12
        assert Yatzy.four_of_a_kind(3,3,3,2,1) == 0
        assert Yatzy.four_of_a_kind(1,1,3,1,1) == 4
        assert Yatzy.four_of_a_kind(2,2,2,5,2) == 8
        assert Yatzy.four_of_a_kind(3,6,6,6,6) == 24
        

#* Casos test del método estático  small_straight()
def test_small_straight():
        
        score = 15
        
        assert Yatzy.small_straight(1,2,3,4,5) == score
        assert Yatzy.small_straight(2,3,4,5,1) == score
        assert Yatzy.small_straight(1,2,5,4,3) == score
        assert Yatzy.small_straight(2,1,3,5,4) == score
        assert Yatzy.small_straight(5,4,3,2,1) == score
        assert Yatzy.small_straight(1,6,6,5,1) == 0

#* Casos test del método estático  large_straight()
def test_large_straight():
        
        score = 20
        
        assert Yatzy.large_straight(6,2,3,4,5) == score
        assert Yatzy.large_straight(2,3,4,5,6) == score
        assert Yatzy.large_straight(3,5,2,6,4) == score
        assert Yatzy.large_straight(6,2,5,3,4) == score
        assert Yatzy.large_straight(5,6,3,4,2) == score
        assert Yatzy.large_straight(1,2,2,4,5) == 0

#* Casos test del método estático  full_house()
def test_full_house():
        assert Yatzy.full_house(6,2,2,2,6) == 18
        assert Yatzy.full_house(2,3,4,5,6) == 0
        assert Yatzy.full_house(2,2,2,5,5) == 16
        assert Yatzy.full_house(1,3,3,1,1) == 9
        assert Yatzy.full_house(6,6,5,5,6) == 28

#* Casos test del método estático  chance()
def test_chance_score():

        assert Yatzy.chance(2,3,4,5,1) == 15
        assert Yatzy.chance(3,3,4,5,1) == 16
        assert Yatzy.chance(1,3,2,5,5) == 16
        assert Yatzy.chance(1,1,1,5,1) == 9
        assert Yatzy.chance(2,2,4,5,2) == 15
        assert Yatzy.chance(6,6,4,6,6) == 28
        assert Yatzy.chance(1,3,1,5,6) == 16

#* Casos test del método estático  yatzy()
def test_yatzy_scores():
        score = 50
        
        assert Yatzy.yatzy(4,4,4,4,4) == score
        assert Yatzy.yatzy(6,6,6,6,6) == score
        assert Yatzy.yatzy(6,6,6,6,3) == 0
        assert Yatzy.yatzy(1,1,1,1,1) == score
        assert Yatzy.yatzy(2,2,2,2,2) == score
        assert Yatzy.yatzy(3,3,3,3,3) == score
        assert Yatzy.yatzy(5,5,5,5,5) == score
