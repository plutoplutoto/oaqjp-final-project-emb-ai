from flask import Flask, render_template, request, Response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyse = request.args.get("textToAnalyze")

    
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
