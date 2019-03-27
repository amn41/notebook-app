from sanic import Sanic
from sanic.response import json

app = Sanic()

template = """
<!DOCTYPE html>
<html>
<body>
<p>This is a great webpage.</p>
</body>
</html>"""

@app.route('/')
async def test(request):
    return template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
