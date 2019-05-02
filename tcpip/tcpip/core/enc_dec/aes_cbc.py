#coding=utf-8
#AES AES/CBC/PKCS5|Zero

import base64
from Crypto.Cipher import AES

# pip install pycryptodome

'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数. ZeroPadding
 
'''
    在PKCS5Padding中，明确定义Block的大小是8位
    而在PKCS7Padding定义中，对于块的大小是不确定的，可以在1-255之间
    PKCS #7 填充字符串由一个字节序列组成，每个字节填充该字节序列的长度。
    假定块长度为 8，数据长度为 9，
    数据： FF FF FF FF FF FF FF FF FF
    PKCS7 填充： FF FF FF FF FF FF FF FF FF 01 01 01 01 01 01 01   ?应该是填充01
    
    python3:填充bytes(这个说法不对,AES的参数是字符串,不是byte)
    length = 16 - (len(data) % 16)
    data += bytes([length])*length
 
    python2:填充字符串
    length = 16 - (len(data) % 16)
    data += chr(length)*length
    
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s : s[0:-ord(s[-1])]
'''

class AES_CBC:

    def add_to_16(self, value):
        while len(value) % 16 != 0:
            value += '\0'
        return str.encode(value)  # 返回bytes

    #加密方法
    def encrypt_oracle(self, key, text):
        # iv=self.add_to_16(key)   #多了个iv
        # 偏移量 16个0
        iv = "0000000000000000"
        # 初始化加密器
        aes = AES.new(self.add_to_16(key), AES.MODE_CBC, self.add_to_16(iv))
        bs = AES.block_size
        pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)#PKS7 
    
        encrypt_aes = aes.encrypt(str.encode(pad2(text)))
    
        # 用base64转成字符串形式
        # 执行加密并转码返回bytes
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  
        print(encrypted_text)
        #和js的 结果相同 http://tool.chacuo.net/cryptaes
        return encrypted_text
    
    #解密方法
    def decrypt_oralce(self, key, text):
        # 初始化加密器
        # 偏移量 16个0
        iv = "0000000000000000"
        aes = AES.new(self.add_to_16(key), AES.MODE_CBC, self.add_to_16(iv))
        #优先逆向解密base64成bytes
        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
        #
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8') # 执行解密密并转码返回str
        unpad = lambda s : s[0:-ord(s[-1])]
        #PADDING = '\0'
        #print decrypted_text.rstrip(PADDING)  #zeropadding只见诶去掉结尾\0
        # print(unpad(decrypted_text))
        return unpad(decrypted_text)


if __name__ == '__main__':
    aes = AES_CBC()
    #加密
    key = "12345678"
    enc_text = aes.encrypt_oracle(key, "wwww.baidu.com")

    #解密
    dec_text = aes.decrypt_oralce(key, enc_text)
    print(key)
    print(enc_text)
    print(dec_text)