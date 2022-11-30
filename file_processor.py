def process_file(file_name):
    contents = []

    file = open(file_name)
    contents = file.readlines()
    file.close()

    return contents
