from typing import List


def max_dd(pnls: List[float]) -> float:
    cur_price = 0
    pre_high = 0
    cur_max_dd = 0 
    cur_dd = 0
    
    for r in pnls:
        cur_price += r
        if cur_price > pre_high:
            pre_high = cur_price
            cur_dd = 0
        
        cur_dd = cur_price - pre_high
        if cur_dd < cur_max_dd:
            cur_max_dd = cur_dd

    return cur_max_dd


pnl = [1, -2, -1, 2]
mdd = max_dd(pnl)
assert mdd == -3

pnl = [1, -2, 1, -2, 6, -1, -10]
cumsum = [0]
for idx, r in enumerate(pnl):
    cumsum.append(cumsum[idx] + r)
print(cumsum[1: ])
mdd = max_dd(pnl)
assert mdd == -11

pnl = [1, -1, 1, -1, 1, -1]
mdd = max_dd(pnl)
assert mdd == -1
