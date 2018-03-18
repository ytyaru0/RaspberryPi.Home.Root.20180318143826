import math
from decimal import Decimal, ROUND_UP, ROUND_HALF_EVEN
class Size:
    def __init__(self, threshold=1024):
        self.__value = 0
        self.__n = 0
        self.__threshold = threshold # 1024 or 1000. 閾値(しきいち)
        self.__unit_names = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']

    # value: Byte (0 <= Byte <= 999*1024*(10**8))
    # unit: n (1024のn乗. 0 <= n ) 呼出時は不要。
    def Show(self, value, n=1):
        if math.fabs(value) < self.__threshold ** n:
            self.__value = value / self.__threshold ** (n-1)
            self.__n = n-1
            v = str(Decimal(self.__value).quantize(Decimal('100.01'), rounding=ROUND_UP)).replace('.00', '')
            return '{} {}'.format(v, self.Unit)
        else:
            return self.Show(value, n+1)

    @property
    def Unit(self):
        origin = ''
        if 1024 == self.__threshold and 0 < self.__n :
            origin = '{}i'.format(self.__unit_names[self.__n])
        if 1000 == self.__threshold:
            if 1 == self.__n: origin = 'k'
            else: origin = self.__unit_names[self.__n]
        return '{}B'.format(origin)

    # 末尾の0や.を削除する
    # v: 整数部と虚数部のテキスト
    def __Strip(self, v):
        i = v.find('.')
        if -1 == i: return v
        if v[i:].endswith('0') or v[i:].endswith('.'):
            v = v[:-1]
            return self.__Strip(v)
        else: return v

        
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1:
        raise Exception('引数エラー。Byteの整数値を1つください。「12.34 KiB」のように単位をつけて返します。')
    else:
        print(Size().Show(int(sys.argv[1])))
    """
    print(Size().Show(0))
    print(Size().Show(10))
    print(Size().Show(100))
    print(Size().Show(1023))
    print(Size().Show(1024))
    print(Size().Show(1025))
    print(Size().Show(1219))
    print(Size().Show(1024**2-1))
    print(Size().Show(1024**2))
    print(Size().Show(1024**2+1))

    print(Size().Show(-1))
    print(Size().Show(-1*1023))
    print(Size().Show(-1*1024))
    print(Size().Show(-1*1025))
    print(Size().Show(-1024**2-1))
    print(Size().Show(-1024**2))
    print(Size().Show(-1024**2+1))
    """
