import ipapi
from flask import Flask, request, render_template
 
app = Flask(__name__)
 
@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('welcome.html')

@app.route('/index.html', methods = ['GET', 'POST'])
def ipAdd():
    search = request.form.get('search')
    data = ipapi.location(ip=search, output='json')
    return render_template('index.html', data=data)


 
if __name__ == "__main__":
    app.run(debug=True)