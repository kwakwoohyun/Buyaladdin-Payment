from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return '''<script src="https://www.paypal.com/sdk/js?client-id=sb"></script>
<script>paypal.Buttons().render('body');</script>'''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
