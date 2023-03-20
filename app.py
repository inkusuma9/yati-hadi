from flask import Flask, redirect, url_for, render_template, request, Response
from flask_assets import Bundle, Environment
from flask_mail import Mail
import smtplib


app = Flask(__name__)

js = Bundle('script.js', output='gen/main.js')

assets = Environment(app)

assets.register('main_js', js)

@app.route("/<nama>")
def home(nama):
    return render_template("index.html", content=nama)


@app.route('/form', methods=['POST'])
def form():
    name = request.form.get("name")
    ucapan = request.form.get("ucapan")
    kehadiran = request.form.get("kehadiran")
    nl = '\n'
    message = f'nama={name} {nl} ucapan={ucapan} {nl} kehadiran={kehadiran}'
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("inkusuma074@gmail.com", "gkjckurekvpgdade")
    server.sendmail("inkusuma074@gmail.com", "nur.hadi7428@gmail.com", message)
    return render_template("form.html")

if __name__ == "__main__":
    app.run()