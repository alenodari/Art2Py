import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
from glob import glob

def pixel_rgb565_to_rgb888(byte1, byte2):
    rgb565 = (byte1 << 8) | byte2
    red = ((rgb565 >> 11) & 0x1F) * 255 / 31
    green = ((rgb565 >> 5) & 0x3F) * 255 / 63
    blue = (rgb565 & 0x1F) * 255 / 31
    return int(red), int(green), int(blue)

def image_rgb565_to_rgb888(rgb565_data, width, height):
    rgb888_data = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(0, len(rgb565_data), 2):
        row = (i // 2) // width
        col = (i // 2) % width
        r, g, b = pixel_rgb565_to_rgb888(rgb565_data[i], rgb565_data[i + 1])
        rgb888_data[row, col] = [r, g, b]

    return Image.fromarray(rgb888_data, 'RGB')

def file_rgb565_to_rgb888(input_file, output_file, width, height):
    with open(input_file, 'rb') as file:
        rgb565_data = file.read(width * height * 2)

    image = image_rgb565_to_rgb888(rgb565_data, width, height)
    image.save(output_file)

    # Desenha a imagem
    # plt.figure(figsize=(640, 480))
    # plt.imshow(image)
    # plt.axis("off")
    # plt.show(block=True)

# input_file_path = 'OV7670_640_480/image01.565'
# output_file_path = 'OV7670_640_480/image01.rgb'
width, height = 640, 480

# # Executa sem salvar a imagem
# with open(input_file_path, 'rb') as file:
#     rgb565_data = file.read(width * height * 2)

# image = image_rgb565_to_rgb888(rgb565_data, width, height)

# Executa salvando a imagem
# file_rgb565_to_rgb888(input_file_path, output_file_path, width, height)

# Executa na pasta
# Join folder_path and extension to create the search pattern
search_pattern = os.path.join("OV2640_Test2", "*.565")

# Use glob to get a list of files matching the pattern
files = glob(search_pattern)

# Process each file
for file_path in files:
    file_rgb565_to_rgb888(file_path, os.path.splitext(file_path)[0] + ".rgb", width, height)