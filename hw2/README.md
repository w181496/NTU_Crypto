# Homework 2

## CBC1
- 假設`A1||A2||A3` = `Encrypt("QQ Homework is too hard, how2decrypt QQ")`
- `Decrypt(A1||A2||A3||A1||A2||A3)`
  
   = `unpad(IV xor D(A1)||A1 xor D(A2)||A2 xor D(A3)||A3 xor D(A1)||A1 xor D(A2)||A2 xor D(A3))`
- 其中unpad只會影響最後一個block
- 所以`A3 xor D(A1) xor A3`就可以得到`D(A1)`
    - 這邊的`A3`是`明文的最後一部分+Padding`
- 再來`IV xor D(A1) xor D(A1)`就得到`IV`惹
- `BALSN{IV=KEY=GG}`

## CBC2

- Padding Oracle Attack
- IV會隨機取，隨便挑一組IV和Encrypted FLAG來解就行
- 要解某個Block B，就去構造隨意的字串A，串成`A||B`去解密
- `A||B`解出來，B對應的明文是`A xor D(B)`
- 若Padding不正確，會噴Fail
- 假設要解B最後1 Byte，那就是想辦法構造去使得`A xor D(B)`最後Byte變成`0x01`
- 所以`D(B)[-1] xor A[-1] = 1`，`D(B)[-1] = A[-1] xor 1`
- 再讓`D(B)[-1] xor 原本前面一塊Block[-1]`就能得到明文最後1 Byte
    - 第一塊Block的前一塊就是IV
- 第2、第3 Byte依此類推，讓結尾改成0x02, 0x03, ...
- `BALSN{1T_15_V3RY_FUN_T0_533_TH3_FL4G_4PP34R_0N3_BY_0N3_R1GHT_XD}`

## CBC3

- 這題關鍵在unpad
- pad的方式跟前面不一樣，他是先塞`隨機字串`，再塞`chr(隨機字串長度)`
- 所以這個長度的值如果能被偽造，unpad時，就有可能unpad掉大於長度16的字串
- 正常情況: `IV||flag[0-15]||flag[16-31]||flag[32-47]||flag[48-63]||mac||padding`
- 如果偽造成: `IV||flag[0-15]||flag[16-31]||flag[32-47]||flag[48-63]||mac||IV||flag[0-15]`
- 此時只需動一動倒數第二個的`IV`，使他unpad後，變成`IV||flag[0-15]||flag[16-31]||flag[32-47]||flag[48-63]||mac`
    - 必需剛好讓他unpad後，最後一塊剩mac，這樣才不會爛掉
- 這樣我們就可以知道，我們的unpad抓到的長度是31，就可以還原FLAG惹
- `BALSN{N33D_B3TT3R_P4DD1NG_M3TH0D_T0_PR3V3NT_P00DL3_4TT4CK_SSLv3}`

## Man-in-the-middle Attack

- 這題跟HITCON 2016 PAKE幾乎一樣
- 首先可以知道，如果我們當中間人，把A的data送給B，B的送給A，則最後的key相同
- 如果我們猜密碼是x，則`g = pow(sha512(x), 2, p)`
- 再來分別對A和B送`g`，其中A和B對我們送的是`g^a`和`g^b`
- 若最後出來的`FLAG xor key` xor `g^a`和`FLAG xor key` xor `g^b`相同，代表我們猜對密碼惹
    - 因為只有其中一輪是不同的，其他輪兩邊的K都是相同的
- 猜對密碼後，我們再做一次正常的連線，此時就能算出K的值惹，也就能知道key惹
- `BALSN{Wow_you_are_really_in_the_middle}`

## Cloudburst

- 這題很有趣，他中間有一層proxy，要我們查真實的網站ip
    - https://the-real-reason-to-not-use-sigkill.csie.org:10130/
- 可以用censys.io查
    - https://140.112.91.250/
- `BALSN{what_a_C1oudPiercer}`

## One-time Wallet

- 題目用`random.getrandbits(32)`生成隨機數
- Wallet Address用了3個getrandbits，Password用了5個
- 因為是偽隨機，且生成夠多個，所以可以預測
- 我用這個tool來算: https://github.com/kmyk/mersenne-twister-predictor
- 只要再預測剩下的5個隨機數就行惹 (Password)
- My script
    - Run wallet.py
    - `head -624 state | mt19937predict > predict`
    - find and get the next five numbers
    - Run predict.py and paste that five nunmbers
- `BALSN{R3tir3_4t_tw3nty}`

## TLS Certificate

- 直接拿rootCA.crt和rootCA.key去簽就行惹
- `openssl req -new -key rootCA.key -subj "/C=TW/ST=Taiwan/L=Taipei/O=National Taiwan University/OU=Department of Computer Science and Information Engineering/CN=*.csie.ntu.edu.tw" -sha256 -out balsn.csr`
- `openssl x509 -req -days 365 -in balsn.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -sha256 -out balsn.crt`
- `BALSN{t1s_ChAiN_0f_7ru5t}`
