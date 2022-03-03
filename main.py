from operator import itemgetter


def choose_sweet(d, money):
    sorted_tuple = sorted(d.items(), key=lambda x: x[1])
    d = dict(sorted_tuple)
    count = count_max_sweet(d, money)
    if count == 0:
        return []
    gold_reserve = dict(list(d.items())[:count - 1])
    summa = sum(gold_reserve.values())
    curr = None
    for item in sorted(d.items(), key=lambda x: x[1])[count - 1:len(d):1]:
        if summa + item[1] > money:
            break
        else:
            curr = item
    if curr is not None:
        gold_reserve[curr[0]] = curr[1]
    return list(gold_reserve.keys())


def count_max_sweet(d, money):
    summarize = 0
    count = 0
    for item in d.values():
        summarize += item
        if summarize > money:
            break
        count += 1
    return count
