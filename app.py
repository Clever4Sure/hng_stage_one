from flask import Flask, request, jsonify
import datetime


app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_info():
    # Retrieve query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    #Get the current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')
    
    #Get the current UTC time with validation of +/-2 minutes
    current_utc_time = datetime.datetime.utcnow()
    if abs(current_utc_time.second - 0) <= 2:
        utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    else:
        utc_time = "Validation Error: UTC time not within +/-2 minutes of 0 seconds."
    
    # GitHub URLs
    github_file_url = "https://github.com/Clever4Sure/hng_stage_one.task/blob/main/stange_one.py"
    github_repo_url = "https://github.com/Clever4Sure/hng_stage_one.task.git"
    
    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)