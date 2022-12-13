import zipfile
import pathlib


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


def compress_files(filepath, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        if type(filepath) == list:
            for fpath in filepath:
                fpath = pathlib.Path(fpath)
                archive.write(fpath, arcname=fpath.name)
        else: archive.write(filepath, arcname=filepath.name)

# if __name__ == '__main__':
#     compress_files(filepath=['add.png', 'complete.png'], dest_dir='dist')