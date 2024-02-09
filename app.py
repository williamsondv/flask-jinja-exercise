from flask import Flask, request, render_template
import stories

app = Flask(__name__)

@app.route("/")
def select_story():
    return render_template('dropdown.html')

@app.route('/form')
def story_form():
    story = stories.story_dict[request.args["story_selection"]]
    return render_template('form.html', words = story.prompts, story_num = request.args["story_selection"])

@app.route("/story")
def story():
    story = stories.story_dict[request.args["story_num"]]
    text = story.generate(request.args)
    return render_template('story.html', text=text)      