from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
CORS(app, support_credentials=True)

limiter = Limiter(
    app,
    key_func=lambda: request.headers["X-Real-Ip"],
)


@app.route("/<path:vargs>", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("1 per day")
def add(vargs):
    result = 0
    try:
        # Convert to integers and check bound constraints
        for arg in vargs.split("/"):
            if '1' <= arg <= '9':   # Check value constraints
                result += int(arg)  # Find sum
    except:
        return "Bad request", 400
      
      
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
