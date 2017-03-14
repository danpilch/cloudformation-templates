from troposphere import Parameter
from troposphere.constants import KEY_PAIR_NAME, SUBNET_ID
from magicdict import MagicDict


class Parameters(MagicDict):
    def __init__(self):
        super(Parameters, self).__init__()

        self.ClusterSubnet = Parameter(
            "ClusterSubnet",
            Description="Subnet ID for creating the EMR cluster",
            Type=SUBNET_ID
        )

        self.EMRVersion = Parameter(
            "EMRVersion",
            Description="EMR version",
            Type="String",
            Default="emr-5.4.0"
        )
        
        self.InstanceType = Parameter(
            "InstanceType",
            Default="m1.large",
            Type="String",
            Description="Instance type for cluster",
            AllowedValues=["m1.large", "m1.xlarge"]
        )  
        
        self.InstanceCount = Parameter(
            "InstanceCount",
            Description="Number of worker instances to start",
            Type="Number",
            Default="2"
        )

        self.InstanceStorage = Parameter(
            "InstanceStorage",
            Description="Size in GB for instance storage",
            Type="Number",
            Default="100"
        )

        self.InstanceKeyPair = Parameter(
            "InstanceKeyPair",
            Default="np-shared",
            Type=KEY_PAIR_NAME,
            Description="The keypair to use for initial connections"
        )
