from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        try:
            # Extract data from request
            data = request.json.get('data', [])
            if not data:
                raise ValueError("Invalid data format")

            # Process the input data
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]
            lowercase_alphabets = [item for item in alphabets if item.islower()]
            highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
            
            user_id = "sparshmittal99"
            email = "sparshmittal8b@gmail.com"
            roll_number = "21BCE11689"
            
            response = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
            }
            return jsonify(response)
        except Exception as e:
            return jsonify({"is_success": False, "error": str(e)})
    
    elif request.method == 'GET':
        response = {
            "operation_code": 1
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
