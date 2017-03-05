from troposphere import Parameter
from magicdict import MagicDict


class Parameters(MagicDict):
    def __init__(self):
        super(Parameters, self).__init__()

        self.InstanceImage = Parameter(
            "InstanceImage",
            Default="ami-02ace471",
            Type="String",
            Description="Select an AMI"
        )

        self.InstanceKeyPair = Parameter(
            "InstanceKeyPair",
            Default="dan",
            Type="AWS::EC2::KeyPair::KeyName",
            Description="The keypair to use for initial connections"
        )

        self.InstanceStorageOS = Parameter(
            "InstanceStorageOS",
            Default="8",
            Type="Number",
            Description="The amount of storage, in GB, to add to the OS disk"
        )

        self.InstanceType = Parameter(
            "InstanceType",
            Default="t2.micro",
            Type="String",
            Description="Select a size for the Birst Connect server",
            AllowedValues=["t2.micro", "t2.small", "t2.medium", "t2.large"]
        )

        self.PublicDomain = Parameter(
            "PublicDomain",
            Default="ctrlengineering.com",
            Type="String",
            Description="domain to use for public DNS record",
        )    
