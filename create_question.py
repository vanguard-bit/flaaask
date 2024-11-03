import json
import os.path


def create(question_id, question_dict):
    temp_dict = {}
    if os.path.isfile('questions.json'):
        with open('questions.json', 'r') as file:
            temp_dict = json.load(file)
    temp_dict = {**temp_dict, **question_dict}
    # print(temp_dict)
    for k, v in temp_dict.items():
        print(k, v)
        print()
    with open('questions.json', 'w') as file:
        json.dump(temp_dict, file, indent=2)


if __name__ == '__main__':
    question_id = 1
    question_dict = {question_id: {
        'snippet': 'twoSum(nums, target)',
        'testcases': [
            ['nums = [2, 7, 11, 15]', 'target = 9', 'result = [0, 1]'],
            ['nums = [3, 2, 4]', 'target = 6', 'result = [1, 2]'],
            ['nums = [3, 3]', 'target = 6', 'result = [0, 1]'],
        ]
    }
    }
    create(question_id, question_dict)
