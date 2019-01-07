from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)
#make a which disney princess are you?
#if favorite color is blue, one point to Cinderella, Ariel, and Elsa
#if favorite color is pink, one point to Sleeping Beauty
#if favorite color is yellow, one point to Belle and Snow White
#if favortie color is purple, one point to Jasmine and Rapunzal
#if favorite color is red, one point to Anna and Merida
#if favorite color is orange, one point to Mulan, Pohantas, and Moana

