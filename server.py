""" Import Flask, render_template, request. Import the package EmotionDetection
    The server is designed to perform emotion detection on user provided text"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    formatted_response = f"For the given statement, the system response is 'anger': {anger}, \
                            'disgust': {disgust} , 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.\
                            The dominant emotion is {dominant_emotion}"

    return formatted_response


@app.route("/")
def render_index_page():
    """
    Main function to run the Emotion Detection application.
    """
    return render_template('index.html', template_folder='templates')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)
