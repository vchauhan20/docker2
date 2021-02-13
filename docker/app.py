from flask import Flask,request,  render_template

from free import TextSimilarity
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculate',methods=['POST'])
def calculate():
    texts = [x for x in request.form.values()]

    first = TextSimilarity(texts[0].lower().strip())
    second = TextSimilarity(texts[1].lower().strip())
    third = TextSimilarity(texts[2].lower().strip())
    stop_usage = int(texts[3])

    first.create_tokens()
    second.create_tokens()
    third.create_tokens()

    first.remove_stop_words(stop_usage)
    second.remove_stop_words(stop_usage)
    third.remove_stop_words(stop_usage)


    first_second_similarity = first.cosine_similar_score(second)
    second_third_similarity = second.cosine_similar_score(third)
    first_third_similarity = first.cosine_similar_score(third)

    result_12 = f'first --> Second Similarity :{round(first_second_similarity,3)   }'
    result_23 = f' Second --> Third Similarity :{round(second_third_similarity,3) } '
    result_13 = f' First --> Third  Similarity :{round(first_third_similarity,3)  }'
    return render_template('home.html',result_12=result_12 , result_23 = result_23 , result_13 = result_13)

if __name__ == '__main__':
    app.run(debug=True)
