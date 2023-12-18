from skimage import measure
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import numpy as np


def compute_ssim(image_path1, image_path2):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)
    image1_gray = image1.convert('L')
    image2_gray = image2.convert('L')
    image1_array = np.array(image1_gray)
    image2_array = np.array(image2_gray)
    ssim_index = ssim(image1_array, image2_array, data_range=image2_array.max() - image2_array.min())
    return ssim_index


IMAGE_PATH = 'House.tiff'
WHATERMARKED_IMAGE_PATH = 'host_image_with_whatermark.tif'
print(compute_ssim(IMAGE_PATH, WHATERMARKED_IMAGE_PATH))
