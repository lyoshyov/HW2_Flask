from flask import Flask, render_template
from flask import request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt')
def encrypt():
    """
    Encrypts an message
    """
    string_to_encrypt = request.args['string']
    if string_to_encrypt == '':
        return f'String is empty, input message for encrypt.'
    else:
        encoded_message = string_to_encrypt.encode()
        encrypted_message = f.encrypt(encoded_message).decode()
        return render_template(
            'index.html',
            result=encrypted_message, name_of_result='Encrypt result:'
        )   # result is result of encrypt, name_of_result is title, result name.



@app.route('/decrypt')
def decrypt():
    """
    Decrypts an encrypted message
    """
    string_to_decrypt = request.args['string']
    if string_to_decrypt == '':
        return f'String is empty, input encrypted message for decrypt.'
    else:
        decrypted_message = f.decrypt(bytes(string_to_decrypt, 'utf-8')).decode()
        return render_template(
            'index.html',
            result=decrypted_message, name_of_result='Decrypt result:'
        )   # result is result of decrypt, name_of_result is title, result name.


if __name__ == '__main__':
    app.run(debug=True)