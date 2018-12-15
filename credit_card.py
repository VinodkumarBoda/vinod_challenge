import re

PATTERN = r'^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def is_valid_creditcard(card):
    match_result = re.match(PATTERN, card)
    if not match_result:
        return False
    if card.count('-') not in (0, 3):
        return False
    if not has_four_consecutive_digits(card):
        return False
    return True
    
def has_four_consecutive_digits(card):
    card = card.replace("-", "")
    result = True
    card_list = list(card)
    for i in range(3,16):
        if card_list[i-3] == card_list[i] and card_list[i-2] == card_list[i] and card_list[i-1] == card_list[i]:
            result = False
            break
    return result

if __name__ == '__main__':
    cards_count = int(input())
    
    cards = []
    for count in range(cards_count):
        cards.append(input())

    for card in cards:
        if is_valid_creditcard(card):
            print('Valid')
        else:
            print('Invalid')