# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_storage_app]
import logging
import os
import io
import time
import uuid
from PIL import Image
from flask import Flask, request, render_template
import inference
import inference_toy
from tempfile import NamedTemporaryFile
from matplotlib import pyplot as plt
# from google.cloud import storage
from vol_frac import cal_vol_fraction

app = Flask(__name__, template_folder="templates")
app.config['SEND_FILE_MAS_AGE_DEFAULT'] = 300
from common import get_model, gen_rand_noise

# Configure this environment variable via app.yaml
# CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

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



# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'GET':
#         return render_template('index.html', value='hi')
#     if request.method == 'POST':
#         # print("HELLLOODFKOSDKFOSDKFOSKDOF")
#
#         x1 = float(request.form.get('x1', None))
#         y1 = float(request.form.get('y1', None))
#         r1 = float(request.form.get('r1', None))
#         x2 = float(request.form.get('x2', None))
#         y2 = float(request.form.get('y2', None))
#         r2 = float(request.form.get('r2', None))
#
#         img = generate_image(x1/128, x2/128, y1/128, y2/128, 3.1415*r1*r1/128/128, 3.1415*r2*r2/128/128)
#
#         savebuffer = uuid.uuid4()
#         name = './static/' + str(savebuffer) + '.png'
#         plt.imsave(name, img, cmap='nipy_spectral')
#
#         return render_template('output.html', imgpath=name)


@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'GET':
#         return render_template('index.html', value='hi')
#     if request.method == 'POST':
#         # print("HELLLOODFKOSDKFOSDKFOSKDOF")
#
#         x1 = float(request.form.get('x1', None))
#         y1 = float(request.form.get('y1', None))
#         r1 = float(request.form.get('r1', None))
#         x2 = float(request.form.get('x2', None))
#         y2 = float(request.form.get('y2', None))
#         r2 = float(request.form.get('r2', None))
#
#         img = generate_image(x1, y1, r1, x2, y2, 0)
#
#         savebuffer = uuid.uuid4()
#         name = './static/' + str(savebuffer) + '.png'
#         plt.imsave(name, img, cmap='nipy_spectral')
#
#         return render_template('output.html', imgpath=name)

@app.route("/toyexample", methods=['GET', 'POST'])
def toyexample():
    if request.method == 'GET':
        return render_template('index_toy.html', value='hi')
    if request.method == 'POST':
        # print("HELLLOODFKOSDKFOSDKFOSKDOF")

        x1 = float(request.form.get('x1', None))
        y1 = float(request.form.get('y1', None))
        r1 = float(request.form.get('r1', None))
        x2 = float(request.form.get('x2', None))
        y2 = float(request.form.get('y2', None))
        r2 = float(request.form.get('r2', None))

        img = inference_toy.generate_image(x1 / 128, x2 / 128, y1 / 128, y2 / 128, 3.1415 * r1 * r1 / 128 / 128,
                             3.1415 * r2 * r2 / 128 / 128)

        fig = plt.figure(figsize=(12, 12))
        columns = 1
        rows = 1

        for i in range(1, columns*rows+1):
            image = img[i-1].squeeze(0).cpu().numpy()
            fig.add_subplot(rows, columns, i)
            plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9,
                                wspace=0.05, hspace=0.05)
            plt.imshow(image, cmap='binary')
            plt.axis('off')

        #print(img.shape)
        savebuffer = uuid.uuid4()
        name = './static/' + str(savebuffer) + '.png'
        #plt.imsave(name, img, cmap='nipy_spectral')
        plt.savefig(name, bbox_inches='tight', pad_inches=0)
        # return render_template('output.html', imgpath=name)
        return render_template("toyexample.html", imgpath=name)


@app.route("/polycrystalline", methods=['GET', 'POST'])
def polycrystalline():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        # print("HELLLOODFKOSDKFOSDKFOSKDOF")

        x1 = float(request.form.get('x1', None))
        y1 = float(request.form.get('y1', None))
        r1 = float(request.form.get('r1', None))
        x2 = float(request.form.get('x2', None))
        y2 = float(request.form.get('y2', None))
        # r2 = float(request.form.get('r2', None))

        img = inference.generate_image(x1, y1, r1, x2, y2, 0)
        vol_fraction = cal_vol_fraction(img)

        fig = plt.figure(figsize=(12, 12))
        columns = 1
        rows = 1

        for i in range(1, columns*rows+1):
           image = img[i-1].squeeze(0).cpu().numpy()
           fig.add_subplot(rows, columns, i)
           plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9,
                               wspace=0.05, hspace=0.05)
           plt.imshow(image, cmap='jet', vmin=-0.5, vmax=4.5)
           plt.axis('off')
        #plt.savefig('./images/Darpa_Appendix.png', bbox_inches='tight', pad_inches=0)
        savebuffer = uuid.uuid4()
        name = './static/' + str(savebuffer) + '.png'
        plt.savefig(name, bbox_inches='tight', pad_inches=0)

        # return render_template('output.html', imgpath=name)
        return render_template("polycrystalline.html", name=str(vol_fraction), imgpath=name)

# @app.route('/upload', methods=['POST'])
# def upload():
#     """Process the uploaded file and upload it to Google Cloud Storage."""
#     uploaded_file = request.files.get('file')
#
#     if not uploaded_file:
#         return 'No file uploaded.', 400
#
#     # Create a Cloud Storage client.
#     gcs = storage.Client()
#
#     # Get the bucket that the file will be uploaded to.
#     bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)
#
#     # Create a new blob and upload the file's content.
#     blob = bucket.blob(uploaded_file.filename)
#
#     blob.upload_from_string(
#         uploaded_file.read(),
#         content_type=uploaded_file.content_type
#     )
#
#     # The public URL can be used to directly access the uploaded file via HTTP.
#     return blob.public_url


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)
# [END gae_flex_storage_app]