from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/') #url on the browser
def my_home():
   return render_template('index.html')

@app.route('/<string:page_name>') #generic
def html_page(page_name):
   return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode = 'a') as db:
        email = data['email']
        subject = data['subject']
        msg = data['message']
        file_txt = db.write(f'\n {email},{subject},{msg}')

def write_to_csv(data):
    with open('database2.csv', newline='', mode = 'a') as db2:
        email = data['email']
        subject = data['subject']
        msg = data['message']
        file_csv = csv.writer(db2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        file_csv.writerow([email, subject, msg])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('Thankyou.html')
        except:
            print("not save to database!!!")
    else:
        return 'something went wrong'

