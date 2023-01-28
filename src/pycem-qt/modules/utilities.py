"""Collection of useful functions."""
# %% Imports
# Standard system imports
import os
from pathlib import Path

# Related third party imports

# Local application/library specific imports


# %% Functions
def get_project_root():
    """Return absolute path of root directory of project."""
    return Path(__file__).absolute().parent.parent.parent.parent


def delete_assets():
    """Clean-up any existing images or movies in webapp assets directory."""
    root = get_project_root()
    path = root / 'src/app/assets/img'
    for file_name in os.listdir(path):
        # Construct full file path
        file = path / file_name
        if os.path.isfile(file) and file.suffix in ['.gif', '.png', '.mp4']:
            print('Deleting file:', file)
            os.remove(file)


def list_files(path, ext='.png'):
    """Return a list of of files in a directory of a given file extension."""
    file_list = []
    for file_name in os.listdir(path):
        # Construct full file path
        file = path / file_name
        if os.path.isfile(file) and file.suffix == ext:
            file_list.append(file)
    return file_list


if __name__ == '__main__':
    print(get_project_root())
