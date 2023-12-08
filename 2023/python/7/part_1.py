def load_input():
    with open("input.txt") as f:
        for line in f.readlines():
            yield line.strip()


cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def is_five_of_a_kind(hand):
    if len(set(hand)) == 1:
        return 1


def is_four_of_a_kind(hand):
    for card in hand:
        if hand.count(card) == 4:
            return 2


def is_full_house(hand):
    for card in hand:
        if hand.count(card) == 3 and len(set(hand)) == 2:
            return 3


def is_three_of_a_kind(hand):
    for card in hand:
        if hand.count(card) == 3 and len(set(hand)) == 3:
            return 4


def is_two_pairs(hand):
    for card in hand:
        if hand.count(card) == 2 and len(set(hand)) == 3:
            return 5


def is_one_pair(hand):
    for card in hand:
        if hand.count(card) == 2 and len(set(hand)) == 4:
            return 6


def find_combination(hand):
    for func in [is_five_of_a_kind, is_four_of_a_kind, is_full_house, is_three_of_a_kind, is_two_pairs, is_one_pair]:
        result = func(hand)
        if result:
            return result
    return 7


def sort_hands(hands):
    if len(hands) == 1:
        return hands
    for step in range(len(hands) + 1):
        for i in range(len(hands) - 1):
            hand = hands[i][0]
            next_hand = hands[i + 1][0]
            for j in range(len(hand)):
                if hand[j] == next_hand[j]:
                    continue
                elif cards.index(hand[j]) < cards.index(next_hand[j]):
                    hands[i], hands[i + 1] = hands[i + 1], hands[i]
                    break
                else:
                    break
    return hands


def handler():
    hands = []
    for line in load_input():
        hands.append(line.split(" "))
    sorted_by_combination = dict()
    for i in range(len(hands)):
        combination = find_combination(hands[i][0])
        if combination in sorted_by_combination.keys():
            sorted_by_combination[combination].append(hands[i])
        else:
            sorted_by_combination[combination] = [hands[i]]
    sorted_by_combination = dict(sorted(sorted_by_combination.items(), key=lambda x: x[0]))
    final_sort = []
    for key in sorted_by_combination.keys():
        final_sort.extend(sort_hands(sorted_by_combination[key]))
    final_sort = final_sort[::-1]
    result = 0
    for i in final_sort:
        r = int(i[1]) * (final_sort.index(i) + 1)
        result += r
    return result



if __name__ == '__main__':
    print(handler())