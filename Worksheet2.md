```py
import math, random, string

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True
```
# -------------------- Problem 1 --------------------
```py
L = [11, 12, 13, 14]
print("Problem 1:")
print("Initial L:", L)

L.extend([50, 60])
print("(i) After adding 50,60:", L)

for val in [11, 13]:
    if val in L:
        L.remove(val)
print("(ii) After removing 11,13:", L)

print("(iii) Sorted ascending:", sorted(L))
print("(iv) Sorted descending:", sorted(L, reverse=True))

print("(v) Search 13 present?:", 13 in L)
if 13 in L:
    print("    Index of 13:", L.index(13))

print("(vi) Number of elements:", len(L))
print("(vii) Sum of elements:", sum(L))
print("(viii) Sum odd numbers:", sum(x for x in L if x % 2 != 0))
print("(ix) Sum even numbers:", sum(x for x in L if x % 2 == 0))
print("(x) Sum primes:", sum(x for x in L if is_prime(x)))

L_clear = L.copy()
L_clear.clear()
print("(xi) After clearing:", L_clear)
# (xii) del L would delete the list object
```

# -------------------- Problem 2 --------------------
```py
def sum_list_no_builtin(lst):
    total = 0
    for item in lst:
        total += item
    return total

print("\nProblem 2:")
print("Sum without built-in:", sum_list_no_builtin([3, 5, 7, 9]))
```

# -------------------- Problem 3 --------------------
```py
def product_list_no_builtin(lst):
    prod = 1
    for item in lst:
        prod *= item
    return prod

print("\nProblem 3:")
print("Product without built-in:", product_list_no_builtin([2, 3, 4]))
```

# -------------------- Problem 4 --------------------
```py
arr_3d = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print("\nProblem 4: 3x4x6 array with '*' created.")
```
# -------------------- Problem 5 --------------------
```py
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print("\nProblem 5:")
D[8] = 8.8
print("(i) After add key=8:", D)
D.pop(2, None)
print("(ii) After remove key=2:", D)
print("(iii) Is key 6 present?:", 6 in D)
print("(iv) Count elements:", len(D))
print("(v) Sum values:", sum(D.values()))
D[3] = 7.1
print("(vi) Update key 3:", D)
D_copy = D.copy()
D_copy.clear()
print("(vii) After clear:", D_copy)
```
# -------------------- Problem 6 --------------------
```py
S1 = {10,20,30,40,50,60}
S2 = {40,50,60,70,80,90}
print("\nProblem 6:")
S1.update([55,66])
print("(i) After add 55,66:", S1)
S1.discard(10); S1.discard(30)
print("(ii) After remove 10,30:", S1)
print("(iii) Is 40 present?:", 40 in S1)
print("(iv) Union:", S1|S2)
print("(v) Intersection:", S1&S2)
print("(vi) S1 - S2:", S1-S2)
```
# -------------------- Problem 7 --------------------
```py
print("\nProblem 7:")
random.seed(0)
letters = string.ascii_letters
random_strings = [''.join(random.choice(letters) for _ in range(random.randint(6,8))) for _ in range(100)]
print("(i) First 10 random strings:", random_strings[:10])
primes_600_800 = [n for n in range(600,801) if is_prime(n)]
print("(ii) Primes 600-800:", primes_600_800)
div_by_7_9 = [n for n in range(100,1001) if n % 63 == 0]
print("(iii) Numbers 100-1000 divisible by 7 and 9:", div_by_7_9)
```
# -------------------- Problem 8 --------------------
```py
exam_st_date = (11,12,2025)
print("\nProblem 8:")
print("The examination will start from: {}/{}/{}".format(*exam_st_date))
```
# -------------------- Problem 9 --------------------
```py
given_nums = [5,12,15,20,33,40,55]
div_by_5 = [n for n in given_nums if n % 5 == 0]
print("\nProblem 9:")
print("Divisible by 5:", div_by_5)
```
# -------------------- Problem 10 --------------------
```py
def is_even(n):
    return n%2==0

print("\nProblem 10:")
print("7 ->", is_even(7))
print("8 ->", is_even(8))
```
# -------------------- Problem 11 --------------------
```py
def count_substring_overlapping(text, sub):
    count = 0
    start = 0
    while True:
        idx = text.find(sub, start)
        if idx == -1:
            break
        count += 1
        start = idx+1
    return count

text_example = "Emma is here. Emma loves Python. EmmaEmma"
print("\nProblem 11:")
print("Occurrences (overlap):", count_substring_overlapping(text_example, "Emma"))
```

# -------------------- Problem 12 --------------------
```py
list_a = [1,2,3,4,5,6,7]
list_b = [10,11,12,13,14,15]
new_list = [x for x in list_a if x%2!=0] + [x for x in list_b if x%2==0]
print("\nProblem 12: New list:", new_list)
```
# -------------------- Problem 13 --------------------
```py
positions = [(2,3),(4,5),(6,7),(7,8)]
positions_even = [p for p in positions if p[0]%2==0]
print("\nProblem 13: Positions with even x:", positions_even)
```
# -------------------- Problem 14 --------------------
```py
sensor_data = {1:2.3,2:4.5,3:1.8,4:3.6}
sensor_above3 = [sid for sid,val in sensor_data.items() if val>3]
print("\nProblem 14: Sensor IDs with >3:", sensor_above3)
```
# -------------------- Problem 15 --------------------
```py
commands_received = {"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
commands_executed = {"MOVE","TURN_LEFT","STOP"}
not_executed = commands_received - commands_executed
print("\nProblem 15: Commands not executed:", not_executed)
```
