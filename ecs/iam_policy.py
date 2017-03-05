from troposphere.iam import Role, InstanceProfile
from awacs.aws import Allow, Statement, Principal, Policy
from awacs.sts import AssumeRole

from magicdict import MagicDict
from parameters import Parameters

class IAM(MagicDict):
    def __init__(self, parameters):
        super(IAM, self).__init__()

        self.InstanceRole = Role(
            "InstanceRole",
            AssumeRolePolicyDocument=Policy(
                Statement=[
                    Statement(
                        Effect=Allow,
                        Action=[AssumeRole],
                        Principal=Principal("Service", ["ec2.amazonaws.com"])
                    )
                ]
            )
        )

        self.InstanceProfile = InstanceProfile(
            "InstanceProfile",
            Path="/",
            Roles=[self.InstanceRole]
        )
