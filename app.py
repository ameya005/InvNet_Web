import io

from PIL import Image
from flask import Flask, request, render_template
from inference import generate_image
from tempfile import NamedTemporaryFile
from matplotlib import pyplot as plt

app = Flask(__name__, template_folder="templates")
app.config['SEND_FILE_MAS_AGE_DEFAULT'] = 300
from common import get_model, gen_rand_noise
from inference import generate_image

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        # print("HELLLOODFKOSDKFOSDKFOSKDOF")

        x1 = float(request.form.get('x1', None))
        y1 = float(request.form.get('y1', None))
        r1 = float(request.form.get('r1', None))
        x2 = float(request.form.get('x2', None))
        y2 = float(request.form.get('y2', None))
        r2 = float(request.form.get('r2', None))

        #print(type(x1))
        # img = generate_image(x1,y1,r1,x2,y2,r2)[0,...]
        img = generate_image(x1/128, x2/128, y1/128, y2/128, 3.1415*r1*r1/128/128, 3.1415*r2*r2/128/128)

        #plt.imshow(img, cmap='jet')
        #plt.show()
        #f = NamedTemporaryFile(suffix='.png')
        #name = f.name
        name = './static/genimg.png'
        plt.imsave(name, img, cmap='nipy_spectral')
        return render_template('output.html', imgpath=name)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)


