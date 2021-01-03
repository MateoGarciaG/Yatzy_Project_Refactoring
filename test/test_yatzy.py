from src.yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_ones():
        assert Yatzy.ones(1,2,3,4,5) == 1
        assert Yatzy.ones(1,2,1,4,5) == 2
        assert Yatzy.ones(6,2,2,4,5) == 0
        assert Yatzy.ones(1,2,1,1,1) == 4
        assert Yatzy.ones(1,1,1,1,1) == 5
        assert Yatzy.ones(1,2,1,1,2) == 3


def test_twos():
        assert Yatzy.twos(1,2,3,2,6) == 4
        assert Yatzy.twos(2,2,2,2,2) == 10
        assert Yatzy.twos(3,2,2,2,5) == 6
        assert Yatzy.twos(2,2,2,2,3) == 8
        assert Yatzy.twos(4,1,2,6,3) == 2
        assert Yatzy.twos(6,3,3,4,5) == 0


def test_threes():
        assert Yatzy.threes(1,2,3,2,3) == 6
        assert Yatzy.threes(2,3,3,3,3) == 12
        assert Yatzy.threes(2,1,3,1,4) == 3
        assert Yatzy.threes(2,3,3,3,5) == 9
        assert Yatzy.threes(2,5,6,1,1) == 0
        assert Yatzy.threes(3,3,3,3,3) == 15


def test_fours():
        assert Yatzy.fours(4,4,4,5,5) == 12
        assert Yatzy.fours(4,4,5,5,5) == 8
        assert Yatzy.fours(4,5,5,3,6) == 4
        assert Yatzy.fours(4,4,5,4,4) == 16
        assert Yatzy.fours(4,4,4,4,4) == 20
        assert Yatzy.fours(1,5,3,2,6) == 0


def test_fives():
        assert Yatzy.fives(4,4,4,5,5) == 10
        assert Yatzy.fives(4,4,5,5,5) == 15
        assert Yatzy.fives(4,5,5,5,5) == 20
        assert Yatzy.fives(5,5,5,5,5) == 25
        assert Yatzy.fives(4,5,3,2,6) == 5
        assert Yatzy.fives(4,1,2,6,4) == 0


def test_sixes():
        assert Yatzy.sixes(4,4,4,5,5) == 0
        assert Yatzy.sixes(4,4,6,5,5) == 6
        assert Yatzy.sixes(6,5,6,6,5) == 18
        assert Yatzy.sixes(6,6,6,6,5) == 24
        assert Yatzy.sixes(6,6,6,6,6) == 30
        assert Yatzy.sixes(2,3,2,6,6) == 12


def test_one_pair():
        assert Yatzy.score_pair(3,4,3,5,6) == 6
        assert Yatzy.score_pair(5,3,3,3,5) == 10
        assert Yatzy.score_pair(5,3,6,6,1) == 12
        assert Yatzy.score_pair(1,3,6,1,5) == 2
        assert Yatzy.score_pair(2,2,4,6,1) == 4
        


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


def test_three_of_a_kind():
        assert Yatzy.three_of_a_kind(3,3,3,4,5) == 9
        assert Yatzy.three_of_a_kind(5,3,5,4,5) == 15
        assert Yatzy.three_of_a_kind(3,3,3,3,5) == 9
        assert Yatzy.three_of_a_kind(2,3,2,2,5) == 6
        assert Yatzy.three_of_a_kind(6,3,5,6,6) == 18
        assert Yatzy.three_of_a_kind(1,1,3,1,5) == 3
        assert Yatzy.three_of_a_kind(4,1,4,1,4) == 12


def test_four_of_a_knd():
        assert 12 == Yatzy.four_of_a_kind(3,3,3,3,5)
        assert 20 == Yatzy.four_of_a_kind(5,5,5,4,5)
        assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)
        assert 0  == Yatzy.four_of_a_kind(3,3,3,2,1)


def test_smallStraight():
        assert 15 == Yatzy.smallStraight(1,2,3,4,5)
        assert 15 == Yatzy.smallStraight(2,3,4,5,1)
        assert 0 == Yatzy.smallStraight(1,2,2,4,5)


def test_largeStraight():
        assert 20 == Yatzy.largeStraight(6,2,3,4,5)
        assert 20 == Yatzy.largeStraight(2,3,4,5,6)
        assert 0 == Yatzy.largeStraight(1,2,2,4,5)


def test_fullHouse():
        assert 18 == Yatzy.fullHouse(6,2,2,2,6)
        assert 0 == Yatzy.fullHouse(2,3,4,5,6)

def test_chance_scores_sum_of_all_dice():
        expected = 15
        actual = Yatzy.chance(2,3,4,5,1)
        assert expected == actual
        assert 16 == Yatzy.chance(3,3,4,5,1)


def test_yatzy_scores_50():
        expected = 50
        actual = Yatzy.yatzy([4,4,4,4,4])
        assert expected == actual
        assert 50 == Yatzy.yatzy([6,6,6,6,6])
        assert 0 == Yatzy.yatzy([6,6,6,6,3])