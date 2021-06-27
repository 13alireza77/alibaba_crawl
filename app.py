from flask import Response
from flask import request, jsonify
import flask

from manager import Manager

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/crawl', methods=['POST'])
def crawl():
    right_input = False
    try:
        url = request.form['url']
        pattern = request.form['pattern']
        level = int(request.form['level'])
        print(url, pattern, level)
        if url and pattern and level:
            right_input = True
            manager = Manager(level, pattern)
            manager.manage_crawler(url)
            print(manager.dict_result)
            return manager.dict_result
        raise Exception
    except Exception as e:
        print(e)
        if right_input:
            return Response('something went wrong')
        else:
            return Response('bad input')


if __name__ == '__main__':
    app.run()
