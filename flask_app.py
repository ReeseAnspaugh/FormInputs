from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    color = request.form.get('input_color', '')
    snack = request.form.get('input_snack', '')
    place = request.form.get('input_place', '')
    weekend = request.form.get('input_weekend','')
    princess = {"Cinderella": 0, "Ariel":0, "Elsa":0, "Sleeping Beauty":0, "Belle":0, "Snow White":0, "Jasmine":0, "Rapunzal":0, "Anna":0, "Merida":0, "Mulan":0, "Pocahontas":0, "Moana":0}
    if color == "Blue":
        princess["Cinderella"] = princess["Cinderella"]+1
        princess["Ariel"] = princess["Ariel"]+1
        princess["Elsa"] = princess["Elsa"]+1
    if color == "Red":
        princess["Anna"] = princess["Anna"]+1
        princess["Merida"] = princess["Merida"]+1
    if color == "Pink":
    if color == "Yellow":
    if color == "Purple":
    if color == "Orange":
    if color == "Green":
    if snack == "Fries":
    if snack == "Chips":
    if snack == "Yogurt":
    if snack == "Candy":
    if snack == "Carrots":
    if snack == "Other":
    return render_template("main_page.html", input_data=dropdown,
                           output="You're  %s." % name)
#make a which disney princess are you?
#if favorite color is blue, one point to Cinderella, Ariel, and Elsa
#if favorite color is pink, one point to Sleeping Beauty
#if favorite color is yellow, one point to Belle and Snow White
#if favortie color is purple, one point to Jasmine and Rapunzal
#if favorite color is red, one point to Anna and Merida
#if favorite color is orange, one point to Mulan, Pocahontas, and Moana


