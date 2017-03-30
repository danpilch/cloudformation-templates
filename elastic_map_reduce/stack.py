from troposphere import Template

from parameters import Parameters
from emr import EMR
from iam import IAM
from buckets import Buckets


class Stack(object):
    def __init__(self):
        self.template = Template()
        self.template.add_version("2010-09-09")
        self.template.add_description("Creates resources for a EMR environment")

        parameters = Parameters()
        for resource in parameters.values():
            self.template.add_parameter(resource)

        buckets = Buckets()
        for resource in buckets.values():
            self.template.add_resource(resource)        

        for resource in IAM(parameters=parameters, buckets=buckets).values():
            self.template.add_resource(resource)

        for resource in EMR(parameters=parameters, buckets=buckets, iam=IAM(parameters=parameters, buckets=buckets)).values():
            self.template.add_resource(resource)
