from PIL import Image
from MD5 import indexes_of_blocks_for_watermark_embedding
from WHT import WHT, inverse_WHT
IMAGE_PATH = 'lena_std.tif'

host_image = Image.open(IMAGE_PATH)
pixels = host_image.load()
x, y = host_image.size
R = []
G = []
B = []

# разбиние сетки пикселей изображения на блоки 4х4 пикселя
for i in range(0, x, 4):
    # Проход по столбцам с шагом 4
    for j in range(0, y, 4):
        # Создание блока
        rblock = []
        gblock = []
        bblock = []
        # Проход по строкам блока
        for k in range(i, i + 4):
            rline = []
            gline = []
            bline = []
            # Проход по столбцам блока
            for l in range(j, j + 4):
                # Добавление элемента в блок
                rline.append(pixels[k, l][0])
                gline.append(pixels[k, l][1])
                bline.append(pixels[k, l][2])
            rblock.append(rline)
            gblock.append(gline)
            bblock.append(bline)
        # Добавление блока в список
        R.append(rblock.copy())
        G.append(gblock.copy())
        B.append(bblock.copy())

# определение порядка пикселей, путем применения алгоритма MD5
for i, n in enumerate(indexes_of_blocks_for_watermark_embedding):
    indexes_of_blocks_for_watermark_embedding[i] = [n//128, n % 128]


# Step 4 obtaining the frequency domain coefcient through  WHT
for i in range(len(R)):
    for j in range(len(R[0])):
        R[i][j] = WHT(R[i][j])
        G[i][j] = WHT(G[i][j])
        B[i][j] = WHT(B[i][j])

