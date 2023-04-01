import base64
from Cryptodome.Cipher import AES

key = b't23sisasecr123ey'  # 这个key可以通过随机字节序列或伪随机数生成器来产生

# 定义加密函数
def encrypt(plaintext):
    # 将明文进行填充，使其长度是AES加密算法的倍数（16字节）
    plaintext = plaintext + (16 - len(plaintext) % 16) * chr(16 - len(plaintext) % 16)
    # 初始化加密器
    cipher = AES.new(key, AES.MODE_ECB)
    # 对明文进行加密
    ciphertext = cipher.encrypt(plaintext.encode())
    # 将加密后的密文进行Base64编码返回
    return base64.b64encode(ciphertext).decode()


# 定义解密函数
def decrypt(ciphertext):
    # 初始化解密器
    cipher = AES.new(key, AES.MODE_ECB)
    # 对密文进行Base64解码，再进行解密
    plaintext = cipher.decrypt(base64.b64decode(ciphertext)).decode()
    # 去除填充的数据，并返回解密后的明文
    return plaintext[:-ord(plaintext[-1])]

#
# # 测试加密解密函数
# if __name__ == '__main__':
#     plaintext = 'Hed!'  # 待加密的明文
#     ciphertext = encrypt(key, plaintext)  # 加密
#     print('密文是：', ciphertext)
#     decrypted_plaintext = decrypt(key, ciphertext)  # 解密
#     print('解密后的明文是：', decrypted_plaintext)
