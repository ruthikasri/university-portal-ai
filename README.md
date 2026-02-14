# 🎓 University Portal AI

An AI-powered academic management web application that automates student assignment evaluation and faculty attendance tracking.

## 📌 Problem Statement

In most colleges, faculty members manually check assignments and maintain attendance records.
This process is time-consuming, error-prone, and delays feedback to students.

This project provides a centralized web portal that digitizes academic management and introduces automated assignment evaluation.

---

## 🚀 Features

### 👩‍🎓 Student Module

* Secure login system
* Upload assignment (PDF)
* Automatic text extraction
* Instant evaluation feedback
* Score generation (out of 10)

### 👩‍🏫 Faculty Module

* Faculty authentication
* Mark student attendance (Present/Absent)
* Automatic date recording
* Persistent attendance storage

### 🤖 Automated Evaluation Engine

* Reads uploaded PDF files
* Analyzes word count & sentence structure
* Generates:

  * Summary
  * Strengths
  * Weaknesses
  * Suggestions
  * Final score

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python Flask
* **File Processing:** PyPDF2
* **Data Storage:** CSV (lightweight database)
* **Version Control:** Git & GitHub

---

## ⚙️ How It Works (Architecture)

1. User accesses the portal through a browser.
2. Flask backend handles authentication and routing.
3. Students upload assignments → server extracts text.
4. Evaluation engine analyzes the content and generates feedback.
5. Faculty marks attendance → data stored persistently.

---

## 📂 Project Structure

```
university-portal-ai/
│
├── app.py
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── upload.html
│   ├── result.html
│   └── attendance.html
│
├── static/
│   └── style.css
```

---

## 🔮 Future Improvements

* Integration with MySQL database
* Real AI/LLM model integration
* Plagiarism detection
* Student performance analytics dashboard
* ERP system integration

---

## 👩‍💻 Author

**Ruthika Sri**
Electronics & Communication Engineering Student

---

## ⭐ Conclusion

This project demonstrates how automation and AI-based evaluation can significantly reduce faculty workload and provide immediate academic feedback to students, creating a smarter digital campus environment.
