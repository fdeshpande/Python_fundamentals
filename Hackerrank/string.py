from collections import Counter


def getLargestString(s, k):
    d = Counter(s)
    result = []

    while d:
        chars = sorted(d.keys(), reverse=True)

        for ch in chars:
            if d[ch] == 0:
                continue

            to_add = min(d[ch], k)
            result.append(ch * to_add)
            d[ch] -= to_add

            if d[ch] == 0:
                del d[ch]

            if len(result) > k and result[-1] * k == result[-k:]:
                if d:
                    for next_ch in chars:
                        if next_ch in d and d[next_ch] > 0:
                            result.append(next_ch)
                            d[next_ch] -= 1

                            if d[next_ch] == 0:
                                del d[next_ch]
                            break

    return ''.join(result)

# Test case
print(getLargestString('baccc', 2))

