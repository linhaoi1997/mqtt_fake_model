from support.base_test.base_api.BaseApi import BaseApi
from support.tools import graphql_query, find_test_file, record
import json
import requests
import random
from urllib3 import encode_multipart_formdata


def format_s(name: str):
    if name.endswith("s"):
        return name[:-1]
    return name


def format_name(name: str):
    all_name = (
        "spare_part_outbounds", "spare_part_receipts", "spare_parts", "thing_inspection_rules",
        "thing_inspections", "thing_inspections_feedback",
        "thing_maintenance", "thing_maintenance_feedback", "thing_maintenance_rules", "thing_repairs",
        "thing_repairs_feedback", "things"
    )
    if name.endswith("Input"):
        name = name[:-5]
    if name.startswith("Create") or name.startswith("Update"):
        name = name[6:]
    name = name.lower()
    for i in all_name:
        if "".join([format_s(j) for j in i.split("_")]) == name:
            return i
    raise Exception("没有找到对应表单")


class FormStructApi(BaseApi):

    def run(self, variables=None, is_change_struct=False):
        if is_change_struct:
            self.change_struct()
            self.set_random_variables()
        if variables:
            self.variables = variables
        self.result = self.user.send_request(self.api_name, self.variables).result
        return self.result

    def change_struct(self):
        interface = getattr(self.schema, self.api_name)
        _input = getattr(self.schema, interface.input)
        # 接口查询对应表单的 formstruct
        form_struct = BaseApi("formStruct")
        form_struct.variables = {"name": format_name(_input.name), "isDraft": False}
        form_struct.run()
        result = form_struct.result
        custom_fields = result["data"]["formStruct"]["customFields"]
        # 更新api
        _input.update_param(custom_fields, self.schema)


class UploadApi(BaseApi):
    def __init__(self):
        super(UploadApi, self).__init__("uploadFiles")

    def upload(self, files_name: list):
        files_num = len(files_name)
        # operation 的参数
        file_list = [None for i in range(files_num)]
        # map 的参数
        file_dict = {}
        for i in range(files_num):
            file_dict[str(i + 1)] = ["variables.files.%s" % i]
        self.variables = {
            "operations": (
                None,
                json.dumps({"query": graphql_query.get_query(self.api_name),
                            "variables": {"files": file_list},
                            "operationName": "uploadFiles"})),
            "map": (None, json.dumps(file_dict)),
        }
        # 每个file对应的值
        file_map = {}
        for i in range(files_num):
            file_name = files_name[i]
            file_tuple = {str(i + 1): (file_name, find_test_file(file_name), self.get_type(file_name))}
            self.variables.update(**file_tuple)

        encode_data = encode_multipart_formdata(self.variables)
        data = encode_data[0]
        self.user.update_headers(**{"Content-Type": encode_data[1]})
        self.result = requests.post(self.user.base_url, headers=self.user.headers, data=data).json()
        record(self.result, "上传文件结果")
        return self.result

    @staticmethod
    def get_type(name: str):
        _type = name.split('.')[-1]
        type_map = {
            'xls': 'application/vnd.ms-excel',
            'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            "pdf": "application/pdf",
            "doc": "application/msword",
            "png": "application/msword",
            "jpg": "image/jpg"
        }
        try:
            return type_map.get(_type)
        except KeyError:
            raise Exception("没有对应类型，请补充")


class QuerySingleApi(BaseApi):

    def query(self, _id):
        var = {
            "id": _id
        }
        self.run(var)
        return self.result["data"]


class QueryManyApi(BaseApi):

    def query(self, offset=0, limit=10, _filter=None):
        if _filter is None:
            _filter = {}
        var = {
            "offset": offset,
            "limit": limit,
            "filter": _filter
        }
        return self.run(var)

    def query_and_return_ids(self, offset=0, limit=10, _filter=None):
        self.query(offset, limit, _filter)
        ids = self.find_from_result("$.data." + self.api_name + ".data[*].id")
        if ids:
            return ids
        else:
            return []

    def query_and_return_certain(self, name, offset=0, limit=10, _filter=None):
        self.query(offset, limit, _filter)
        results = self.find_from_result("$.data." + self.api_name + ".data[*].%s" % name)
        if results:
            return results
        else:
            return []


class CreateApi(FormStructApi):

    def create(self, variables=None, find_id=True, allow_none=False):
        if variables is None:
            variables = {}
        self.set_random_variables()
        for json_path, value in variables.items():
            if allow_none:
                self.change_value(f_json_path="input." + json_path, value=value)
            else:
                if value:
                    self.change_value(f_json_path="input." + json_path, value=value)
                else:
                    self.pop_value(f_json_path="input." + json_path)
        self.run()
        if find_id:
            self.id = self.find_first_deep_item("id")
        return self.result


class UpdateApi(BaseApi):

    def update(self, _id=None, variables=None):
        if self.id and not _id:
            _id = self.id
        self.change_value(f_json_path="input." + "id", value=_id)
        if variables is None:
            variables = {}
        for json_path, value in variables.items():
            if value is not None:
                self.change_value(f_json_path="input." + json_path, value=value)
            else:
                self.pop_value(f_json_path="input." + json_path)
        return self.run()

    def update_all(self, _id=None, variables=None):
        self.set_random_variables()
        self.update(_id, variables)

    def update_part(self, _id=None, variables=None):
        self.variables = {"input": {}}
        self.update(_id, variables)


class DeleteApi(BaseApi):

    def delete(self, _ids: list):
        var = {
            "input": {
                "ids": _ids
            }
        }
        return self.run(var)


class DeleteSingleApi(BaseApi):

    def delete(self, _id: int):
        var = {
            "id": _id
        }
        return self.run(var)


class ExportApi(BaseApi):
    def export(self, _ids: list):
        var = {
            "input": {
                "ids": _ids
            }
        }
        return self.run(var)


class QueryTreeApi(QuerySingleApi):

    def __init__(self, api_name, tree_object, user=None):
        super(QueryTreeApi, self).__init__(api_name, user)
        # 初始化一个树的定义类
        self.tree_object = tree_object

    def return_tree_root(self):
        self.run()
        # 定义树并返回根结点
        tree_root = self.tree_object(json.loads(self.find_from_result("$.data.%s" % self.api_name)[0]))
        return tree_root

    def return_random_deep_node(self, num: int, has_next_deep=False, child_num=1):
        tree_node = self.return_tree_root()
        _num = 1
        tmp = []
        while _num < num:
            # 每一层随机选择一个符合要求的节点
            _num += 1
            tmp = tree_node.children
            # 如果需要返回的节点有子节点就做检查
            if has_next_deep:
                tmp = []
                for child in tree_node.children:
                    if len(child.children) >= child_num:
                        tmp.append(child)
            else:
                tmp = tree_node.children
            if tmp:
                tree_node = random.choice(tmp)
                tmp.pop(tmp.index(tree_node))
            else:
                raise Exception("第%s层级没有有子层级的节点" % _num)
        return tree_node

    def return_certain_node(self, _name):
        # 查找一个 name 为要求 _name 的节点
        _name = str(_name)
        tree_root = self.return_tree_root()

        # 递归函数
        def search(tree_node):
            tmp = []
            for child in tree_node.children:
                if child.name == _name:
                    return child
                else:
                    tmp.append(child)
            for child in tmp:
                if search(child):
                    return search(child)

        if _name == tree_root.name:
            return tree_root
        else:
            result = search(tree_root)
            if result:
                return result
            else:
                raise AssertionError("找不到 名称为%s的节点" % _name)


if __name__ == '__main__':
    test = FormStructApi("createSparePart")
    test.change_struct()
    test = UploadApi()
    print(test.upload(["test.jpg", "test.jpeg"]))
