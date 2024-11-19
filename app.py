from flask import Flask, request, jsonify

from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Health Calculator API",
        "version": "1.0",
        "endpoints": {
            "GET /": "This help message",
            "GET /health": "Health check endpoint",
            "POST /bmi": {
                "description": "Calculate BMI",
                "parameters": {
                    "height": "Height in meters (e.g., 1.75)",
                    "weight": "Weight in kilograms (e.g., 70)"
                },
                "example": {
                    "curl": "curl -X POST http://localhost:5000/bmi -H 'Content-Type: application/json' -d '{\"height\": 1.75, \"weight\": 70}'"
                }
            },
            "POST /bmr": {
                "description": "Calculate BMR",
                "parameters": {
                    "height": "Height in centimeters (e.g., 175)",
                    "weight": "Weight in kilograms (e.g., 70)",
                    "age": "Age in years (e.g., 25)",
                    "gender": "Either 'male' or 'female'"
                },
                "example": {
                    "curl": "curl -X POST http://localhost:5000/bmr -H 'Content-Type: application/json' -d '{\"height\": 175, \"weight\": 70, \"age\": 25, \"gender\": \"male\"}'"
                }
            }
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        data = request.get_json()
        if not data or 'height' not in data or 'weight' not in data:
            return jsonify({"error": "Missing required fields"}), 400

        height = float(data['height'])
        weight = float(data['weight'])
        
        bmi_value = calculate_bmi(height, weight)
        
        # Determine BMI category
        category = ""
        if bmi_value < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_value < 25:
            category = "Normal weight"
        elif 25 <= bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return jsonify({
            "bmi": round(bmi_value, 2),
            "category": category
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        data = request.get_json()
        required_fields = ['height', 'weight', 'age', 'gender']
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender']

        bmr_value = calculate_bmr(height, weight, age, gender)
        
        return jsonify({
            "bmr": bmr_value,
            "daily_calories": {
                "sedentary": round(bmr_value * 1.2, 2),
                "light_exercise": round(bmr_value * 1.375, 2),
                "moderate_exercise": round(bmr_value * 1.55, 2),
                "active": round(bmr_value * 1.725, 2),
                "very_active": round(bmr_value * 1.9, 2)
            }
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
