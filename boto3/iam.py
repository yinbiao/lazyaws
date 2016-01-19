# -*- coding=utf-8 -*-
#!/bin/env python

import boto3
from include.tools import fprint
from policydocument import policy

class IamApi(object):
    def __init__(self):
        self.iam_client = boto3.client('iam')

    def create_user(self, username, path="/"):
        if not path.endswith("/"):
            path = path + "/"
        return self.iam_client.create_user(Path=path, UserName=username)

    def create_login_profile(self,username, password, **kwargs):
        '''创建用户密码
        args:
            UserName (string) -- [REQUIRED]
            Password (string) -- [REQUIRED]
            PasswordResetRequired (boolean) -- Specifies whether the user is required to 
                                               set a new password on next sign-in.

        returns:
            {
                'LoginProfile': {
                    'UserName': 'string',
                    'CreateDate': datetime(2015, 1, 1),
                    'PasswordResetRequired': True|False
                }
            }
        '''
        return self.iam_client.create_login_profile(UserName=username,
                                                    Password=password, **kwargs)

    def update_login_profile(self, username, password, **kwargs):
        # returns : None
        return self.iam_client.update_login_profile(UserName=username, Password=password, **kwargs)

    
    def create_policy(self, policyname, policydocument, **kwargs):
        '''创建策略

        Args:
            PolicyName: 'string', [REQUIRED]
            Path: 'string',
            PolicyDocument: 'string', [REQUIRED]
            Description: 'string'

        Returns:
            {
                'Policy': {
                    'PolicyName': 'string',
                    'PolicyId': 'string',
                    'Arn': 'string',
                    'Path': 'string',
                    'DefaultVersionId': 'string',
                    'AttachmentCount': 123,
                    'IsAttachable': True|False,
                    'Description': 'string',
                    'CreateDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1)
                }
            }
        '''
        return self.iam_client.create_policy(PolicyName=policyname,
                                             PolicyDocument=policydocument,
                                             **kwargs)

    def get_user(self, username):
        return self.iam_client.get_user(UserName=username)

    def get_account_summary(self):
        return self.iam_client.get_account_summary()

    def get_account_authorization_details(self,*args, **kwargs):
        return self.iam_client.get_account_authorization_details(
                Filter=args, **kwargs)

    def get_credential_report(self):
        return self.iam_client.get_credential_report()

    def get_policy(self,arn):
        return self.iam_client.get_policy(PolicyArn=arn)

    def list_policies(self,**kwargs):
        return self.iam_client.list_policies(**kwargs)

    def list_user_policies(self, username, **kwargs):
        return self.iam_client.list_user_policies(UserName=username, **kwargs)


if __name__ == '__main__':
    api = IamApi()
    #api.create_user('lonay','/admin')
    #print api.get_user('lonay')
    #print api.get_account_summary()
    # fprint( api.get_account_authorization_details("User","Role",
    #         **{'MaxItems':100}) )
    #print api.get_credential_report()
    #fprint( api.get_user() )
    #fprint( api.list_policies(**{"Scope":"All","OnlyAttached":False}) )
    #s3policy = policy.S3Policy(pid="3333")
    #c = { "DateGreaterThan" : {
    #            "aws:CurrentTime" : "2013-12-15T12:00:00Z"
    #    }}
    #print s3policy.S3BucketUser(['aaa','bbb'],"user1","s3:GetBucketTagging",condition=c)
    fprint( api.update_login_profile('lonay','lonay821') )









