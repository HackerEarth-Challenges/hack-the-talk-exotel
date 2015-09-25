# This is a skeleton python code indicating how input and output should be
# taken. You can write code in any language though.

def read_mp3_files_from_current_dir():
    # You should read all the mp3 files from the current directory where the
    # program is being executed. You can read them one by one or get all files
    # in one list.
    return ['one.mp3', 'two.mp3']

def process_mp3_files():
    files = read_mp3_files_from_current_dir()
    for mp3_file in files:
        print compute_emotion(mp3_file)

def compute_emotion(mp3_file):
    # Assuming our conversations are always happy :)
    return 'happy'

if __name__ == '__main__':
    process_mp3_files()
