from troposphere import Template

from parameters import Parameters
from ec2 import EC2


class Stack(object):
    def __init__(self):
        self.template = Template()
        self.template.add_version("2010-09-09")
        self.template.add_description("Creates an EC2 image")

        parameters = Parameters()
        for param in parameters.values():
            self.template.add_parameter(param)

        for res in EC2(parameters=parameters).values():
            self.template.add_resource(res)

