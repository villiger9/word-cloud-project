from flask import Flask, render_template, request, jsonify
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_wordcloud", methods=["POST"])
def generate_wordcloud():
    text = request.form["text"]

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        text
    )

    # Convert word cloud to image
    img_buffer = BytesIO()
    wordcloud.to_image().save(img_buffer, format="PNG")
    img_str = (
        "data:image/png;base64," + base64.b64encode(img_buffer.getvalue()).decode()
    )

    return jsonify({"image": img_str})


if __name__ == "__main__":
    app.run(debug=True)
