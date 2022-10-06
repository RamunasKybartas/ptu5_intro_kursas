import numpy as np



# for x in range(0, numpy_listas):
#     print(x)

# for x in range(0, numpy_listas):
#     print(x)


# def grazinam_pirminius(sarasas):
#     for skaicius in sarasas:
#         i = 0
#         for x in range(1, skaicius):
#             if skaicius%x == 0:
#                 i += 1
#         if i==1:
#             print(skaicius)
#         print("nepirminis")

# skaiciai = [x for x in range(0, 101)]
# # print(skaiciai)

# grazinam_pirminius(skaiciai)

matrica = np.random.randint(-5, 50, 100)
matrica = matrica.reshape(10, 10)

print(matrica[::2, ::2])
print("-" * 200)
print(matrica[:, 2])
print("-" * 200)
print(matrica > 30)
virs_30 = matrica[matrica>30]
print(virs_30)
print(matrica)
print(matrica[5:10, 5:10])

nauja_matrica = np.arange(0, 2022, 10)
print(nauja_matrica)
print(matrica)
print("-" * 200)
print(matrica[:3:, 4:10:2])
