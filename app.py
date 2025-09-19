# def handler(event, context):
#     return {
#         "statusCode": 200,
#         "body": "Hello from Python Lambda!"
#     }


from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on EC2 with GitHub Actions!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
