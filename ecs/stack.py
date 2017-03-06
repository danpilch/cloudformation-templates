from troposphere import Template, Output, Ref, Export, Sub

from cluster.parameters import Parameters
from cluster.iam import IAM
from cluster.ecs import ECS
from cluster.cloudwatch import Cloudwatch


class Stack(object):
    def __init__(self):
        self.template = Template()
        self.template.add_version("2010-09-09")
        self.template.add_description("Creates an ECS stack to run docker applications")

        parameters = Parameters()
        iam = IAM(parameters=parameters)
        ecs = ECS(parameters=parameters, IAM=iam)
        cloudwatch = Cloudwatch(ecs=ecs)

        for resource in parameters.values():
            self.template.add_parameter(resource)

        for resource in iam.values():
            self.template.add_resource(resource)

        for resource in ecs.values():
            self.template.add_resource(resource)

        for resource in cloudwatch.values():
            self.template.add_resource(resource)

        self.template.add_output(Output(
            "Cluster",
            Description="Cluster Name",
            Value=Ref(ecs.Cluster),
            Export=Export(Sub("${AWS::StackName}-cluster"))
        ))
        
        self.template.add_output(Output(
            "InstanceSG",
            Description="Security Group which balancer stack needs to access",
            Value=Ref(ecs.InstanceSG),
            Export=Export(Sub("${AWS::StackName}-sg-instance"))
        ))
