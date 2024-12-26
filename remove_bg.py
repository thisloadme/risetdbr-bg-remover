from pathlib import Path
from rembg import remove, new_session

session = new_session()

supported_ekstensi = ['.webp','.png','.jpg','.jpeg']
input_folder = 'input_folder'
output_folder = 'output_folder'

for file in Path(input_folder).glob('*'):
    ekstensi = str(file.suffix)
    if ekstensi not in supported_ekstensi:
        continue

    input_path = str(file)
    output_path = str(output_folder + '/' + (file.stem + "_out" + ekstensi))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session)
            o.write(output)