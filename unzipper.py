import zstandard
import shutil
from tqdm import tqdm

def decompress_zstd(input_file, output_file):
    with open(input_file, 'rb') as compressed_file:
        decompressor = zstandard.ZstdDecompressor()
        with decompressor.stream_reader(compressed_file) as reader:
            with open(output_file, 'wb') as decompressed_file:
                decompressed_file.write(reader.read())
def main():
    input_file = 'Path\\to\\Input_File'
    output_file = 'Path\\to\\Input_File'

    decompress_zstd(input_file, output_file)
    print("Decompression completed.")

if __name__ == "__main__":
    main()
