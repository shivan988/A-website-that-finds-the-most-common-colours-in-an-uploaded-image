from flask import Flask, render_template, redirect, url_for, session
from pract import extract_color_code
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


class Pathform(FlaskForm):
    path = StringField(label='Enter the path of the image', validators=[DataRequired()])
    submit = SubmitField(label="upload")


app = Flask(__name__)
app.secret_key = "This is my secretkey"
Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/image_color', methods=['GET', 'POST'])
def image_color():
    return render_template("image_color.html" )


@app.route('/color_extract')
def color_extract():
    list_col = session.get('list_col', [])
    image = session.get('image_path', [])
    return render_template('color_extract.html', list_col=list_col, image = image)


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    form = Pathform()
    if form.validate_on_submit():
        path = form.path.data
        list_col = extract_color_code(path)
        image_path = path
        session['list_col'] = list_col
        session['image_path'] = image_path
        return redirect(url_for('color_extract', list_col=list_col))
    return render_template("upload_image.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)