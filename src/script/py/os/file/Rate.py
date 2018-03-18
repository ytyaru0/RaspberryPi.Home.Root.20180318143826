#!python3
import math
from decimal import Decimal, ROUND_DOWN

# Raspbianにshのbcコマンドがなかったので作った
class Rate:
    def Get(self, before:int, after:int) -> Decimal:
        return Decimal((1 - (after / before))*-1*100).quantize(Decimal('100.01'), rounding=ROUND_DOWN)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        raise Exception('引数エラー。Byteの整数値を2つください。変換前と後の2値をくれたら減量比率テキストを返します。')
    else:
        print(Rate().Get(int(sys.argv[1]), int(sys.argv[2])))
            
