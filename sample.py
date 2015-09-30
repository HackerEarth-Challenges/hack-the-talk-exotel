# This is a skeleton python code indicating how input and output should be
# taken. You can write code in any language though.

def read_input():
    # input.txt contains the mp3 file name in each line which are present int
    # he current directory the program is being executed.
    f = open('input.txt')
    files = f.read().split('\n')

    # Sanity cleaning to remove empty strings
    files = [f for f in files if f]
    return files

def process_mp3_files():
    files = read_input()
    for mp3_file in files:
        print compute_emotion(mp3_file)

def compute_emotion(mp3_file):
    # Assuming our conversations are always happy :)
    return 'happy'

if __name__ == '__main__':
    process_mp3_files()
