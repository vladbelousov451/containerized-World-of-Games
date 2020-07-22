from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
import Utils
import logging

scoreFile = Utils.SCORES_FILE_NAME

app = Flask(__name__)




log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)




@app.route('/')
def score_server():
    with open(scoreFile, "r") as File:
        Score = File.read()
        File.close()
    return render_template("index.html" , Scoreingame=Score )


def main():
    app.run(host='0.0.0.0' )

if __name__ == "__main__":
    main()