from PIL import Image
import numpy as np
from scipy.signal import correlate2d


def normalized_cross_coef(img1_path, img2_path):
    # Открыть изображения и преобразовать их в массивы NumPy
    img1 = np.array(Image.open(img1_path).convert('L'))
    img2 = np.array(Image.open(img2_path).convert('L'))
    mean1 = np.mean(img1)
    mean2 = np.mean(img2)
    dev1 = img1 - mean1
    dev2 = img2 - mean2
    norm1 = np.sqrt(np.sum(dev1 ** 2))
    norm2 = np.sqrt(np.sum(dev2 ** 2))
    nc = correlate2d(dev1, dev2, mode='valid') / (norm1 * norm2)
    return nc[0][0]


IMAGE_PATH = 'pizza.jpg'
WHATERMARKED_IMAGE_PATH = 'embedded_whatermark.tif'
print(normalized_cross_coef(IMAGE_PATH, WHATERMARKED_IMAGE_PATH))