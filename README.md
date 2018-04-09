# Homework 1

1 ~ 3為手寫題

## 4. How2Crypto

- code4.py
- Round 0: 直接輸出
- Round 1: 00 -> a, 01 -> b, ...
- Round 2: 凱薩密碼
- Round 3: 凱薩的變形(?
- Round 4: Substitution Cipher
- Round 5: Transpostition Cipher
- Round 6: 間隔分段，每段取首字串起來，剩下的再頭尾頭尾遞迴取完
- 每個round成功後，都會拿到片段字串，串起來後Base64 decode會是一張flag圖片
- `BALSN{You_Are_Crypto_Expert!!!^_^}`
- P.S. script中的round 4、round 6有小片段要手動輸入

## 5. RSA

- code5.py
    - 使用sympy來做模逆
- 先用factordb把n分解
- 模逆求d
- `e^d mod N`把flag密文還原
- `BALSN{if_N_is_factorized_you_get_the_private_key}`

## 6. OTP

- code6.sh
- xortool直接解
    - https://github.com/hellman/xortool
    - git clone下來就能用惹
- `xortool -x "otp.txt" -c 20`
    - 會直接生成明文
- 原理：踹key長度，再踹每一位ascii去xor的結果，都要在可見字元，且以英文文章來說空格字元會非常多
- `BALSN{NeVer_U5e_0ne_7ime_PAd_7wIcE}`

## 7. Double AES

- 所有腳本都在code7/下
- 由2-DES的概念可以知道，使用同把key時，加解密的中間值會相同
- 先枚舉加密和解密的所有中間值可能(各2^23種)
    - `python3 m1.py > m1`
    - `python3 m2.py > m2`
- 然後再排序其內容
    - `sort m1 > m1-sorted`
    - `sort m2 > m2-sorted`
- 之後就可以用`O(n)`去找相同的hash值
    - `python 2aes_find.py`
    - 會找到key0=`6298659`和key1=`4272711`
- 拿去解密就能解出FLAG
    - `python3 dec.py`
- `BALSN{so_2DES_is_not_used_today}`

## 8. Time-machine

- 所有腳本都在code8/下
- 利用很久以前出來的SHA1 collision payload (兩個pdf)
- 取前300多個byte都還是相同SHA1
- 之後只要兩邊尾端同時加上相同字串，SHA1後的結果都會是一樣的
- 接著要做的就只是去找要加在尾端的字串，使得SHA1後最後六個Byte符合題目要求
- `BALSN{P0W_1s_4_w4st3_0f_t1m3_4nd_3n3rgy}`

## 9. Future Oracle

- code9.py
- Length Extension Attack
- `Nc`可控，餵進去會吐`sha256(password||ID||Nc||login)`
- 目標：構造`sha256(password||ID||Ns||login||printflag)`
    - 他取`printflag`是從尾端取，所以可以work
- 可以透過再開一個連線，餵Ns到Nc的地方，得到`sha256(password||ID||Ns||login)`
- 透過hashpump在後面加上`||printflag`
    - 這裡要踹`len(password)+2`的可能值
        - 最後踹出來是21
    - 可得到`sha256(password||ID||Ns||login padding ||printflag)`的值
    - 前半就塞`Base64(ID||Ns||login padding)`就行
- `BALSN{Wh4t_1f_u_cou1d_s33_th3_futur3}`

## 10. Digital Saving Account

- code10.py
- Block size: 16
- ECB mode下的cut and paste attack
- 構造`login=aaaaaaaaaa|bbbbbbbbbb&role=|guest&pwd=xxxxxx|`
    ```
    84dd debf 1a5a 0634 fc71 6205 305e 93e3
    ccdc e179 4c08 a81f 07d4 4a6c c534 cbe6
    c9c9 4ff4 02f8 1ce6 1674 e4a0 e525 1ef0
    3817 7c2b 193c 037b b94d 43ab 7874 3cd3
    ```
- 構造`login=aaaaaaaaaa|admin&role=guest|&pwd=bbbbbbbbbbb|`
    ```
    84dd debf 1a5a 0634 fc71 6205 305e 93e3
    7911 955f 68be ca09 a00c 7aa8 9693 62b7
    c0b9 8088 2508 5f2e 4a77 4803 91c2 af79
    3817 7c2b 193c 037b b94d 43ab 7874 3cd3
    ```
- 透過上面的結果構造`login=aaaaaaaaaa|&pwd=bbbbbbbbbbb|bbbbbbbbbb&role=|admin&role=guest|`
    ```
    84dd debf 1a5a 0634 fc71 6205 305e 93e3
    c0b9 8088 2508 5f2e 4a77 4803 91c2 af79
    ccdc e179 4c08 a81f 07d4 4a6c c534 cbe6
    7911 955f 68be ca09 a00c 7aa8 9693 62b7
    6728 7034 bff2 0d0c 39bd 8a47 af44 8152
    ```
- 帳號:`aaaaaaaaaa`；密碼:`bbbbbbbbbbbbbbbbbbbbb`
- base64 encoding string: `hN3evxpaBjT8cWIFMF6T48C5gIglCF8uSndIA5HCr3nM3OF5TAioHwfUSmzFNMvmeRGVX2i+ygmgDHqolpNit2cocDS/8g0MOb2KR69EgVI=`
- 接著就能以`admin`登入
- 登入後可以看到有:
    - Transaction: 2個隨意簽章的字串
    - Public Key: p, q, g, y
    - FLAG: 把sig("FLAG")的r, s餵給他才會噴FLAG
- 由於Transaction的k重複使用，我們可以透過它來還原private key!
- `k * (s1−s2) ≡ H(m1) − H(m2) mod q`即可還原k
- `x ≡ r^(−1) * (k * s − H(m)) mod q`知道k，即可還原private key x
- 其中H()為`SHA1`
- 有了private key就能直接簽`sig("FLAG")`
- 此處我使用了`gmpy2`套件輔助模逆等運算
- `BALSN{s3nd_m3_s0m3_b1tc01n_p13as3}`
