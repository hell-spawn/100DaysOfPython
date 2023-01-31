# Leveraging exception matching rules

from pathlib import Path
import shutil
import os

source_dir = Path.cwd()/"data"
target_dir = Path.cwd()/"backup"

print(target_dir)
for source_path in source_dir.glob('**/*.csv'):
    source_name = source_path.relative_to(source_dir)
    target_path = target_dir/source_name
    try:
        shutil.copy(source_path, target_path)
    except FileNotFoundError: 
        target_path.mkdir(exist_ok=True, parents=True)
    except OSError as ex:
        print(f"Copy {source_path} to {target_path} error {ex}")
