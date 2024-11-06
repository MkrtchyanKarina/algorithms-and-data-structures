import pathlib


def read_txt(file: str):
    task_number = file.split('\\')[-1][4:-3]
    folder = f'task{task_number}'
    input_file = f'input{task_number}.txt'
    path = pathlib.Path(pathlib.Path(__file__).parent.parent, folder, 'txtf', input_file)
    file = open(path)
    arguments = file.read().split("\n")
    return arguments


def write_txt(file: str, result:str):
    task_number = file.split('\\')[-1][4:-3]
    folder = f'task{task_number}'
    output_file = f'output{task_number}.txt'
    path = pathlib.Path(pathlib.Path(__file__).parent.parent, folder, 'txtf', output_file)
    file = open(path, 'w')
    file.write(result)