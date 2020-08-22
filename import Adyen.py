import Adyen
from flask import Flask

app = Flask(__name__)




import Adyen

@app.route('/')
def get_payment_methods():
    adyen = Adyen.Adyen()
    adyen.client.xapikey = 'AQEyhmfxLI/IbBZKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFihja6KR9b5EFAR0H0jGxRuEQwV1bDb7kfNy1WIxIIkxgBw==-TaV30ekCd9bVxvqjn/Enaf7Udh5r1ZG77dvt13opS+Q=-J;Q5y(=k8*Eb6Zt2'
 
    request = {
        'merchantAccount': 'AdyenRecruitmentCOM'
    }
 
    response = adyen.checkout.payment_methods(request)
    print(response)




if __name__ == '__main__':

    app.run(debug=True)
    get_payment_methods()