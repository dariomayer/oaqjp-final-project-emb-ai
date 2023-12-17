from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if all(response[key] is None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']):
        return "Invalid input ! Try again."
    else:
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>"
    )

    return formatted_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)