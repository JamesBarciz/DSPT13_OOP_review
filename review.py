import random
import time


class BaseCharacter:
    """
    This is the BaseCharacter model.

    Params:
      - name (str): name of the character
    """

    def __init__(self, name):
        self.name = name
        self.level = 1

        random_stat = self._rollD20()
        self.intel = random_stat
        self.stam = random_stat
        self.strn = random_stat
        self.agi = random_stat

    def _rollD20(self):
        """An internal method which simulates rolling a 20-sided die."""

        print(f'Determining stats for {self.name}...')
        time.sleep(1)
        print('Rolling 20-sided dice...')
        time.sleep(2)

        die_number = random.randint(1, 20)
        print(f'Rolled a {die_number}!')

        return die_number

    def _rollD10(self):
        """An internal method which simulates rolling a 10-sided die."""

        print('Rolling 10-sided die to determine bonus stats...')
        time.sleep(2)

        die_number = random.randint(1, 10)
        print(f'Rolled a {die_number}!')

        return die_number

    def level_up(self):
        """Levels up a character"""

        dict_items = vars(self)
        stat_increase = self._rollD20()

        for k, v in list(dict_items.items()):
            if type(v) == int and k != 'level':
                dict_items[k] += stat_increase
            elif k == 'level':
                dict_items[k] += 1

        self.__dict__.update(dict_items)

        if __name__ == '__main__':
            print(f'{self.name} has reached level {self.level}!')
            print(f'Intellect has increased by {stat_increase} to {self.intel}')
            print(f'Stamina has increased by {stat_increase} to {self.stam}')
            print(f'Strength has increased by {stat_increase} to {self.strn}')
            print(f'Agility has increased by {stat_increase} to {self.agi}')
        else:
            return self

    def change_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            raise Exception('Parameter "new_name" must be a string.')


class Mage(BaseCharacter):
    """The mage class!"""

    def __init__(self, name):
        super().__init__(name)
        time.sleep(2)
        bonus_stats = self._rollD10()
        self.intel += bonus_stats
        self.stam += bonus_stats
        self.health = 50 + (self.stam * 5)
        self.mana = 80 + (self.intel * 5)

    def display_stats(self):
        print(f'{self.name}\'s stats\n')
        print(f'\tTotal Health: {self.health}')
        print(f'\tTotal Mana:   {self.mana}')


if __name__ == '__main__':
    m0 = Mage('Merlin')
    breakpoint()
