import io

import torch
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms

BATCH_SIZE = 1
DIM = 128


def gen_rand_noise():
    noise = torch.randn(BATCH_SIZE, DIM)
    noise = noise.cpu()

    return noise

def get_model():
    checkpoint_path = './backend/two_circles_generator.pt'
    aG = torch.load(checkpoint_path, map_location='cpu')
    aG.eval()

    return aG
