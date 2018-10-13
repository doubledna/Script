#! /usr/bin/env python
# -*-encoding=utf-8-*-

from M2Crypto import RSA
msg = 'aaaa-aaaa'
rsa_pub = RSA.load_pub_key('rsa_pub.pem')
rsa_pri = RSA.load_key('rsa_pri.pem')
print '***********************************************'
print 'public key encryption,private key encryption'
ctxt = rsa_pub.public_encrypt(msg, RSA.pkcs1_padding)
ctxt64 = ctxt.encode('base64')
print ('cipher:%s'% ctxt64)
rsa_pri = RSA.load_key('rsa_pri.pem')
txt = rsa_pri.private_decrypt(ctxt, RSA.pkcs1_padding)
print('clear:%s'% txt)
print '************************************************'
print 'private key encryption,public key encryption'
ctxt_pri = rsa_pri.private_encrypt(msg, RSA.pkcs1_padding)
ctxt64_pri = ctxt.encode('base64')
print('cipher:$s'% ctxt64_pri)
txt_pri = rsa_pub.public_decrypt(ctxt_pri, RSA.pkcs1_padding)
print('clear:%s'% txt_pri)

