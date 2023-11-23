import subprocess
import time

def main(num, group_of_50):

    ref_dict = {
        1: '1-50',
        2: '51-100'
    }

    file = f'C:/Users/hpickersgill/AppData/Local/Programs/Python/Python311/python.exe c:/Users/hpickersgill/Desktop/Personal_files/Euler-problems/{ref_dict[group_of_50]}/prob_{num}.py'
    
    subprocess.call(file, shell=True)

if __name__ == "__main__":
    start = time.time()
    main(74, 2)
    print(f'{time.time() - start:.2f} seconds')