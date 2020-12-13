import os
from caps.read_yaml import get_file_path

file_path = get_file_path("schema_graphql")


# 查找npm生成的标准graphql接口
def find_schema(schema_type="queries", name="accountExist"):
    file_name = os.path.join(file_path, schema_type, name) + ".gql"
    with open(file_name) as f:
        query_str: str = f.read()
    return query_str


if __name__ == "__main__":
    query = find_schema()
    print(query)