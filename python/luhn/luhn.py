class Luhn(object):
    def __init__(self, card_num):
        self.card_num = ''.join(filter(lambda x : x in '0123456789', card_num))

    def valid(self):
        temp = [int(num[1]) * 2 if (num[0]+1) % 2 == 0 else int(num[1]) for num in enumerate(self.card_num[::-1])]
        temp = [num - 9 if num > 9 else num for num in temp]
        return sum(temp) % 10 == 0