from flask import Flask, render_template_string
import json

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Celeb Rankings</title>
<style>
body { font-family: Arial; background: #111; color: white; text-align:center; }
h1 { color: gold; }
table { margin:auto; border-collapse: collapse; width: 60%; }
td, th { padding: 10px; border-bottom: 1px solid #444; }
tr:hover { background: #222; }
</style>
</head>
<body>
<h1>🏆 Celebrity Rankings</h1>
<table>
<tr><th>Rank</th><th>Name</th><th>Rating</th></tr>
{% for p in players %}
<tr>
<td>{{loop.index}}</td>
<td>{{p[0]}}</td>
<td>{{p[1]["r"]|int}}</td>
</tr>
{% endfor %}
</table>
</body>
</html>
"""

@app.route("/")
def home():
    data = json.load(open("players.json"))
    sorted_players = sorted(data.items(), key=lambda x: x[1]["r"], reverse=True)
    return render_template_string(HTML, players=sorted_players)

app.run()
