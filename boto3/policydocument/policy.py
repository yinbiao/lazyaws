# -*- coding=utf-8 -*-
#!/bin/env python

from jinja2 import Environment, FileSystemLoader
from collections import OrderedDict

class PolicyBase(object):
    def __init__(self,pid=None):
        env = Environment(loader=FileSystemLoader('.'))
        self.template = env.get_template('templates/policydocument.tpl')
        self.context = {}
        self.statement = []
        self.pid = pid
    def GetPolicy(self):
        #获取策略
        self.context['statement'] = self.statement
        self.context['pid'] = self.pid
        return self.template.render(self.context)
    def PutStatement(self,effect,action=None,notaction=None,resource=None,notresource=None,
                     principal=None,notprincipal=None,condition=None,sid=None):
        '''添加statement块
        args:
            sid str
            effect [required] str Allow|Deny
            action|notaction [required] str|array
            resource|notresource [required] str|array
            principal|notprincipal dict 
            condition dict
        '''
        self.statement.append({
            'sid':sid,
            'effect':effect,
            'action': repr(action),
            'notaction': repr(notaction),
            'resource': repr(resource),
            'notresource': repr(notresource),
            'principal': repr(principal),
            'notprincipal': repr(notprincipal),
            'condition': repr(condition),
            })


class S3Policy(PolicyBase):
    def S3BucketUser(self, bucket=[], username=[], action=[],
                     condition=None, effect="Allow"):
        '''管理s3 bucket 用户权限
        
        允许或禁止某些用户对相应bucket的权限

        args:
            bucket      [required] str|array
            username    [required] str|array 用户名称
            action      [required] str|array
            condition   str|array
            effect      Allow 或者 Deny
        '''
        if isinstance(bucket, list):
            resource = []
            for buc in bucket:
                resource.append("arn:aws:s3:::" + buc)
        else:
            resource = "arn:aws:s3:::" + bucket
        self.PutStatement(effect, action=action, resource=resource, condition=condition)
        return self.GetPolicy()





        