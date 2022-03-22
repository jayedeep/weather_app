from flask import Flask,render_template,request,flash
import requests

app=Flask(__name__)
app.config['SECRET_KEY']='fa292b2d6f3c723b973bfd3a59ae10f2'

@app.route('/',methods=['GET','POST'])
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=76fbf61817ef12c85f9aee285351bef5'
    if request.method == 'POST':
        if request.form.get('search_city'):
            city=request.form.get('search_city')
            response = requests.get(url.format(city)).json()
            print(">>>>>>response\n\n\n\n",response)
            if response.get('cod') == 200:
                return render_template('index.html',response=response)
            else:
                flash(response.get('message'), 'danger')

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)