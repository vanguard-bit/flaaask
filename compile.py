from werkzeug.utils import secure_filename
import os.path
import subs


def makedir(filename, referrer):

    if not os.path.isdir('referrer_reqs'):
        print("referrer_reqs directory not found...", end=' ')
        print("creating referrer_reqs directory")
        os.mkdir('referrer_reqs')

    dir_path = 'referrer_reqs' + os.path.sep + referrer + os.path.sep
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    filename = secure_filename(filename)
    file_path = dir_path + os.path.sep + filename
    if os.path.isfile(file_path):
        print(f"deleting {referrer=} past request file")
        os.unlink(file_path)
    return file_path


def find_ques(file_path):
    assert os.path.isfile(file_path), "file has to be present."
    with open(file_path, "r") as file:
        first_line = file.readline()
        first_line = first_line.strip('#').strip('/**/').strip('//').strip()
        if first_line.isdigit():
            return (True, int(first_line))
        return (False, "\033[31mERROR: \033[0mFirst line in the file is not question number.")


def process(file, referrer):
    file_ext = file.filename[file.filename.rfind('.'):]
    file_path = makedir(file.filename, referrer)
    file.save(file_path)

    find_ques_res = find_ques(file_path)
    if not find_ques_res[0]:
        print(f"{referrer}: first line is not question number...returning error message")
        return (False, find_ques_res[1])
    question_id = find_ques_res[1]
    subs_res = subs.compilation(question_id, file_path, file_ext)
    return subs_res
