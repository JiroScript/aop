import random
import string
# ジェネレータ:発生器
class generator:
    def random_strings(count, length, upper=True, digits_only=False, letters_only=False):
        """指定された個数と長さのランダムな文字列を生成する関数"""
        letters = ""
        if letters_only:
            letters = string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        elif digits_only:
            letters = string.digits # 0123456789
        else:
            letters = string.ascii_letters + string.digits # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        (random.choice(letters)) # f
        result_list = []
        for i in range(count):
            result_str = ''.join(random.choice(letters) for i in range(length))
            if not upper:
                result_str = result_str.lower()
            result_list.append(result_str)
        
        return result_list
    
    def random_ints(count, length):
        """乱数とは、「でたらめな数」。
        コンピュータが発生させる乱数は「疑似乱数」と言って完全にでたらめではない"""
        i1 = 10 ** (length - 1 )
        i9 = 10 ** length - 1
        t = i1, i9 # タプルのパック」
        i1, i9 = t #「アンパック」
        l = [ random.randint(*t)  for _ in range(1,count + 1)]
        return l
if None : 
    l = generator.random_strings(count=3, length=8, upper = False, digits_only=False, letters_only=False)              
    (l) # ['cwodq8rw', 'g8jqsz01', 'oqydllm5']
    l = generator.random_ints(count=10 , length=4)
    (l) # 
    d = {'乱数':'「でたらめな数」。コンピュータが発生させる乱数は「疑似乱数」と言って完全にでたらめではない'}

def read__csv(  d):
    import pandas as pd
    # CSVファイルからデータを読み込む
    # encoding='cp932' 日本語で拡張文字が含まれている場合
    df = pd.read_csv(d.get('file'), index_col=d.get('index_col'), header=d.get('header'), encoding=d.get('encoding')) 
    (df)
if None : read__csv( {'file': 'term.csv', 'header':None, 'encoding':'shift_jis'})      

# スライス
def slices(): 
    s = "01234"
    n = len(s) # 5
    x = n//2 # 2
    # 文字列、半分、奇数文字列、偶数文字列
    print( x, s[x:], s[:x], s[:x:], s[:-x:], s[-x:],  s[-x:][::-1]) 
    # 2 234 01 01 012 34 43
    
    l = [0, 1, 2, 3, 4]
    for i in range(len(l)):
        (l[:i] + l[i+1:])
    """
    [1, 2, 3, 4]
    [0, 2, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 2, 4]
    [0, 1, 2, 3]
    """

if None : passslices()

"""100×100の距離行列を生成します。乱数を使用して、
各距離を1から100の範囲でランダムに割り当てます。
対角要素は0に設定されています。"""
import random
def generate_distance_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(i+1, size):
            distance = random.randint(1, 100)
            matrix[i][j] = distance
            matrix[j][i] = distance

    return matrix
if None :
    size = 3
    distance_matrix = generate_distance_matrix(size) 
    # [[0, 25, 63], [25, 0, 17], [63, 17, 0]]

"""辞書内でvalueが最大の要素のkeyを取得する"""
def max_key():
    d = {'い': 1, 'ろ': 2, 'は': 3}

    print(max(d, key=d.get)) # は
if None : passmax_key() 

"""
2進数、8進数、16進数、そして10進数への変換
bin(), oct(), hex(), int()"""
def int_bin():
    
    num = 3 << 1 # 6 , 110 , ビット演算子
    binary = bin(num) # 0b110 
    binary_f = '{:b}'.format(num) # 110
    Logical_AND = (num >> 1) & 1 # 1 論理積 , Logical AND
    print(num, binary, binary_f, Logical_AND)
if None :   int_bin()

if __name__ == '__main__':   
    pass
    arr = [random.randint(1, 10) for i in range(4)] # 整数配列生成器 , [1, 9, 9, 4]
    for _ in range(3):
        arr = [random.randint(0, 10) for i in range(5)] # [0, 7, 4, 10, 3]
    