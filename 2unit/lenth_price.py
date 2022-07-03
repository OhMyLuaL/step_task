#!/usr/bin/env python
lenth=(len(str(input()))*60)


price_in_rub = lenth // 100
price_in_cop = lenth % 100


print(price_in_rub , 'р.' , price_in_cop , 'коп.')