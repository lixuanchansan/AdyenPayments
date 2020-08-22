import Adyen
from flask import Flask
import json 
app = Flask(__name__)
import json


@app.route('/paymentMethods')
def get_payment_methods():
    adyen = Adyen.Adyen()
    adyen.client.xapikey = 'AQEyhmfxLI/IbBZKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFihja6KR9b5EFAR0H0jGxRuEQwV1bDb7kfNy1WIxIIkxgBw==-TaV30ekCd9bVxvqjn/Enaf7Udh5r1ZG77dvt13opS+Q=-J;Q5y(=k8*Eb6Zt2'

    request = {
        "merchantAccount": "AdyenRecruitmentCOM",
        "countryCode": "NL",
        "amount": {
            "currency": "EUR",
            "value": 1000
        },
        "channel": "Web",
        "shopperLocale": "nl-NL"
    }
    response = adyen.checkout.payment_methods(request)
    response = response.message

    for paymentmtd in response['groups']:
        print(paymentmtd)    
        return response

    


if __name__ == '__main__':

    app.run(debug=True)
