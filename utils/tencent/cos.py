from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos.cos_exception import CosServiceError
from settings.dev import COS_SECRET_ID, COS_SECRET_KEY
from sts.sts import Sts


def exist_bucket(bucket, region):
    """
    bucket存在返回True
    """
    config = CosConfig(Region=region, SecretId=COS_SECRET_ID, SecretKey=COS_SECRET_KEY)
    client = CosS3Client(config)
    response = client.list_buckets()

    # print(response)
    buckets = response['Buckets']
    if not buckets:
        return False

    bucket_list = buckets['Bucket']
    for item in bucket_list:
        if item['Name'] == bucket:
            return True

    return False


def create_bucket(bucket, region='ap-nanjing'):
    """
    创建桶
    """
    config = CosConfig(Region=region, SecretId=COS_SECRET_ID, SecretKey=COS_SECRET_KEY)
    client = CosS3Client(config)
    client.create_bucket(
        Bucket=bucket,
        ACL='public-read'  # private/public-read/public-read-write
    )
    cors_config = {
        'CORSRule': [{
            'AllowedOrigin': '*',
            'AllowedMethod': ['GET', 'PUT', 'HEAD', 'POST', 'DELETE'],
            'AllowedHeader': '*',
            'ExposeHeader': '*',
            'MaxAgeSeconds': 500
        }
        ]
    }
    client.put_bucket_cors(
        Bucket=bucket,
        CORSConfiguration=cors_config
    )


def upload_file(bucket, region, file_object, key):
    """
    上传文件
    """
    config = CosConfig(Region=region, SecretId=COS_SECRET_ID, SecretKey=COS_SECRET_KEY)
    client = CosS3Client(config)
    client.upload_file_from_buffer(
        Bucket=bucket,
        Body=file_object,
        Key=key,
    )
    return "https://{}.cos.{}.myqcloud.com/{}".format(bucket, region, key)


def delete_file(bucket, region, key):
    config = CosConfig(Region=region, SecretId=COS_SECRET_ID, SecretKey=COS_SECRET_KEY)
    client = CosS3Client(config)
    client.delete_object(
        Bucket=bucket,
        Key=key,
    )


def delete_file_list(bucket, region, key_list):
    """
    删除文件列表
    key_list是一个字典
    """
    config = CosConfig(Region=region, SecretId=COS_SECRET_ID, SecretKey=COS_SECRET_KEY)
    client = CosS3Client(config)

    objects = {
        "Quiet": "true",
        "Object": key_list
    }

    client.delete_objects(
        Bucket=bucket,
        Delete=objects
    )


def get_credential(bucket, region):
    """ 获取临时凭证 """
    config = {
        # 临时密钥有效时长，单位是秒
        'duration_seconds': 300,
        'secret_id': COS_SECRET_ID,
        # 固定密钥
        'secret_key': COS_SECRET_KEY,
        # 换成你的 bucket
        'bucket': bucket,
        # 换成 bucket 所在地区
        'region': region,
        # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
        # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
        'allow_prefix': '*',
        # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
        'allow_actions': [
            # # 简单上传
            # 'name/cos:PutObject',
            # 'name/cos:PostObject',
            # # 分片上传
            # 'name/cos:InitiateMultipartUpload',
            # 'name/cos:ListMultipartUploads',
            # 'name/cos:ListParts',
            # 'name/cos:UploadPart',
            # 'name/cos:CompleteMultipartUpload',
            '*',
        ],
    }
    sts = Sts(config)
    result_dict = sts.get_credential()
    return result_dict
