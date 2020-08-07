from sanic import Sanic
from sanic.response import json
from sanic_jwt import initialize
from sanic_jwt.decorators import protected

from src.user import authenticate

app = Sanic("Shalev's App")
initialize(app, authenticate=authenticate)


@app.route("/normalize", methods=["POST"])
@protected()
async def normalize(request):
    """Normalizes the input JSON"""
    return json({d["name"]: d[max([key for key in d if "val" in key.lower()])] for d in request.json.get("data")})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888)
