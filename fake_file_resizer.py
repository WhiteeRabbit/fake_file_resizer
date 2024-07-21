#licensed by Shamil :)
import os

def pad_executable(input_file, output_file, target_size_mb):
    target_size = target_size_mb * 1024 * 1024

    input_size = os.path.getsize(input_file)
    padding_size = target_size - input_size
    
    if padding_size <= 0:
        print("! The input file's size is larger than the target size.")
        return

    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:

            f_out.write(f_in.read())

            f_out.write(b'\0' * padding_size)
    
    print(f"* File '{output_file}' has been created with size {target_size_mb} MB.")


in_file = input('your input file name:')
out_file = input('your output file name:')
num = input('your desired size:')
pad_executable(in_file, out_file, num)
