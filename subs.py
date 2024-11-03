import subprocess
import handlers
from check_allowed import comp_cmd_map


def check_health():
    try:
        from subprocess import DEVNULL
    except ImportError:
        import os
        DEVNULL = open(os.devnull, 'wb')
    try:
        for map in comp_cmd_map:
            if map == '.py':
                subprocess.run(comp_cmd_map[map] + ' doesnotexist.py', stdout=DEVNULL, stderr=subprocess.STDOUT)
            else:
                subprocess.run(comp_cmd_map[map], stdout=DEVNULL, stderr=subprocess.STDOUT)
    except FileNotFoundError:
        print(f"Install the compiler for {map} files")
        return (False, '\033[36mInteral server error\033[0m')
    return (True, 'No Interal server error')


def compilation(question_id, file_path, file_ext):
    check_health_res = check_health()
    if not check_health_res[0]:
        return check_health_res
    print('check health passed...handlers running')
    handler_res = handlers.py_handler(question_id, file_path, file_ext)
    return handler_res


if __name__ == '__main__':
    compilation('', '', '')
