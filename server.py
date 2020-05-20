from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(
            f'\n\nName:\t\t{name}, \nEmail:\t\t{email}, \nSubject:\t{subject}, \nMessage:\t{message}')
        return file


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route("/submit", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return 'OK'
        except:
            return "Message Not Saved!!"
    else:
        return "Message Not Submitted Please try again."
