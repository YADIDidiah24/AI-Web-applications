# app.py

from flask import Flask, request, jsonify, render_template
from text_summary import summariser

# Initialize Flask app
app = Flask(__name__)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for text summarization
@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.form['text']
    ratio = float(request.form.get('ratio', 0.3))  # Default ratio is 0.3

    # Get summary and sentence scores from summariser
    summary, sentence_scores, original_len, summary_len = summariser(text, ratio)

    # Return the result in JSON format
    return jsonify({
        "summary": summary,
        "sentence_scores": sentence_scores,
        "original_length": original_len,
        "summary_length": summary_len
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
