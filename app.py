om flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    phone_number = request.form['phone_number']
    url = 'https://cpp.bka.sh/external-services/referral/report/otp/request'
    
    response = requests.post(
        url,
        headers={'Content-Type': 'application/json'},
        data=json.dumps({'referrerWallet': phone_number})
    )
    
    if response.ok or (response.status_code == 400 and response.json().get('externalCode') == '6208'):
        result = 'Success'
    else:
        result = 'Failed'
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
