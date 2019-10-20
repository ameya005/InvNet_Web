import io

import torch
import torch.nn as nn
from PIL import Image
from models import wgan_poly
# from google.cloud import storage

BATCH_SIZE = 16
DIM = 128
CATEGORY = 6
OUTPUT_DIM = DIM*DIM*CATEGORY

# def download_blob(bucket_name, source_blob_name, destination_file_name):
#     """Downloads a blob from the bucket."""
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket_name)
#     blob = bucket.blob(source_blob_name)
#
#     blob.download_to_filename(destination_file_name)
#
#     print('Blob {} downloaded to {}.'.format(
#         source_blob_name,
#         destination_file_name))


def gen_rand_noise():
    noise = torch.randn(BATCH_SIZE, DIM)
    noise = noise.cpu()

    return noise

def get_model():
    model = wgan_poly.GoodGenerator(dim=64, output_dim=OUTPUT_DIM, ctrl_dim=6)
    model.load_state_dict((torch.load('poly_weights.pt')))
    # checkpoint_path = './backend/poly_generator.pt'
    # download_blob(bucket_name="twocircle_generator", source_blob_name="two_circles_generator.pt",
    #               destination_file_name='./two_circles_generator.pt')
    # aG = torch.load(checkpoint_path, map_location='cpu')
    model.eval()

    return model
