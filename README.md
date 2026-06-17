To create a fresh repository on GitHub with the complete code for your Flask SMS app, I'll provide you with all the necessary files and their contents. You can copy this code into your local files and push it to GitHub.

### Project Structure

1. **Create a folder for your project**. You can name it `flask_sms_app` or any name you prefer.

### File Contents

#### 1. `app.py`

Create a file named `app.py` and add the following code:

```python
from flask import Flask, request, render_template
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
```

#### 2. `requirements.txt`

Create a file named `requirements.txt` and add the following lines:

```
Flask==2.0.3
requests==2.26.0
```

#### 3. Create a `templates` Directory

#### 3.1: `index.html`

Inside the `templates` directory, create a file named `index.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Send SMS</title>
</head>
<body>
    <h1>Send SMS</h1>
    <form action="/send_sms" method="POST">
        <label for="phone_number">Phone Number:</label>
        <input type="text" name="phone_number" required>
        <br>
        <button type="submit">Send SMS</button>
    </form>
</body>
</html>
```

#### 3.2: `result.html`

Inside the same `templates` directory, create a file named `result.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
</head>
<body>
    <h1>Result</h1>
    <p>{{ result }}</p>
    <a href="/">Back</a>
</body>
</html>
```

### Step-by-Step to Push to GitHub

1. **Initialize a Git Repository**:
   Open your terminal and navigate to your project directory:
   ```bash
   cd path/to/flask_sms_app
   git init
   ```

2. **Add Files**:
   ```bash
   git add .
   ```

3. **Commit Your Changes**:
   ```bash
   git commit -m "Initial commit of Flask SMS app"
   ```

4. **Create a GitHub Repository**:
   Go to [GitHub](https://github.com), sign in, and create a new repository. Name it `flask_sms_app`.

5. **Link Your Local Repository to GitHub**:
   ```bash
   git remote add origin https://github.com/yourusername/flask_sms_app.git
   ```

6. **Push Your Code**:
   ```bash
   git push -u origin main
   ```

### Conclusion

You now have the complete code for your Flask SMS app and instructions on how to push it to GitHub. If you need further assistance or run into any issues, just let me know!
