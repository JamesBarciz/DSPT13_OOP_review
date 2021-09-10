
class BaseCharacter:
    """
    This is the BaseCharacter model.

    Params:
      - name (str): name of the character
    """

    def __init__(self, name):
        self.name = name
        self.intel = 3
        self.stam = 3
        self.strn = 3
        self.agi = 3
        self.level = 1

    def level_up(self, increment=1):
        """Levels up a character"""

        if increment < 1 and isinstance(increment, int):
            raise Exception('Parameter "increment" must be an integer greater than or equal to 1.')

        dict_items = vars(self)
        stat_increase = 3 * increment

        for k, v in list(dict_items.items()):
            if type(v) == int and k != 'level':
                dict_items[k] += stat_increase
            elif k == 'level':
                dict_items[k] += increment

        self.__dict__.update(dict_items)

        if __name__ == '__main__':
            print(f'{self.name} has reached level {self.level}!')
            print(f'Intellect has increased by {stat_increase} to {self.intel}')
            print(f'Stamina has increased by {stat_increase} to {self.stam}')
            print(f'Strength has increased by {stat_increase} to {self.strn}')
            print(f'Agility has increased by {stat_increase} to {self.agi}')
        else:
            return self


class Mage(BaseCharacter):
    """The mage class!"""

    def __init__(self, name):
        super().__init__(name)
        self.intel += 2
        self.stam += 2
        self.health = 50 + (self.stam * 5)
        self.mana = 80 + (self.intel * 5)

    def display_stats(self):
        print(f'{self.name}\'s stats\n')
        print(f'\tTotal Health: {self.health}')
        print(f'\tTotal Mana:   {self.mana}')


m0 = Mage("Raistlin")


if __name__ == '__main__':
    m0.display_stats()
