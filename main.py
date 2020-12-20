from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from predict import dogcat

os.putenv('LANG', 'en_US.UTF-8')  #needed at time of deployment not in local
os.putenv('LC_ALL', 'en_US.UTF-8')

application = Flask(__name__)
CORS(application)  #to run inter http and https cros is cross origin


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg" # saving the input image from website in local folder
        self.classifier = dogcat(self.filename)


@application.route("/", methods=['GET'])  #back slash is by default added by web browser to get base template
@cross_origin()
def home():
    return render_template('index.html')


@application.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)


clApp = ClientApp()
# #port = int(os.getenv("PORT"))
if __name__ == "__main__":
    # clApp = ClientApp()
    # app.run(host='0.0.0.0', port=port)
    application.run(debug=True)
