from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import PyPDF2
import csv
from datetime import datetime

# -------------------- APP SETUP --------------------
app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# -------------------- DUMMY USERS --------------------
students = {
    "student1": "123"
}

faculty_users = {
    "faculty1": "123"
}

# -------------------- HOME PAGE --------------------
@app.route('/')
def home():
    return render_template('home.html')

# -------------------- LOGIN PAGE --------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Student Login
        if role == "student":
            if username in students and students[username] == password:
                return redirect(url_for('student'))

        # Faculty Login
        elif role == "faculty":
            if username in faculty_users and faculty_users[username] == password:
                return redirect(url_for('faculty_page'))

        return "<h3>Invalid Login Details!</h3><a href='/login'>Try Again</a>"

    return render_template('login.html')

# -------------------- STUDENT PAGE --------------------
@app.route('/student')
def student():
    return render_template('upload.html')

# -------------------- FACULTY PAGE --------------------
@app.route('/faculty')
def faculty_page():
    return render_template('attendance.html')

# -------------------- PDF TEXT EXTRACTION --------------------
def extract_text_from_pdf(filepath):
    text = ""
    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# -------------------- LOCAL AI EVALUATION --------------------
def evaluate_assignment(text):

    words = text.split()
    word_count = len(words)

    sentences = text.split('.')
    sentence_count = len(sentences)

    avg_sentence_length = word_count / sentence_count if sentence_count != 0 else 0

    score = 5

    if word_count > 300:
        score += 1
    if word_count > 600:
        score += 1
    if avg_sentence_length > 12:
        score += 1
    if avg_sentence_length > 18:
        score += 1

    if score > 10:
        score = 10

    feedback = f"""
Assignment Evaluation Report

Summary:
The assignment contains approximately {word_count} words and {sentence_count} sentences.

Strengths:
• Demonstrates effort in writing
• Basic explanation of the topic is present
• Readable sentence structure

Weaknesses:
• Some areas lack deep explanation
• Technical clarity can be improved
• Paragraph organization needs improvement

Suggestions:
• Add more examples and diagrams
• Improve introduction and conclusion
• Use more technical terms

Final Score: {score}/10
"""

    return feedback

# -------------------- UPLOAD + EVALUATION --------------------
@app.route('/upload', methods=['POST'])
def upload():

    if 'assignment' not in request.files:
        return "No file uploaded"

    file = request.files['assignment']

    if file.filename == '':
        return "No selected file"

    # Save file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Extract text
    text = extract_text_from_pdf(filepath)

    if len(text.strip()) == 0:
        return "Could not read text from the PDF."

    feedback = evaluate_assignment(text)

    return render_template('result.html', feedback=feedback)

# -------------------- MARK ATTENDANCE --------------------
@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():

    date = datetime.now().strftime("%Y-%m-%d")

    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        for student in request.form:
            status = request.form[student]
            writer.writerow([date, student, status])

    return """
    <h2>Attendance Saved Successfully!</h2>
    <br>
    <a href='/faculty'><button>Back to Faculty Page</button></a>
    """

# -------------------- RUN SERVER --------------------
if __name__ == '__main__':
    app.run(debug=True)
