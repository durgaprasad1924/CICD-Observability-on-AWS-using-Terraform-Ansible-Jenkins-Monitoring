from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Pipeline Demo</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, Helvetica, sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: #ffffff;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                background-color: rgba(0, 0, 0, 0.35);
                padding: 40px;
                border-radius: 12px;
                max-width: 800px;
                text-align: center;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            }
            h1 {
                font-size: 42px;
                margin-bottom: 10px;
            }
            h2 {
                font-size: 24px;
                font-weight: normal;
                margin-bottom: 25px;
                color: #ffdd57;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
            }
            .footer {
                margin-top: 30px;
                font-size: 14px;
                color: #dddddd;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 Hello, Welcome!</h1>
            <h2>CI/CD Pipeline Demo Application</h2>

            <p>
                A <strong>CI/CD pipeline</strong> (Continuous Integration & Continuous Deployment)
                is an automated process that helps developers build, test, and deploy applications
                quickly and reliably.
            </p>

            <p>
                In this project, every code change pushed to GitHub is automatically:
                <br>✔ Built using Jenkins
                <br>✔ Containerized with Docker
                <br>✔ Deployed on AWS EC2
            </p>

            <div class="footer">
                🚀 Deployed using Jenkins | Docker | AWS
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

