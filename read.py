import matplotlib.pyplot as plt

def BF(price, length):
    count = [1]
    def bruteforce(price, length):
        if length <= 0:
            return 0
        max_length = float('-inf')
        for i in range(length):
            max_length = max(max_length, price[i] + bruteforce(price, length - (i + 1)))
            count[0] += 1
        return max_length
    
    return bruteforce(price, length),count[0]

def OT(price, length):
    c = [1]
    def DP(price, length):
        memo = [0] * (length + 1)

        for i in range(1, length + 1):
            max_val = float('-inf')
            for j in range(i):
                max_val = max(max_val, price[j] + memo[i - j - 1])
                c[0] += 1
            memo[i] = max_val

        return memo[length]
    
    return DP(price, length),c[0]

def GL(price, length):
    
    summ = 0
    count = 0
    while length > 0:
        max_value = 0
        max_length = 0
        for i in range(length):
            if price[i] > max_value and (i + 1) <= length:
                max_value = price[i]
                max_length = i + 1
            count += 1
        summ += price[max_length-1]
        length -= max_length

    return summ, count


price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30,
        31, 33, 33, 33, 36, 36, 36, 42, 44, 44,
        48, 48, 52, 60, 62, 62, 68, 70, 70, 70,
        74, 79, 82, 85, 88, 91, 94, 97, 100, 100,
        102, 110, 110, 116, 120, 124, 124, 132, 136, 140]
n_values = list(range(1, 51))
results_rod = []
results_dynamic = []
results_bottom_up = []

for n in range(1, 11):
    result_rod, c_rod = BF(price[:n], n)
    result_dynamic, c_dynamic = OT(price[:n], n)
    result_bottom_up, c_bottom_up = GL(price[:n], n)
    results_rod.append((n, result_rod, c_rod))
    results_dynamic.append((n, result_dynamic, c_dynamic))
    results_bottom_up.append((n, result_bottom_up, c_bottom_up))

# Extrair os valores para plotagem
n_values, max_values_rod, call_counts_rod = zip(*results_rod)
n_values, max_values_dynamic, call_counts_dynamic = zip(*results_dynamic)
n_values, max_values_bottom_up, call_counts_bottom_up = zip(*results_bottom_up)

    # Plotar os resultados
plt.figure(figsize=(12, 6))
plt.plot(n_values, max_values_rod, label='BF', marker='o')
plt.plot(n_values, max_values_dynamic, label='OT', marker='x')
plt.plot(n_values, max_values_bottom_up, label='GL', marker='s')
plt.xlabel('Comprimento da Haste (n)')
plt.ylabel('Valor Máximo')
plt.legend()
plt.grid(True)
plt.show()

    # Plotar os resultados
plt.figure(figsize=(12, 6))
plt.plot(n_values, call_counts_rod, label='BF', marker='o')
plt.plot(n_values, call_counts_dynamic, label='OT', marker='x')
plt.plot(n_values, call_counts_bottom_up, label='GL', marker='s')
plt.xlabel('Comprimento da Haste (n)')
plt.ylabel('Número de repetições')
plt.legend()
plt.grid(True)
plt.show()


    # Plotar os resultados
plt.figure(figsize=(12, 6))
plt.plot(n_values, call_counts_dynamic, label='OT', marker='x')
plt.plot(n_values, call_counts_bottom_up, label='GL', marker='s')
plt.xlabel('Comprimento da Haste (n)')
plt.ylabel('Número de repetições')
plt.legend()
plt.grid(True)
plt.show()

