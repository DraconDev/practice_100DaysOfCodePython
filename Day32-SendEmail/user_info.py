import pandas


class User():
    """docstring for User."""

    def __init__(self, ):
        super(User, self).__init__()
        self.email = ''
        self.pw = ''
        self.code = ''
        self.get_user()

    def get_user(self):
        data = pandas.read_csv(
            '../../../_credentials/_test_email/cred.csv')
        # login = data.iloc[:2].to_dict('records')[0]
        # print(data, )
        data = data.to_dict('records')[0]
        self.email = data['email']
        self.pw = data['pw']
        self.code = data['code']
