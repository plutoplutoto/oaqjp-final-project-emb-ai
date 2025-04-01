"""Flask server for the Emotion Detection web application."""

from flask import Flask, render_template, request, Response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyzes emotion from user-provided text."""
    text_to_analyse = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return Response("Invalid text! Please try again.", status=400, mimetype="text/plain")

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return Response(response_text, status=200, mimetype="text/plain")


@app.route("/")
def render_index_page():
    """Renders the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
