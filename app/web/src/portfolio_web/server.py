from flask import Flask, render_template, request

app = Flask(__name__)
def main():
    app.run(debug=True)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return 'form submitted'
    else:
        return 'Something went wrong. Try again!'

if __name__ == "__main__":
    main()