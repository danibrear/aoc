from utils import aslist, splitlines, ingroups, getday, getpath

from collections import Counter

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

WILD_CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def getHandValue(hand):
    sortedHand = sorted(hand, key=lambda x: CARDS.index(x))
    c = Counter(sortedHand)

    most = c.most_common(1)[0][0]

    if c[most] == 5:
        return 7
    elif c[most] == 4:
        return 6
    if c[most] == 3:
        if len(c) == 2:
            return 5
        else:
            return 4
    if c[most] == 2:
        if len(c) == 3:
            return 3
        else:
            return 2
    return 1


def getWildHand(hand):
    sortedHand = sorted(hand, key=lambda x: CARDS.index(x))
    c = Counter(sortedHand)

    JCount = c.pop("J", 0)

    if JCount == 5:
        return "AAAAA"
    most = c.most_common(1)[0][0]

    hand = hand.replace("J", most)
    return hand


def getWildHandValue(hand):
    return getHandValue(getWildHand(hand))


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

        self.value = getHandValue(cards)

        self.wildCards = getWildHand(cards)

        self.wildValue = getWildHandValue(cards)

    def compare(self, other, wild=False):
        mine = self.wildValue if wild else self.value
        theirs = other.wildValue if wild else other.value
        myCards = self.cards
        theirCards = other.cards

        CARDS_TO_USE = WILD_CARDS if wild else CARDS
        if mine > theirs:
            return 1
        elif mine < theirs:
            return -1
        else:
            for i in range(len(myCards)):
                if CARDS_TO_USE.index(myCards[i]) < CARDS_TO_USE.index(theirCards[i]):
                    return 1
                elif CARDS_TO_USE.index(myCards[i]) > CARDS_TO_USE.index(theirCards[i]):
                    return -1
            return 0


def sortHands(hands, wild=False):
    sortedHands = []
    for hand in hands:
        if len(sortedHands) == 0:
            sortedHands.append(hand)
        else:
            for i in range(len(sortedHands)):
                if hand.compare(sortedHands[i], wild) == 1:
                    sortedHands.insert(i, hand)
                    break
                elif hand.compare(sortedHands[i], wild) == 0:
                    sortedHands.insert(i + 1, hand)
                    break
                elif i == len(sortedHands) - 1:
                    sortedHands.append(hand)
                    break
    return sortedHands


def part1(lines):
    hands = []
    for line in lines:
        parts = line.split(" ")
        bid = int(parts[1])
        hand = Hand(parts[0], bid)

        hands.append(hand)

    sortedHands = sortHands(hands)

    total = sum([(len(sortedHands) - i) * h.bid for i, h in enumerate(sortedHands)])
    print(total)
    return total


def part2(lines):
    hands = []
    for line in lines:
        parts = line.split(" ")
        bid = int(parts[1])
        hand = Hand(parts[0], bid)

        hands.append(hand)

    sortedHands = sortHands(hands, wild=True)

    # for hand in sortedHands:
    #     print(hand.cards, hand.value, "::", hand.wildCards, hand.wildValue)

    total = sum([(len(sortedHands) - i) * h.bid for i, h in enumerate(sortedHands)])
    print(total)
    return total


path = getpath(__file__)
with open("{}/day7.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    p1v = part1(lines)  # 248105065
    p2v = part2(lines)  # 249515436

    assert p1v == 248105065
    assert p2v == 249515436
