from flask import Flask, render_template, url_for, redirect,request,jsonify
import pickle
import pandas as pd


app = Flask(__name__)

@app.route("/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/healthblueprint")
def healthblueprint():
    return render_template("healthblueprint.html")

@app.route("/organhealth")
def organhealth():
    return render_template("organhealth.html")

@app.route("/lungs")
def lungs():
    return render_template("lungs.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/kidney")
def kidney():
    return render_template("kidney.html")

@app.route("/liver")
def liver():
    return render_template("liver.html")

@app.route("/fooddiet")
def fooddiet():
    return render_template("fooddiet.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

def assess_diet(food_items):
    # Simple example logic for assessing diet
    total_calories = sum(int(calories) for calories in food_items)
    if total_calories < 1500:
        suggestion = "You should add more high-calorie foods."
        return "Your calorie intake is too low.", suggestion
    elif total_calories > 2500:
        suggestion = "You should reduce intake of high-calorie foods."
        return "Your calorie intake is too high.", suggestion
    else:
        return "Your calorie intake is within a healthy range.", ""

@app.route('/fooddiet_prediction', methods=['GET', 'POST'])
def fooddiet_prediction():
    if request.method == 'POST':
        food_items = request.form.getlist('food')
        assessment, suggestion = assess_diet(food_items)
        return render_template('fooddiet_result.html', assessment=assessment, suggestion=suggestion)
    return render_template('fooddiet_form.html')


data = pd.read_csv('C:/Users/Nithin/OneDrive/Desktop/av/env/dataset/calories.csv')
@app.route('/calories')
def calories():
    return render_template('calories.html')

@app.route('/get_calories', methods=['POST'])
def get_calories():
    item = request.form['foodItem']
    calorie_value = data[data['Item'] == item]['Calories'].values
    if len(calorie_value) == 0:
        return "Item not found"
    return f"Calories for {item}: {calorie_value[0]}"


HEALTHY_FOODS = {"apple", "banana", "spinach", "quinoa", "chicken", "salmon", "avocado", "broccoli", "carrot", "kale", "sweet potato", "brown rice", "eggs", "nuts", "Greek yogurt", "blueberries", "oats", "lean beef", "turkey", "tuna", 
                "asparagus", "bell peppers", "cabbage", "cauliflower", "mushrooms", "green beans", "lentils", "chickpeas", "whole grain bread", "flaxseeds", "chia seeds", "almonds", "walnuts", "pistachios", "coconut oil", "olive oil", "chia seeds",
                "seaweed", "low-fat dairy products", "watermelon", "kiwi", "oranges", "grapefruit", "pomegranate", "figs", "dates", "prunes", "black beans", "kidney beans", "edamame", "tofu", "tempeh", "brown rice", "wild rice", "basmati rice",
                "idli", "dosa", "upma", "poha", "dhokla","carrots", "lettuce", "tomatoes", "celery", "cucumber", "bell peppers", "onions", "garlic", "ginger", "turmeric", "whole wheat bread", "whole grain pasta", "quinoa", "millet", "barley", "beans", "legumes", "chickpeas", "lentils", "peas", "tofu",
    "sunflower seeds", "pumpkin seeds", "chia seeds", "flaxseeds", "sesame seeds", "walnuts", "almonds", "cashews", "peanuts", "pecans", "pistachios", "hazelnuts", "coconut", "olive oil", "avocado oil", "canola oil", "walnut oil", "sunflower oil",
    "cooking spray", "vinegar", "balsamic vinegar", "red wine vinegar", "apple cider vinegar", "mustard", "hummus", "salsa", "guacamole", "pesto", "soy sauce", "tamari", "coconut aminos", "herbs", "spices", "turmeric", "cinnamon", "oregano", "basil",
    "rosemary", "thyme", "sage", "parsley", "cumin", "coriander", "nutritional yeast", "green tea", "black tea", "herbal tea", "coffee", "red wine", "dark chocolate", "cocoa powder", "unsweetened almond milk", "unsweetened coconut milk", "unsweetened soy milk",
    "unsweetened oat milk", "sparkling water", "mineral water", "still water", "unsweetened herbal tea"}

UNHEALTHY_FOODS = {"cake", "pizza", "burger", "soda", "ice cream", "fries", "chips", "cookies", "candy", "white bread", "processed meats", "fried foods", "white rice", "pastries", "energy drinks", "donuts", "bacon", "hot dogs", "cheeseburgers",
                  "deep-fried foods", "potato chips", "microwave popcorn", "canned soups", "sugary cereals", "artificial sweeteners", "instant noodles", "bottled salad dressings", "margarine", "frozen dinners", "canned fruits in syrup",
                  "store-bought smoothies", "refined pasta", "sweetened yogurt", "high-sugar coffee drinks", "deli meats", "whipped cream", "highly processed snack bars", "store-bought juices", "fast food", "packaged baked goods", "pre-packaged meals",
                  "white rice", "vada", "samosa", "pakora", "bhaji", "bhature","frozen pizza", "microwave dinners", "potato chips", "tortilla chips", "cheese puffs", "corn chips", "pork rinds", "candy bars", "doughnuts", "pastries", "croissants", "muffins", "white bread", "bagels", "sugary cereals", "pop tarts", "pancakes",
    "waffles", "syrups", "jellies", "sweetened jams", "processed meats", "hot dogs", "bacon", "sausages", "salami", "pepperoni", "jerky", "instant noodles", "ramen", "cup noodles", "bottled smoothies", "sweetened beverages", "energy drinks", "sugary sodas",
    "fruit juices", "sports drinks", "sweetened coffee drinks", "sweetened teas", "flavored waters", "milkshakes", "margaritas", "cocktails", "beer", "liquor", "fried chicken", "fried fish", "fried shrimp", "fried calamari", "fried tofu", "fried vegetables",
    "fried rice", "fried noodles", "fried dumplings", "fried snacks", "fried desserts", "fried ice cream", "fried bananas", "fried dough", "fried candy bars", "fried pastries", "fried cookies", "fried doughnuts", "fried cakes", "fried pies", "fried bread"}

def check_diet(food_choices):
    healthy_count = sum(1 for food in food_choices if food in HEALTHY_FOODS)
    unhealthy_count = sum(1 for food in food_choices if food in UNHEALTHY_FOODS)
    if healthy_count > unhealthy_count:
        return "Good job! You're consuming a healthy diet."
    elif healthy_count < unhealthy_count:
        return "You should consider including more healthy foods in your diet."
    else:
        return "Your diet seems balanced, but you can still improve it by adding more variety."

@app.route('/dietcheck_from')
def dietcheck_from():
    return render_template('dietcheck_from.html')

@app.route('/dietcheck_result', methods=['POST'])
def dietcheck_result():
    food_choices = request.form['foods'].lower().split(',')
    diet_status = check_diet(food_choices)
    return render_template('dietcheck_result.html', diet_status=diet_status)

user_data = {
    'daily_entries': {},
}

def dietcheck_result():
    foods = request.form.get('foods')
    
    # Process the foods here (e.g., check against a database of food items)
    # For simplicity, let's just count the number of items entered
    
    # Update user's daily entries
    user_id = 1  # Replace with actual user identification
    if user_id not in user_data['daily_entries']:
        user_data['daily_entries'][user_id] = 0
    user_data['daily_entries'][user_id] += 1
    
    # Check if user has reached reward milestones
    rewards = []
    days_tracked = user_data['daily_entries'][user_id]
    if days_tracked == 100:
        rewards.append("You've reached 100 days! Here's your reward.")
    if days_tracked == 150:
        rewards.append("Congratulations! You've reached 150 days.")
    if days_tracked == 200:
        rewards.append("Wow! You've been tracking for 200 days.")
    if days_tracked == 300:
        rewards.append("Incredible! 300 days of consistent tracking.")
    if days_tracked == 500:
        rewards.append("You've reached a major milestone - 500 days!")
    
    return render_template('diet_result.html', diet_status=" ".join(rewards))


@app.route("/exercise")
def exercise():
    return render_template("exercise.html")

@app.route("/cancer")
def cancer():
    return render_template("cancer.html")


@app.route("/Kidneycancer")
def Kidneycancer():
    return render_template("Kidneycancer.html")

@app.route("/breastcancer")
def breastcancer():
    return render_template("breastcancer.html")

@app.route("/lungcancer")
def lungcancer():
    return render_template("lungcancer.html")

@app.route("/carcinomacancer")
def carcinomacancer():
    return render_template("carcinomacancer.html")

@app.route("/melanoma")
def melanoma():
    return render_template("melanoma.html")

@app.route("/lymphomacancer")
def lymphomacancer():
    return render_template("lymphomacancer.html")

@app.route("/leukemiacancer")
def leukemiacancer():
    return render_template("leukemiacancer.html")

@app.route("/bloodcancer")
def bloodcancer():
    return render_template("bloodcancer.html")

@app.route("/braincancer")
def braincancer():
    return render_template("braincancer.html")


@app.route("/milkdonor")
def milkdonor():
    return render_template("milkdonor.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")



diabetes_model = pickle.load(open('C:/Users/Nithin/OneDrive/Desktop/av/env/diabetes_model.sav', 'rb'))
@app.route('/diabetes_prediction', methods=['GET', 'POST'])
def diabetes_prediction():
    if request.method == 'POST':
        # Get input data from the form
        Pregnancies = float(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])

        # Make prediction
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        # Process prediction result
        if diab_prediction[0] == 1:
            diab_diagnosis = 'This Person May Have A Risk Of Developing Diabetes'
        else:
            diab_diagnosis = 'The person is not diabetic'

        # Render a template with the prediction result
        return render_template('diabetes_result.html', diagnosis=diab_diagnosis)
    else:
        return render_template('diabetes_form.html')
    

    
heart_disease_model = pickle.load(open('C:/Users/Nithin/OneDrive/Desktop/av/env/heart_disease_model.sav', 'rb'))
@app.route('/heart_prediction', methods=['GET', 'POST'])
def heart_prediction():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])

        # Make prediction with numeric values
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'This Person May Have A Risk Of Developing Heart disease'
        else:
            heart_diagnosis = 'The person is not Heart disease'

        # Render a template with the prediction result
        return render_template('heart_result.html', diagnosis=heart_diagnosis)
    else:
        return render_template('heart_form.html')
        


parkinsons_model = pickle.load(open('C:/Users/Nithin/OneDrive/Desktop/av/env/parkinsons_model.sav', 'rb'))
@app.route('/predict_parkinsons', methods=['POST', 'GET'])
def predict_parkinsons():
    if request.method == 'GET':
        return render_template('parkinsons_form.html')
    elif request.method == 'POST':
        
        fo = float(request.form['fo'])
        fhi = float(request.form['fhi'])
        flo = float(request.form['flo'])
        Jitter_percent = float(request.form['Jitter_percent'])
        Jitter_Abs = float(request.form['Jitter_Abs'])
        RAP = float(request.form['RAP'])
        PPQ = float(request.form['PPQ'])
        DDP = float(request.form['DDP'])
        Shimmer = float(request.form['Shimmer'])
        Shimmer_dB = float(request.form['Shimmer_dB'])
        APQ3 = float(request.form['APQ3'])
        APQ5 = float(request.form['APQ5'])
        APQ = float(request.form['APQ'])
        DDA = float(request.form['DDA'])
        NHR = float(request.form['NHR'])
        HNR = float(request.form['HNR'])
        RPDE = float(request.form['RPDE'])
        DFA = float(request.form['DFA'])
        spread1 = float(request.form['spread1'])
        spread2 = float(request.form['spread2'])
        D2 = float(request.form['D2'])
        PPE = float(request.form['PPE'])
        
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "This Person May Have A Risk Of Developing Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            
        # Render a template with the prediction result
        return render_template('parkinsons_result.html', diagnosis=parkinsons_diagnosis)
    else:
        return render_template('parkinsons_form.html')



    
    
@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/heartgraph')
def heartgraph():
    return render_template('heartgraph.html')

@app.route('/kidneygraph')
def kidneygraph():
    return render_template('kidneygraph.html')

@app.route('/livergraph')
def livergraph():
    return render_template('livergraph.html')

@app.route('/lungsgraph')
def lungsgraph():
    return render_template('lungsgraph.html')











if __name__ == '__main__':
    app.run(debug=True)
