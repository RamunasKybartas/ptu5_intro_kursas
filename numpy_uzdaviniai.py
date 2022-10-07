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

# matrica = np.random.randint(-5, 50, 100)
# matrica = matrica.reshape(10, 10)

# print(matrica[::2, ::2])
# print("-" * 200)
# print(matrica[:, 2])
# print("-" * 200)
# print(matrica > 30)
# virs_30 = matrica[matrica>30]
# print(virs_30)
# print(matrica)
# print(matrica[5:10, 5:10])

# nauja_matrica = np.arange(0, 2022, 10)
# print(nauja_matrica)
# print(matrica)
# print("-" * 200)
# print(matrica[:3:, 4:10:2])

# matricele = np.full((1, 5), 4)
# matricele = np.full((5, 5), 4)
# matricele2 = np.full_like(matricele, 3)
# print(matricele)
# print(matricele2)
# print(matricele2 * 2)
# matricele[2,2] = 9
# print(matricele)
bandomoji = np.full((5, 5), 3)
antrine = np.full((1,5), 5).astype(float)
print(bandomoji)
bandomoji[1:4, 1:4] = 3
bandomoji[2,0:5] = 2
bandomoji[0:, 2] = 2
print(np.sum(bandomoji.astype(float)))
print(np.vstack((bandomoji, antrine)))
print("-" * 150)
print(bandomoji)
# nauja = np.array([x*50 for x in bandomoji if x==1])
print("-" * 150)
print(bandomoji[bandomoji > 1])


skaiciai = [2,5,8,9,6,7]
f = 1
skaicius = 5
listas = f*2 if skaicius in skaiciai else f*3
print(f"gavosi: {listas}")