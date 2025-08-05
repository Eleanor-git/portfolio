from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
csv_file = "./database.csv"


# file="./database.txt"
# def save_to_file(data):
#     with open(file, mode="a") as data_file:  # mode="a" stands for appending to the end of file
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"].replace("\n", "")
#         data_file.write(f"\n{email},{subject},{message}")

def save_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    with open(csv_file, mode='a', newline='') as database_csv:
        writer = csv.writer(database_csv,
                            delimiter=',',  # 分隔符號
                            quotechar='',
                            quoting=csv.QUOTE_NONE)

        writer.writerow([email, subject, message])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            save_to_csv(data)
            return redirect("./thankyou.html")
        except:
            return f"Unfortunately, the form was failed sending to the server, so please try again. Note! Do not use commons, and make a new line."
    else:
        return "Something went wrong! Try again"
