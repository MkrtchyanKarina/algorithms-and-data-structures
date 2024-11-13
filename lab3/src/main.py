import os
import pathlib
import subprocess

project_path = pathlib.Path(__file__).parent.parent
array = os.listdir(project_path)
src_path = []

for i in range(1, len(array)-3): # в цикле от первой до последней папки
    task = array[i]

    dir_path = pathlib.Path(project_path, task) # получаем директорию i-ой папки
    src_path += [pathlib.Path(dir_path, "src", f'{task}.py')]


if __name__ == "__main__":
    for f in src_path:
        subprocess.run(['python', str(f)])

