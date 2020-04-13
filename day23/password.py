import base64
import os
from hashlib import sha256
from hmac import HMAC

"""

http://zhuoqiang.me/password-storage-and-python-example.html
https://www.jianshu.com/p/d54a4f592dc7
Python 3最重要的新特性大概要算是对文本和二进制数据作了更为清晰的区分。文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示。

在将字符串存入磁盘和从磁盘读取字符串的过程中，Python 自动地帮你完成了编码和解码的工作，你不需要关心它的过程，例如你能把一个中文赋值给字符串。而使用 bytes 类型，实质上是告诉 Python，不需要它帮你自动地完成编码和解码的工作，而是用户自己手动进行，并指定编码格式。
"""
def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8)  # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, bytes)
    assert isinstance(password, str)

    if isinstance(password, str):
        password = password.encode('UTF-8')

    assert isinstance(password, bytes)

    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])


if __name__ == "__main__":
    hashed = encrypt_password('secret password')
    print("password",hashed)
    assert validate_password(hashed, 'secret password')
    print(hashed)
    print(base64.b64encode(hashed))
    print(base64.b64decode(base64.b64encode(hashed)))