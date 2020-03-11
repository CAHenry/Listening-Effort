from pathlib import *
import os


def get_rel_path(source, destination):
    out = os.path.relpath(source, destination)
    output = out.replace('\\', '/')
    output = './' + output
    return output

current_dir = PurePath(Path.cwd())
home_dir = PurePath(Path.home())
masking_dir = PurePath(r'C:\Users\craig\Documents\Listening-Effort\Media\Masking')
print(current_dir)
print(home_dir)
test_files = PurePath(r'C:\Users\craig\Documents\Listening-Effort\Test_Files')
out = os.path.relpath(test_files, masking_dir)
output = out.replace('\\', '/')

output_2 = get_rel_path(r'C:\Users\craig\Documents\Listening-Effort\Test_Files', r'C:\Users\craig\Documents\Listening-Effort\Media\Masking')
pass