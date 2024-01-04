from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    site_info = {
        'title': 'Oxbridge',
        'description': 'Oxbridge — Oxford and Cambridge Universities, the oldest in the UK, the most important of the "ancient universities", using tutorials as the main form of education, unlike other British universities. The term is formed by merging the first syllable in the word Oxford and the last syllable in the word Cambridge. The word Oxbridge first appeared in 1849 in the novel Pendennis by the English satirical writer William Thackeray. By the mid-50s of the twentieth century, the word had firmly entered the lexicon of the British, and it began to be used even in official sources and printed publications in sections of the review of educational systems.',
        'image': 'static/logo.jpg'
    }
    return render_template('site.html', info=site_info)

if __name__ == '__main__':
    app.run(debug=True)

