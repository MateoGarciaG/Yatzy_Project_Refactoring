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
        assert 0 == Yatzy(4,4,4,5,5).sixes()
        assert 6 == Yatzy(4,4,6,5,5).sixes()
        assert 18 == Yatzy(6,5,6,6,5).sixes()


def test_one_pair():
        assert 6 == Yatzy.score_pair(3,4,3,5,6)
        assert 10 == Yatzy.score_pair(5,3,3,3,5)
        assert 12 == Yatzy.score_pair(5,3,6,6,5)


def test_two_pair():
        assert 16 == Yatzy.two_pair(3,3,5,4,5)
        assert 18 == Yatzy.two_pair(3,3,6,6,6)
        assert 0 == Yatzy.two_pair(3,3,6,5,4)


def test_three_of_a_kind():
        assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
        assert 15 == Yatzy.three_of_a_kind(5,3,5,4,5)
        assert 9 == Yatzy.three_of_a_kind(3,3,3,3,5)


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