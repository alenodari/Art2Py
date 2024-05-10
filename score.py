from PIL import Image
# import torch
from torchvision.transforms import ToTensor
from piq import brisque
import os
from glob import glob
import numpy as np

def calculateBrisque(file):
    # Load the image
    image = Image.open(file)

    # Converte a imagem para um tensor PyTorch e adiciona uma dimensão de lote
    # image = torch.from_numpy(rgb888_image).permute(2, 0, 1).unsqueeze(0)
    # image_tensor = torch.tensor(image).permute(2, 0, 1)[None, ...] / 255.

    # Convert the PIL Image to a PyTorch tensor
    transform = ToTensor()
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Calcula a pontuação BRISQUE
    brisque_score = brisque(image_tensor)
    print(f"A pontuação BRISQUE da imagem é {brisque_score.item()}")

    return brisque_score.item()

# Executa na pasta
# Join folder_path and extension to create the search pattern
search_pattern = os.path.join("OV7670_Test2", "*.rgb")

# Use glob to get a list of files matching the pattern
files = glob(search_pattern)

# Initialize an array to store the results
results = np.zeros(len(files), dtype=float)

# Process each file
for i, file_path in enumerate(files):
    results[i] = calculateBrisque(file_path)

# Calculate average, median, and standard deviation
average_value = np.mean(results)
median_value = np.median(results)
std_deviation = np.std(results)

print(f"Average: {average_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")