from random import randint

for _ in range(10):
    escolhas_total = []
    for _ in range(100):
        numeros_escolhidos = []
        ranking = []
        escolhas = []
        for i in range(10000):
            num = randint(0, 10000)
            numeros_escolhidos.append(num)

        numeros_escolhidos.sort()

        for i in numeros_escolhidos:
            if i not in escolhas:
                escolhas.append(i)
                ranking.append((i, numeros_escolhidos.count(i)))

        ranking.sort(key=lambda num: num[1], reverse=True)

        escolhas_total.append(ranking[:1])

    escolhas_total.sort(key=lambda num: num[0][1], reverse=True)
    print(escolhas_total[:3])