from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Bicycle Mechanic",
    "location": "Sacramento, CA",
    "salary": "$50k - $100k"
  },
  {
    "id": 2,
    "title": "Frame Designer",
    "location": "Sacramento, CA",
    "salary": "$50k - $100k"
  },
  {
    "id": 3,
    "title": "Frame Painter",
    "location": "Sacramento, CA",
    "salary": "$50k - $100k"
  },
  {
    "id": 4,
    "title": "Shop Manager",
    "location": "Sacramento, CA"
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="LMQ Cycles")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)