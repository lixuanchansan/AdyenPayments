# AdyenPayments

curl https://checkout-test.adyen.com/v53/paymentMethods \
-H "x-API-key: AQEyhmfxLI/IbBZKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFihja6KR9b5EFAR0H0jGxRuEQwV1bDb7kfNy1WIxIIkxgBw==-TaV30ekCd9bVxvqjn/Enaf7Udh5r1ZG77dvt13opS+Q=-J;Q5y(=k8\*Eb6Zt2" \
-H "content-type: application/json" \
-d '{
"merchantAccount": "AdyenRecruitmentCOM",
"countryCode": "NL",
"amount": {
"currency": "EUR",
"value": 1000
},
"channel": "Web",
"shopperLocale": "nl-NL"
}'
