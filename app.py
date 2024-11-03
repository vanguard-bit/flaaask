from flask import Flask
from flask import request
from waitress import serve
from check_allowed import allowed_files
import compile

app = Flask(__name__)


@app.get('/')
def get():
    return """\033[31mNo support for get request.\033[0m
Did you mean to send a \033[33mpost\033[0m request?"""


@app.post('/')
def report():
    if len(request.files) == 0:
        return 'No file attached.'
    file = request.files['file']
    file_name = file.filename
    allowed_file = allowed_files(file_name)
    if not allowed_file or not request.referrer:
        return f"\033[31m{file_name} not a valid file or no header argument.\033[0m"
    else:
        compile_res = compile.process(file, request.referrer)
        return compile_res[1]


if __name__ == '__main__':
    serve(app, host='192.168.0.4', port='8080')
