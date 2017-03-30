from troposphere import Ref, Join, Tags, AWS_STACK_NAME
import troposphere.emr as emr

from magicdict import MagicDict


class EMR(MagicDict):
    def __init__(self, parameters, iam, buckets):
        super(EMR, self).__init__()

        self.EMRCluster = emr.Cluster(
            "EMRCluster",
            Name=Join("-", [Ref(AWS_STACK_NAME), "emr"]),
            ReleaseLabel=Ref(parameters.EMRVersion),
            Configurations=[
            ],
            JobFlowRole=Ref(iam.emr_instance_profile),
            LogUri=Join("", ["s3://", Ref(buckets.EMRBucket), "/logs"]),
            ServiceRole=Ref(iam.emr_service_role),
            Instances=emr.JobFlowInstancesConfig(
                Ec2KeyName=Ref(parameters.InstanceKeyPair),
                Ec2SubnetId=Ref(parameters.ClusterSubnet),
                MasterInstanceGroup=emr.InstanceGroupConfigProperty(
                    Name=Join("-", [Ref(AWS_STACK_NAME), "master"]),
                    InstanceCount="1",
                    InstanceType=Ref(parameters.InstanceType),
                    Market="ON_DEMAND"
                ),
                CoreInstanceGroup=emr.InstanceGroupConfigProperty(
                    Name=Join("-", [Ref(AWS_STACK_NAME), "worker"]),
                    BidPrice=Ref("AWS::NoValue"),
                    Market="ON_DEMAND",
                    EbsConfiguration=emr.EbsConfiguration(
                        EbsBlockDeviceConfigs=[
                            emr.EbsBlockDeviceConfigs(
                                VolumeSpecification=emr.VolumeSpecification(
                                    SizeInGB=Ref(parameters.InstanceStorage),
                                    VolumeType="gp2"
                                ),
                                VolumesPerInstance="1"
                            )
                        ],
                        EbsOptimized="true"
                    ),
                    InstanceCount=Ref(parameters.InstanceCount),
                    InstanceType=Ref(parameters.InstanceType),
                )
            ),
            Applications=[
                emr.Application(Name="Hadoop"),
                emr.Application(Name="Spark"),
                emr.Application(Name="Hive")
            ],
            VisibleToAllUsers="true",
            Tags=Tags(
                Name=Join("-", [Ref(AWS_STACK_NAME), "emr"])
            )
        )
        
