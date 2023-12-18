from PIL import Image
import math


def PSNR(IMAGE_PATH, WHATERMARKED_IMAGE_PATH):
    image = Image.open(IMAGE_PATH)
    image_pixels = image.load()
    whater_image = Image.open(WHATERMARKED_IMAGE_PATH)
    whater_image_pixels = whater_image.load()
    psnr = 0
    r_mse = 0
    g_mse = 0
    b_mse = 0
    r_max = -1
    g_max = -1
    b_max = -1
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r_mse += (image_pixels[i, j][0] - whater_image_pixels[i, j][0]) ** 2
            g_mse += (image_pixels[i, j][1] - whater_image_pixels[i, j][1]) ** 2
            b_mse += (image_pixels[i, j][2] - whater_image_pixels[i, j][2]) ** 2
            r_max = max(r_max, image_pixels[i, j][0])
            g_max = max(g_max, image_pixels[i, j][1])
            b_max = max(b_max, image_pixels[i, j][2])
    psnr = 10 * math.log10(
        (image.size[0] * image.size[1] * (r_max ** 2 + g_max ** 2 + b_max ** 2)) / (r_mse + g_mse + b_mse))
    return psnr


IMAGE_PATH = 'House.tiff'
WHATERMARKED_IMAGE_PATH = 'host_image_with_whatermark.tif'
print(PSNR(IMAGE_PATH, WHATERMARKED_IMAGE_PATH))
