from collections import deque

def transform(a, b):
    q = deque([(a, 0)])   # очередь: (число, шаги)
    used = {a: a}         # словарь для отметки посещённых и восстановления пути

    while q:
        x, d = q.popleft()   # достаём первый элемент из очереди

        # если дошли до цели
        if x == b:
            return d, used

        # все возможные переходы
        for nx in (x + 1, x - 1, x * 2, x // 2):
            if nx >= 0 and nx not in used:  # только положительные и непосещённые
                q.append((nx, d + 1))       # кладём в очередь
                used[nx] = x                # помним, откуда пришли

    return -1, used  # если не нашли
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

print(gcd_recursive(48, 18))  # 6


def binpow_iter(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:   # если n нечётное
            result *= a
        a *= a           # возводим основание в квадрат
        n //= 2          # делим показатель на 2
    return result

print(binpow_iter(2, 10))  # 1024