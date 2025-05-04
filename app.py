from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Senior Software Engineer',
        'location': 'Bengaluru, India',
        'salary': '10 LPA'
    },
    {
        'id': 2,
        'title': 'UX/UI Designer',
        'location': 'Delhi, India',
        'salary': '8 LPA'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Chennai, India',
        'salary': '12 LPA'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '9 LPA'
    }
]

@app.route("/")
def home():
    return render_template("home.htm", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
