from flask import Flask, jsonify, request
from flask_cors import CORS
from email.message import EmailMessage
import ssl
import smtplib


app=Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorizations, true")
    response.headers.add("Access-Control-Allow-Methods", "GET, OPTIONS, POST, PATCH, DELETE")
    return response
    
@app.route('/', methods=['GET'])
def api_home():
    try:
        return {
            "success": True,
            "message": "Bienvenido"
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }, 500

@app.route('/correo', methods=['POST'])
def Correo():
        user = 'correo01321@gmail.com'
        app_password = 'fqhrnzgxfzfubacp'

        correo1 = request.json.get("correo")
        nombre1 = request.json.get("nombre")
        texto1 = request.json.get("texto")

        subject = 'Un nuevo usuario quiere contactarse contigo'
        content = "holaa, el usuario " + nombre1 + "lleno el formulario de la pagina web, su correo es: " + correo1 + ". \n el o ella te envia este mensaje: \n" + texto1

        em = EmailMessage()
        em['From'] = user
        em['To'] = "bazand25@gmail.com"
        em['Subject'] = subject
        em.set_content(content)

        context1 = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context1) as smtp:
            smtp.login(user,app_password)
            smtp.sendmail(user,"bazand25@gmail.com",em.as_string())
        return jsonify({
            'success': True,
            'message': 'se envio el correo'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
