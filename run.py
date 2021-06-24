from flask import Flask

# from app.views import app
from api_app.views import app

if __name__ == "__main__":
    app.run(debug = True)
