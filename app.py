from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)  # Fix __name_

# Load the FAQ dataset
df = pd.read_csv('customer_support_faq_dataset.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_faq_response', methods=['POST'])
def get_faq_response():
    user_query = request.json.get('query', '').lower()
    if not user_query:
        return jsonify({"response": "Please enter a valid question."})

    # Search for a matching question
    results = df[df['question'].str.contains(user_query, case=False, na=False)]
    if results.empty:
        return jsonify({"response": "Sorry, I couldn't find an answer to that question."})

    # Return the first matching answer (or all if you prefer)
    answer = results.iloc[0]['answer']
    return jsonify({"response": answer})

if __name__ == '__main__':  # Fix __main_
    app.run(debug=True)