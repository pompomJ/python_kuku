# 一般的な九九表を作成する

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:4d}', end="")
    print("\n", end="")
