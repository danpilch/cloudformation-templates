from troposphere import s3, Join, Ref, Tags, AWS_STACK_NAME

from magicdict import MagicDict


class Buckets(MagicDict):
    def __init__(self):
        super(Buckets, self).__init__()

        self.EMRBucket = s3.Bucket(
            "EMRBucket",
            BucketName=Join("-", [Ref(AWS_STACK_NAME), "input"]),
            Tags=Tags(
                Name=Join("-", [Ref(AWS_STACK_NAME), "input"])
            )
        )

