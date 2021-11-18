import argparse
import os

from scan_java_file import scan_java_file
from scan_yml_file import scan_yml_file


def flat(a):
    return [item for sublist in a for item in sublist]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--projectPath", required=True, help="扫描的工程路径")
    args = vars(parser.parse_args())
    print("扫描工程路径:", args['projectPath'])
    print("===============================================================")
    project_path = args['projectPath']
    api_value_content = []
    yaml_document = []
    g = os.walk(project_path)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            if file_name.endswith(".java"):
                print("已扫描文件:" + file_name)
                api_value_content.append(scan_java_file(path, file_name))
            if file_name.endswith("application.yml"):
                print("已扫描文件:" + file_name)
                yaml_document = scan_yml_file(path, file_name)
    api_value_content = flat(api_value_content)
    print("==================扫描完成=============================================")
    print(yaml_document)
    print(api_value_content)
    print(set(yaml_document) < set(api_value_content))
