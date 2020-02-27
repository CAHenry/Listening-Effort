from pathlib import *
import os
current_dir = PurePath(Path.cwd())
home_dir = PurePath(Path.home())
print(current_dir)
print(home_dir)
test_files = PurePath(r'D:\documents\Docs\Imperial\Listening-Effort\Test_files')
out = os.path.relpath(test_files, current_dir)
current_dir.relative_to(test_files)
pass