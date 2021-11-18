import os
import re


def scan_java_file(path, file_name):
    file_path = os.path.join(path, file_name)
    api_value_content = []
    with open(file_path, "r") as java_file:
        file_lines = java_file.readlines()
        for count in range(0, len(file_lines)):
            strip_line = file_lines[count].strip()
            if strip_line == "@ApiOperation(":
                count = count + 1
                patten = re.compile(r'\"(.*)\"')
                api_value = patten.findall(file_lines[count].strip())
                if len(api_value) != 0:
                    api_value_content.append(api_value[0])
        java_file.close()
    return api_value_content
