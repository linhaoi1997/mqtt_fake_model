# coding:utf-8
import yaml
import os


def get_file_path(name):
    d = get_config("path.yaml")
    return d.get(name)


def get_config(file_name):
    # 获取当前脚本所在文件夹路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yaml_path = os.path.join(cur_path, file_name)
    with open(yaml_path, 'r', encoding='utf-8') as f:
        cfg = f.read()
    d = yaml.safe_load(cfg)
    return d


def get_web_information(*name):
    d = get_config("web_information.yaml")
    if not name:
        return d
    elif len(name) == 1:
        return d.get(name[0])
    else:
        return [d.get(i) for i in name]


if __name__ == "__main__":
    print(get_file_path("schema_graphql"))
    s = get_web_information('admin')
    print(s)
    # print(get_web_information("db"))
