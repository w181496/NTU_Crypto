from pwn import *

host = '140.112.31.96'
port = 10126


saved = {}
def switchBS(bs):
    """
    Switch bytes and string.
    """
    if type(bs) == type(b''):
        return "".join(map(chr, bs))
    return n2s(int(''.join( hex(ord(c))[2:].rjust(2,'0') for c in bs),16))
    

class Connect:
    
    def encrypt(self,m1,m2):
        conn = remote(host,port)
        conn.recvuntil('> ')
        conn.sendline('1')
        conn.recvuntil('m1: ')
        conn.sendline(m1)
        conn.recvuntil('m2: ')
        conn.sendline(m2)
        conn.recvuntil('\n')
        result = conn.recvuntil('\n').strip()
        conn.close()
        return result
    
    def decrypt(self,conn,payload):
        conn.recvuntil('> ')
        conn.sendline('2')
        conn.recvuntil('m: ')
        conn.sendline(payload)
        result = conn.recvuntil('\n').strip()
        return result

    def oracle(self,i):
        # make m1 + flag + m2 = 80
        m1 = 'a'*(15-i%16)
        m2 = 'a'*((i%16)+1)
        # get iv(16) + ENC(m1+flag+m2+md5 (96)+ padding(16))
        enc = switchBS(self.encrypt(m1,m2))
        print(enc)
        iv = enc[:16*2]
        success = enc[16*2:-16*2]
        get_block = 1 + i//16
        conn = remote(host,port)
        for i in range(0,100):
            fake = 'ff'*15 + hex(i)[2:].rjust(2,'0') + enc[get_block*16*2:(get_block+1)*16*2]
            payload = (iv + success + fake)
            # print(payload)
            result = self.decrypt(conn,payload)
            # print(i,result)
            if result == b'Success' :
                print(chr(i ^ 31 ^ int(enc[((get_block*16*2)-2):(get_block*16*2)],16)))
                return chr(i ^ 31 ^ int(enc[((get_block*16*2)-2):(get_block*16*2)],16))
        
        conn = remote(host,port)
        for i in range(100,200):
            fake = 'ff'*15 + hex(i)[2:].rjust(2,'0') + enc[get_block*16*2:(get_block+1)*16*2]
            payload = (iv + success + fake)
            # print(payload)
            result = self.decrypt(conn,payload)
            # print(i,result)
            if result == b'Success' :
                print(chr(i ^ 31 ^ int(enc[((get_block*16*2)-2):(get_block*16*2)],16)))
                return chr(i ^ 31 ^ int(enc[((get_block*16*2)-2):(get_block*16*2)],16))
        

        conn = remote(host,port)
        for i in range(200,256):
            fake = 'ff'*15 + hex(i)[2:].rjust(2,'0') + enc[get_block*16*2:(get_block+1)*16*2]
            payload = (iv + success + fake)
            # print(payload)
            result = self.decrypt(conn,payload)
            # print(i,result)
            if result == b'Success' :
                print(chr(i ^ 31 ^ int(enc[((get_block*16*2)-2):(get_block*16*2)],16)))
                return chr(i ^ 31 ^ int(enc[((get_block*16*2)-2):(get_block*16*2)],16))

test = Connect()
flag = ['B', 'A', 'L', 'S', 'N', '{', 'N', '3']
for i in range(len(flag),64):
    flag.append(test.oracle(i))
    print(''.join(flag))

