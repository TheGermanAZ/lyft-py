from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test(string_to_cut):
  msg = ""
  for i in range(3, len(string_to_cut), 3):
    msg += i
  response = {"return_string":msg}
  return response