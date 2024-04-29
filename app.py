from flask import Flask, jsonify, request
import json
import logging

app = Flask(__name__)

logging.basicConfig(filename='data_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def read_questions_from_json(filename):
    try:
        with open(filename, 'r') as f:
            questions = json.load(f)
        return questions
    except FileNotFoundError:
        logging.error(f"File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON in file '{filename}'.")
        return []

def filter_questions(questions, difficulty_level=None, tags=None):
    filtered_questions = []
    for question in questions:
        if (difficulty_level is None or question['difficulty_level'] == difficulty_level) and \
           (tags is None or any(tag in question['tags'] for tag in tags)):
            filtered_questions.append(question)
    return filtered_questions

def save_questions_to_json(questions, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(questions, f, indent=4)
        logging.info(f"Filtered questions saved to '{filename}'.")
        return True
    except Exception as e:
        logging.error(f"Error saving filtered questions to '{filename}': {e}")
        return False

@app.route('/filter-questions', methods=['POST'])
def filter_and_save_questions():
    data = request.get_json()
    input_filename = data.get('input_filename')
    output_filename = data.get('output_filename')
    difficulty_level = data.get('difficulty_level')
    tags = data.get('tags')

    logging.info(f"Reading questions from '{input_filename}'...")
    questions = read_questions_from_json(input_filename)
    logging.info("Filtering questions...")
    filtered_questions = filter_questions(questions, difficulty_level, tags)

    if filtered_questions:
        logging.info(f"Saving filtered questions to '{output_filename}'...")
        if save_questions_to_json(filtered_questions, output_filename):
            return jsonify({"message": f"Filtered questions saved to '{output_filename}'"}), 200
        else:
            return jsonify({"error": f"Failed to save filtered questions to '{output_filename}'"}), 500
    else:
        return jsonify({"error": "No questions found matching the filter criteria."}), 404

if __name__ == "__main__":
    app.run(debug=True)
