from flask import Flask, render_template, request, redirect, url_for, flash, session
from textToSpeech import textToSpeech
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for using flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    file_path = None  # Initialize a variable to store the file path
    
    if request.method == 'POST':
        text = request.form.get('text')
        response = textToSpeech(text)
        
        if response:
            file_path = response  # Save the returned file path
            session['file_path'] = file_path.split('static\\')[1]
            flash(f"Audio file generated: {file_path}")  # Flash a success message
            
        
        return redirect(url_for('index'))  # Redirect after POST to avoid form resubmission
    
    file_path = session.get('file_path', None)

    if file_path:
        session.pop('file_path', None)
    return render_template('index.html', file_path=file_path)  # Pass file_path to the template

if __name__ == '__main__':
    app.run(debug=True)
