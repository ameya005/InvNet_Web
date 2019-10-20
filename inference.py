import torch
import numpy as np
from common import get_model, gen_rand_noise

from matplotlib import pyplot as plt
from models import wgan_poly
from torch.utils.data import Dataset

BATCH_SIZE = 4
DIM = 128
CHANNEL = 6

def generate_image(x1, y1, r1, x2, y2, r2):
    aG = get_model()

    lv = torch.FloatTensor([x1, y1, r1, x2, y2, r2]).repeat(BATCH_SIZE, 1)
    summation = torch.sum(lv, dim=1).unsqueeze(1)
    lv = lv / summation
    lv = lv.cpu()

    gen_images = aG(gen_rand_noise(), lv)
    gen_images = torch.argmax(gen_images.view(BATCH_SIZE, CHANNEL, DIM, DIM), dim=1).unsqueeze(1)
    gen_images = gen_images.int()

    del aG
    # gen_images = aG(gen_rand_noise(), lv).view(BATCH_SIZE, CHANNEL, DIM, DIM)
    # image = gen_images.detach().numpy()
    # image = np.argmax(image, axis=1)
    return gen_images
