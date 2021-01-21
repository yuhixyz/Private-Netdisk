import hashids


def hashid(_id, length=6):
    key = 'yuhi.xyz'
    hasher = hashids.Hashids(salt=key, min_length=length)
    return hasher.encode(_id)  # 返回哈希结果