import os


def scan_yml_file(path, file_name):
    file_path = os.path.join(path, file_name)
    document_apis = []
    with open(file_path, "r") as java_file:
        file_lines = java_file.readlines()
        for count in range(0, len(file_lines)):
            strip_line = file_lines[count].strip()
            if strip_line.startswith("- "):
                if not strip_line[2:].startswith("name:"):
                    document_apis.append(strip_line[2:])
        java_file.close()
    return document_apis
