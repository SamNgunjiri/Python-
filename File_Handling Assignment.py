def read_and_modify_file(input_filename, output_filename):
    try:
        with open(hello.txt, 'r') as file:
            content = file.read()


        modified_content = content.upper()  
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except IOError as e:
        print(f"An error occurred: {e}")

