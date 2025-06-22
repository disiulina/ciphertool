from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        message = request.form.get('message', '')
        shift = request.form.get('shift', '')
        action = request.form.get('action', '')

        if message and shift and action:
            try:
                shift = int(shift)
                if action == 'encrypt':
                    result = caesar_encrypt(message, shift)
                elif action == 'decrypt':
                    result = caesar_decrypt(message, shift)
            except ValueError:
                result = "Shift must be a valid number."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)