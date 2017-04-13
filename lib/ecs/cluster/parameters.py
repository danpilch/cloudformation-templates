from troposphere import Parameter
from magicdict import MagicDict


class Parameters(MagicDict):
    def __init__(self):
        super(Parameters, self).__init__()

        self.Cooldown = Parameter(
            "Cooldown",
            Default="120",
            Type="Number",
            Description="Time in seconds between scaling functions"
        )

        self.InstanceGracePeriod = Parameter(
            "InstanceGracePeriod",
            Default="110",
            Type="Number",
            Description="Time to wait for an instance to launch. Must be less than Cooldown"
        )

        self.InstanceImageId = Parameter(
            "InstanceImageId",
            Default="ami-a7f2acc1",
            Type="String",
            Description="ECS optimised EC2 image, this should be periodically updated"
        )

        self.InstanceKeyName = Parameter(
            "InstanceKeyName",
            Type="AWS::EC2::KeyPair::KeyName",
            Description="Keypair to use for ECS instances"
        )

        self.InstanceMax = Parameter(
            "InstanceMax",
            Default="2",
            Type="Number",
            Description="Max number of ECS instances that can run"
        )

        self.InstanceType = Parameter(
            "InstanceType",
            AllowedValues=["t2.micro", "t2.small", "t2.large"],
            Default="t2.micro",
            Type="String",
            Description="EC2 instance type to use for ECS instances"
        )
            

