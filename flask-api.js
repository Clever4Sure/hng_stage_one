// netlify-functions/flask-api.js
const fetch = require('node-fetch');

exports.handler = async (event, context) => {
  const flaskApiUrl = 'YOUR_FLASK_API_URL';  // Replace with your Flask API URL
  const response = await fetch(flaskApiUrl);
  const data = await response.json();

  return {
    statusCode: 200,
    body: JSON.stringify(data),
  };
};