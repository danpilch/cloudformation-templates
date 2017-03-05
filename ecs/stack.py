from troposphere import Template

from parameters import Parameters
from iam_policy import IAM
from ecs import ECS


class Stack(object):
    def __init__(self):
        self.template = Template()
        self.template.add_version("2010-09-09")
        self.template.add_description("Creates an ECS stack to run docker applications")

        parameters = Parameters()
        for param in parameters.values():
            self.template.add_parameter(param)

        for resource in IAM(parameters=parameters).values():
            self.template.add_resource(resource)

        for resource in ECS(parameters=parameters).values():
            self.template.add_resource(resource)

