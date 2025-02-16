from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# HTML template
html = '''
    <h1>Enter Your Name</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
    {% if name %}
        <p>Name submitted: {{ name }}</p>
    {% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        # Make a POST request to the API
        response = requests.post('https://example.com/api', json={'name': name})
        print(response.json())
    return render_template_string(html, name=name)

if __name__ == '__main__':
    app.run(debug=True)