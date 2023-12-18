from PIL import Image
from arnold_transformaton import arnold_transform
WATERMARTK_PATH = 'pixel_knight.jpg'
IMAGE_PATH = 'lena_std.tif'

# Step 1 Color watermark image preprocessing.
R = []
G = []
B = []
watermark = Image.open(WATERMARTK_PATH)
pixels = watermark.load()
x, y = watermark.size
for i in range(x):
    r = []
    g = []
    b = []
    for j in range(y):
        r.append(pixels[i, j][0])
        g.append(pixels[i, j][1])
        b.append(pixels[i, j][2])
    R.append(r)
    G.append(g)
    B.append(b)
print(R)
print(G)
print(B)

R_scrambled = R[:]
G_scrambled = G[:]
B_scrambled = B[:]

for i in range(len(R)):
    for j in range(len(R[0])):
        x, y = arnold_transform(i, j, [[1, 1], [1, 2]], 32)
        R_scrambled[x][y] = R[i][j]
        G_scrambled[x][y] = G[i][j]
        B_scrambled[x][y] = B[i][j]


R_bin = ''
G_bin = ''
B_bin = ''
for i in range(len(R)):
    for j in range(len(R[0])):
        R_bin += '0' * (8 - len(bin(R_scrambled[i][j])[2:])) + bin(R_scrambled[i][j])[2:]
        G_bin += '0' * (8 - len(bin(G_scrambled[i][j])[2:])) + bin(G_scrambled[i][j])[2:]
        B_bin += '0' * (8 - len(bin(B_scrambled[i][j])[2:])) + bin(B_scrambled[i][j])[2:]
print(R_bin)


#Step 2 Color host image preprocessing
