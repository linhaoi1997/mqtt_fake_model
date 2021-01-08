from caps.read_yaml import get_web_information
from support.graphql_tools.find_schema_path import find_schema
from sgqlc.endpoint.http import HTTPEndpoint
import ssl
from jsonpath import jsonpath
from support.graphql_tools.tools import get_foramt_number

ssl._create_default_https_context = ssl._create_unverified_context


class BaseDataMaker(object):
    def __init__(self):
        self.url = get_web_information('url')
        self.headers = {"Content-Type": "application/json"}
        self.graphql_client = HTTPEndpoint(self.url, self.headers)
        self.login()
        self.formal_param = []
        self.variables = {}

    def login(self):
        variables = get_web_information('admin')
        query = find_schema("mutations", "login")
        result = self.graphql_client(query, variables)
        token = jsonpath(result, "$..token")[0]
        self.headers["Authorization"] = "Token " + token

    def send_request(self):
        return self.graphql_client(self.query, self.variables)

    @staticmethod
    def make_variables(**kwargs):
        pass

    def make_data(self, start=1, count=10):
        kwargs = {}
        n = 1
        while n <= count:
            format_number = get_foramt_number(start)
            for i in self.formal_param:
                if i == "email":
                    kwargs[i] = "15700000{}@test.com".format(format_number)
                elif i == "name":
                    kwargs[i] = "test_{}".format(format_number)
                elif i == "phone":
                    kwargs[i] = "15700000{}".format(format_number)
                elif i == "serialNumber":
                    kwargs[i] = format_number
            self.variables = self.make_variables(**kwargs)
            n += 1
            start += 1
            yield self.send_request()


if __name__ == "__main__":
    test = BaseDataMaker()
