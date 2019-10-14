from flask import Flask, request, render_template
app = Flask(__name__, template_folder="templates")

from common import get_model, gen_rand_noise
from inference import generate_image


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        print("HELLLOODFKOSDKFOSDKFOSKDOF")
        print(request.form.get("x1", None))
        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

