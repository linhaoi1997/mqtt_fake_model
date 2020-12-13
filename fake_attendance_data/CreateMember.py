from fake_attendance_data.BaseDataMaker import BaseDataMaker
from support.graphql_tools.find_schema_path import find_schema


class CreateMember(BaseDataMaker):

    def __init__(self):
        super(CreateMember, self).__init__()
        self.query = find_schema('mutations', 'createMember')
        self.formal_param = ["email", "name", "phone", "serialNumber"]

    @staticmethod
    def make_variables(**kwargs):
        return {
            "member": {
                "email": kwargs["email"],
                "name": kwargs["name"],
                "phone": kwargs["phone"],
                "photo": {"id": "19",
                          "src": "https://s3.cn-north-1.amazonaws.com.cn/seely-test/image/2020/5/9/a18756a8-f8a0-49cf-abee-f2364434e456.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAO353NJI5H7FKDEIQ%2F20200509%2Fcn-north-1%2Fs3%2Faws4_request&X-Amz-Date=20200509T035031Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=093c92cdc06acb66bc31fb67cb1d0a759d268c3ed5ba258d0af7aeb6325841c1",
                          "name": "",
                          "thumbnail": "https://s3.cn-north-1.amazonaws.com.cn/seely-test/__sized__/image/2020/5/9/a18756a8-f8a0-49cf-abee-f2364434e456-thumb-200x200-70.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAO353NJI5H7FKDEIQ%2F20200509%2Fcn-north-1%2Fs3%2Faws4_request&X-Amz-Date=20200509T035032Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=9efba26e17731e377b2fd68ab52689a439a7bfaaddbfb19873168ca0275070fb"
                          },
                "serialNumber": kwargs["serialNumber"]
            }
        }


if __name__ == "__main__":
    test = CreateMember()
    for i in test.make_data(2):
        print(i)
