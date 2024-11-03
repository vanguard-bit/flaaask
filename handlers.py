from check_allowed import comp_cmd_map
import subprocess
import os


def c_handler():
    pass


def py_string_builder(question_info):
    res = []
    for ele in question_info['testcases']:
        ele = '\n    '.join(ele)
        strr = f"""
if __name__ == '__main__':
    {ele}
    output_res = {question_info['snippet']}
    print(output_res == result)
"""
        res.append(strr)
    # for ele in res:
        # print(ele)
    return res


def py_handler(question_id, file_path, file_ext):
    import json
    try:
        with open('questions.json') as file:
            question_info = json.load(file)[str(question_id)]
    except KeyError:
        print('Question Key does not exist...check question number once.')
        return (False, '\033[36mInteral server error\033[0m')
    testcase_list = py_string_builder(question_info)
    for i, ele in enumerate(testcase_list, 1):
        with open(f'{file_path}', 'r') as file:
            code = ''.join(file.readlines())
            with open('new_name.py', 'w') as tempfile:
                tempfile.write(code + '\n\n' + ele)
        comp_op = subprocess.run(f'{comp_cmd_map[file_ext]} new_name.py', capture_output=True)
        comp_res = (bool(comp_op.stdout.decode()))
        comp_err = comp_op.stderr.decode()
        if len(comp_err) != 0:
            os.unlink('new_name.py')
            print('Compilation error')
            return (False, f'\033[31mCompilation error.\033[0m\n{comp_err}')
        if not comp_res:
            os.unlink('new_name.py')
            print('testcase failed')
            return (False, '\033[31mOne or more hidden testcase failed\033[0m')
        os.unlink('new_name.py')
        print(f'testcase {i} passed')
    return (True, '\033[34mAll testcase passed.\033[0m')


def cpp_handler():
    pass


def java_handler():
    pass


if __name__ == '__main__':
    py_handler(str(1), 'two.py', '.py')
