# 一般的な九九表を作成する

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:4d}', end="") # 4行の幅で出力されるよう指定
    print("\n", end="")
