from review import BaseCharacter, Mage


def test_temp_level_one():
    b0 = BaseCharacter('Sariah Nouveau')
    assert isinstance(b0.level, int)
    assert b0.level == 1


def test_mage_health_and_resources():
    m0 = Mage('Raistlin')
    assert hasattr(m0, 'health')
    assert hasattr(m0, 'mana')


def test_mage_greater_stats():
    b0 = BaseCharacter('Sariah Nouveau')
    m0 = Mage('Raistlin')
    assert m0.intel > b0.intel
    assert b0.stam < m0.stam


def test_level_up():
    b0 = BaseCharacter('Sariah Nouveau')
    m0 = Mage('Raistlin')
    assert b0.level < b0.level_up().level
    assert m0.level < m0.level_up().level
