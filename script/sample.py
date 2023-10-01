import itertools
import random

def three_sum(nums):  # 順列 : sequence
    # デカルト積==直積==カルデシアン積==itertools.product()
    lt = [ tuple(sorted(t)) for t in list(itertools.permutations(nums, 3)) if sum(t) == 0 ]
    ll = [ list(l) for l in set(lt)]
   
    return ll

if None:
    (three_sum([-1, 0, 1, 2, -1, -4]))

import numpy as np
def x(ll):
    return ll
def max_product(n):
    lt = list(itertools.combinations([i for i in range(1,11)], 3))
    ([t for t in lt if sum(t) == 12])
    d = { t: np.prod(t) for t in lt if sum(t) == 12 }
    ll = [ list(t) for t,v in d.items() if np.prod(t) == max(d.values()) ]
    return x(*ll)

if None:
    n = 15
    (max_product(n))

import itertools
import numpy as np

def max_product(n):
    lt = list(itertools.combinations([i for i in range(1,11)], 3))
    d = {t: np.prod(t) for t in lt if sum(t) == n}
    ll = [list(t) for t,v in d.items() if np.prod(t) == max(d.values())]
    return ll
if None:
    n = 12
    (max_product(n))

def longest_substring(s):
    d = {}
    for i in range(len(s)):
        S = ""
        for el in s[i:]:
            S += el
            
            conditions1 = any(map(str.isdigit, S)) 
            conditions1 = list(map(str.isdigit, S)).count(True) >=3
            conditions2 = any(map(str.isupper, S)) 
            conditions2 = list(map(str.isupper, S)).count(True) >=2
            conditions3 = any(map(str.islower, S))
            conditions3 = list(map(str.islower, S)).count(True) >=3
            conditions4 = len(S) >= 3
            if conditions1 and conditions2 and conditions3 and conditions4:
                ( i, S)
                d = { **d,**{S:len(S)}}
                break
    (list(map(str.isupper, s)).count(True) >=2)
    x =  min(d.values())
    l = [ k for k, v in d.items() if v == x ]
    ( d.keys())
    ( l, ''.join(l))
    return ''.join(l)

if None:
    s = "abc1Defg23Hijk"
    longest_substring(s) # "1Defg23"

def map_func(s):
    l = [ '文字列に数字が含まれているか？', any(map(str.isdigit, s)) ,
    '文字列に数字が何個含まれているか？',list(map(str.isdigit, s)).count(True) ,
    '文字列に大文字が何個含まれているか？',list(map(str.isupper, s)).count(True) ,
    '文字列に小文字が何個含まれているか？',list(map(str.islower, s)).count(True) ]

    return ' '.join([ '\n' + i if type(i) is str else str(i) for i in l ])

if None:(map_func("abc1Defg23Hijk"))

def two_text( s1 , s2 ):
    l1, l2 = list(s1),list(s2)
    s__ = set(l1) - set(l2) # 差集合
    l1 = [ i for i in l1 if i not in s__ ]
    for i in range(len(l2)):
        if not bool( l1[i] == l2[i] ) :
            try :
                ( l1[i], l2[i], l1.index(l2[i]) )
                p = l1.index(l2[i])
                l1.insert( i, l1.pop(p))
            except:
                return
    c = abs(len(l1) - len(l2))
    l1 = l1[:len(l2)] # 
    return ''.join(l1)
if None:    (two_text('nxppi','pin'))

def can_convert(s1: str, s2: str) -> bool:
    l1, l2 = list(s1),list(s2)
    
    for i in range(len(l2)):
        x, y = l1[i], l2[i] 
        if x != y :
            del l1[i]
            break
    if l1 == l2:
        return True
    elif l1[:-1] == l2:
        return True
    elif l1 != l2:
        return False
    
def can_convert__(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    for i in range(len(s2)):
        if s1[i] != s2[i]:
            return s1[i+1:] == s2[i:]

    return True
if None :   (can_convert("abed", "abde") )

def remove_duplicates(nums: list) -> list:

    s__ = set(nums) 
    d = { i:None for i in nums}
    (list(d))
    return list(d)
if None :   (remove_duplicates([5, 2, 6, 1, 5, 8, 6, 2, 9, 0]))

def count_triangles(nums) -> int:
    lt = list(itertools.combinations(nums, 3))
    ll = [ [ a, b, c ]  for a, b, c in lt if  [ a < b + c, b < a + c, c < a + b ]==[True,True,True] ]
    (lt, ll, len(ll))
    return len(ll)

def count_combinations(nums, k: int, m: int) -> int:
    st = set(itertools.combinations(nums, k))
    l = [ t for t in st if sum(t)==m ]
    return len(l)
if None :   (count_combinations( [1, 2, 3, 4, 5], 3, 6))

def max_product_of_three(nums: list) -> int:
    import numpy as np    
    st = set(itertools.combinations(nums, 3))
    l = []
    for t in st:
        x = np.array(t)
        # 総積
        n = np.prod(x,axis = 0) # axis:縦軸
        l.append(n)
    return max(l)

if None:(max_product_of_three( [-10, -10, 5, 2]))

def longest_palindrome_(s: str):
    l=[]
    for i in range(len(s)-1):
        for j in range(1,len(s) +1 -i):
            line= s[ i: i+j]
            print( i, j, line)
            re_line =line[::-1]
            if line == re_line:
                l.append(line)
    [ s[ i: i+j] for i in range(len(s)-1) for j in range(1,len(s) +1 -i) if s[ i: i+j] ==s[ i: i+j][::-1]]
    return max(l)


# 回文判定
def palindrome(s: str) -> str:
    n = len(s)
    x = n//2
    print(x, s[:x:], s[-x:],  s[-x:][::-1])
    if s[:x:] == s[-x:][::-1]:
        return True
    else :
        return False
if None :    passprint(palindrome("level"))

# FizzBuzz
def FizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5==0:
            print(i,'FizzBuzz')
        elif i % 3 ==0:
            print(i,'Fizz')
        elif i % 5 ==0:
            print(i,'Buzz')
        else:
            print(i)
if None:    FizzBuzz()

# フィボナッチ数列
def Fibonacci_number(i): # 0,1,1,2,3,5,8,13,21,34,55,89,144,233
    n = 10**i
    l = [ 0 , 1 ]
    for _ in range(n):
        l.append( l[-2] + l[-1])
        (l)
        last = l[-1]
        if len(str(last)) >=2 and str(last)[0]== '1' and str(last)[1]== '1' :
            print(str(last), str(last)[:i])
            return int(str(last)[:i])

if None:   (Fibonacci_number(5))

# 最大公約数
def max_common_divisor(n1,n2):
    l=[]
    for i in range(1,n1+1 if n1<n2 else n2+1) :
        if n1 % i == 0 and n2 % i== 0:
            l.append(i)
    return max(l)
if None:    max_common_divisor(10,100)

# 素数判定
def is_prime(n):
    import math
    (math.sqrt(n),int(math.sqrt(n)) )
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        (i)
        if n % i == 0:
            (i)
    l = [ i for i in range(2,n) if n%i == 0]
    if n == 1 :
        b = False
    elif len(l) == 0:
        b = True
    else:
        b = False
    return b
if None:    (is_prime(49))

# 反復アルゴリズムを
def fib(n): # 0,1,1,2,3,5,8,13,21,34,55,89,144,233
    # 初期化
    a, b = 0, 1
    l = []
    while len(l) <= n :
        l.append(a)
        c = a + b
        a = b
        b = c

    return l[n]
if None :     fib(10)

# n番目のフィボナッチ数を求める関数
def fibonacci(n: int) -> int: # 0,1,1,2,3,5,8,13,21,34,55,89,144,233
    l = [0,1]
    for _ in range(n):
        l.append(l[0] + l[-1])
        l = l[1:]
    return l[0]
    
if None :   fibonacci(13)

"""問題:Python 3.7を使用して、再帰アルゴリズムを使って、フィボナッチ数列の第n項を計算する関数 """
class Re1: # recursion:再帰
    def r(n, a, b):
        if n == 1:
            return a
        if n == 2:
            return b
        return Re1.r(n-1, b, a + b)

    def fibonacci(n):
        a, b = 1, 1
        x = Re1.r(n, a, b)
        return x
if None :       (M25.fibonacci(10))
"""問題:Python 3.7を使用して、再帰アルゴリズムを使って、
与えられた整数 n の累乗和（1からnまでの累乗の和）を計算する関数
sum_of_powers(n) を作成してください。
累乗和とは、1から与えられた正の整数までの各整数の累乗の和です。例えば、n = 4 の場合、
累乗和は 1^1 + 2^2 + 3^3 + 4^4 となります。"""
class Re2: # recursion:再帰
    def p(n, i):
        if n == 1:
            return i + n**n
        (n)
        i += n**n
        (i)
        return Re2.p(n-1, i)
    
    def sum_of_powers(n):
        i = 0
        x = Re2.p(n,i)
        return x
if None :   (Re2.sum_of_powers(4))


# 分割統治法 【divide and conquer algorithm】
"""マージソートは、分割統治法を用いた高速なソートアルゴリズムの一種です。
リストを半分に分割し、分割したリストを再帰的にソートしてから、
それらをマージしてソートされたリストを作成します。"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr) // 2
    L = arr[:n]
    R = arr[n:]
    L = merge_sort(L)
    R = merge_sort(R) 
    return merge(L,R)

def merge(L, R):
    lis = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            lis.append(L[i])
            i += 1
        else:
            lis.append(R[j])
            j += 1
    lis += L[i:]
    lis += R[j:]
    return lis

if None :
    arr = [random.randint(1, 10) for i in range(4)] # 整数配列生成器
    arr = list('cwodq8rw')
    arr = [5, -12, 17, -20, 25, -33, 40]
    arr = [ 1, 2, 3, 4, 5 ] # , 6, 7, 8, 9, 10
    ( merge_sort(arr))


"""
以下は、openAIでプログラマーとして勤務するために必要なレベルのアルゴリズム問題の例です。
問題：
配列に含まれる数値の中から、最大値と最小値を見つける関数を実装してください。
ただし、配列には重複する数値が含まれる可能性があります。また、配列の長さは1以上とします。

入力例：[3, 2, 5, 1, 4]
出力例：最大値: 5 最小値: 1
"""
def find_max_min(arr):
    max_val, min_val = arr[0], arr[0]
    (max_val)
    for i in arr:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val =i
    (max_val, min_val)

    return max_val, min_val
if None :
    arr = [3, 2, 5, 7, 4, 9]
    max_val, min_val = find_max_min(arr)
    print("最大値: ", max_val, "最小値: ", min_val)

"""問題: 与えられた整数リストをマージソートを使用して降順にソートし、各要素がそのリストで何回繰り返されるかを計算するPythonプログラムを作成してください。
例:
入力: [7, 4, 1, 4, 2, 7, 9, 2, 7]

出力:
降順にソートされたリスト: [9, 7, 7, 7, 4, 4, 2, 2, 1]
要素の出現回数:
1 - 1回
2 - 2回
4 - 2回
7 - 3回
9 - 1回

注意:

リスト内の要素は整数とします。
入力リストは既に与えられているものとします。入力の取得は不要です。
"""
class reverse:
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        n = len(arr) // 2
        L = arr[:n]
        R = arr[n:]
        
        L = merge_sort(L)[::-1]
        R = merge_sort(R)[::-1]
        return reverse.merge(L,R)

    def merge(L, R):
        lis = []
        i = 0
        j = 0
        while i < len(L) and j < len(R):
            if L[i] >= R[j]:
                lis.append(L[i])
                i += 1
            else:
                lis.append(R[j])
                j += 1
        lis += L[i:]
        lis += R[j:]
        return lis
    def count_elements(sorted_arr):
        d ={}
        for i in sorted_arr:
            d.setdefault(i,0)
            d[i] += 1
        print(d)
        return d

if None :
    arr = [ 1, 3, 2, 4, 5, 2] # 6, 7, 8, , 9, 10
    sorted_arr = reverse.merge_sort(arr)
    element_counts = reverse.count_elements(sorted_arr)

    ("降順にソートされたリスト:", sorted_arr)
    ("要素の出現回数:")
    for key, value in element_counts.items():
        (f"{key} - {value}回")

"""Python 3.7でユークリッドの互除法を実装したサンプルコード"""

def gcd(a, b): # 最大公約数、再帰
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if None :
    (gcd(24, 36)) # 12
    (gcd(12, 8))  # 4

def lcm(a, b):
    # 最小公倍数を求めるために、最大公約数を先に求める
    gcd_value = gcd(a, b)
    
    # 最大公約数を使用して、最小公倍数を求める
    lcm_value = (a * b) // gcd_value
    
    return lcm_value    

if None :   (lcm(12, 18)) # 36

"""ダイクストラ法を実装したサンプルコード
ダイクストラ法とはグラフ上のある地点を始点とする最短経路を求めるためのアルゴリズム"""
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# 使用例

if None :
    graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'D': 4, 'E': 6},
    'C': {'A': 2, 'F': 7},
    'D': {'B': 4},
    'E': {'B': 6, 'F': 1},
    'F': {'C': 7, 'E': 1},
    }
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    (distances) # {'A': 0, 'B': 3, 'C': 2, 'D': 7, 'E': 9, 'F': 8}

"""問題: 与えられた整数リストをマージソートを使用して昇順にソートし、
各要素がそのリストで何回繰り返されるかを計算するPythonプログラムを作成してください。
ただし、マージソートの実装では再帰を使わず、イテレーティブなアプローチを使用してください。
例:
入力: [7, 4, 1, 4, 2, 7, 9, 2, 7]

出力:
昇順にソートされたリスト: [1, 2, 2, 4, 4, 7, 7, 7, 9]
要素の出現回数:
1 - 1回
2 - 2回
4 - 2回
7 - 3回
9 - 1回"""

class ascending: # Ascending:昇順 Descending:降順
    def merge_sort(arr):
        #
        l = []
        for i, E in enumerate(arr):
            if l==[]:
                l.append(E)
            m = []
            for j, e in enumerate(l[::-1]):
                if i==0 :
                    break
                l_ = [ i for i, k in enumerate(l) if k > E]
                if l_ == []:
                    l.append(E)
                    break
                else:
                    l.insert(l_[0],E)
                    break
        n = len(arr) // 2
        left = l[:n]
        right = l[n:]
        # 
        if len(arr) <= 1:
            return arr
        n = len(arr) // 2
        L = arr[:n]
        R = arr[n:]
        left = l[:n]
        right = l[n:]
        
        L = merge_sort(L)
        R = merge_sort(R)
        (L,left,R,right,L==left,R==right)
        return ascending.merge(L,R)

    def merge(L, R):
        (L,R)
        lis = []
        i = 0
        j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lis.append(L[i])
                i += 1
            else:
                lis.append(R[j])
                j += 1
        lis += L[i:]
        lis += R[j:]
        return lis
    def count_elements(sorted_arr):
        d ={}
        for i in sorted_arr:
            d.setdefault(i,0)
            d[i] += 1
        return d

if None : 
    arr = [4, 5, 3, 1, 2,  6, ] # , 7, 8, 9, 10 
    arr = [random.randint(1, 10) for i in range(14)]
    sorted_arr = ascending.merge_sort(arr)
    (set(arr)==set(sorted_arr))
    element_counts = ascending.count_elements(sorted_arr)

    ("降順にソートされたリスト:", sorted_arr)
    ("要素の出現回数:")
    for key, value in element_counts.items():
        (f"{key} - {value}回")
"""
問題:再帰アルゴリズムを使って、整数 n の階乗を計算する関数を作成してください。
階乗とは、1から与えられた正の整数までの連続した整数の積であり、n! と表記されます。
例: 5!  5 * 4 * 3 * 2 * 1 = 120 。
以下の条件に注意してください：
n は正の整数であると仮定します。
n が 0 の場合、答えは 1 です。
ヒント：再帰アルゴリズムの基本的な考え方は、自分自身を呼び出す関数を作成することです。
ただし、無限ループを避けるために、基本ケース（最も単純な問題）を定義することが重要です。
この問題では、基本ケースは n が 1 または 0 の場合です。"""

def factorial(n): # 階乗
    if n == 0 or n == 1: # 
        return 1
    else:
        return n * factorial(n-1)

if None :     passprint(factorial(4))
"""再帰アルゴリズム
1からnまでの合計を計算します。"""
def recursive_sum(n):
    if n == 1 :
        return n
    return n + recursive_sum(n-1)
if None :     passrecursive_sum(3)
"""ただし、この関数はスタックオーバーフローを引き起こす可能性があります。
大きなnの値に対して呼び出すと、再帰呼び出しの深さが増え、
Pythonの最大再帰深度を超える可能性があります。
その場合、sys.setrecursionlimit()を使用して最大再帰深度を増やすか、
反復アルゴリズムを使用することを検討してください。"""

"""問題:再帰アルゴリズムを使って、リスト内の整数の合計を計算する関数を作成してください。"""
def recursive_sum(l):
    if len(l) == 1 :
        return l[0]
    x = l.pop(-2) + l.pop(-1)
    l.append(x)
    return recursive_sum(l)

if None :   (recursive_sum([1,2,3,4,5]))

"""問題：与えられたリスト内の文字列を逆順に出力する関数を作成してください。

入力例： ["apple", "banana", "cherry", "date", "fig"]
出力例： fig date cherry banana apple   """
def print_strings_reverse(l):
    if len(l) == 0:
        return l
    else:
        print(l[-1]) 
        return print_strings_reverse(l[:-1])

if None :   print_strings_reverse(["apple", "banana", "cherry", "date", "fig"])

"""問題：再帰アルゴリズムを使って、与えられた正の整数 n に対して、
1から n までの奇数を出力する関数を作成してください。
入力例： 7
出力例： 1 3 5 7    """
def print_odds(n):

    if n == 0:
        return n
    else :
        if n % 2 == 1 : print(n) 
        print_odds(n-1)
if None :   print_odds(7)