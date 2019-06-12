`challenge` `algorithm` `python` `fun`  

一个有趣的Python谜题网站  

[Python Challenge](http://www.pythonchallenge.com/) 


### 1

[第1个谜题说明](http://www.pythonchallenge.com/pc/def/map.html) 

#### 解答思路:
一个简单的加密算法,加密过程如下:输入一个英文字母,向后移动两位,输入移动后的字母.比如 a->c, z->b

[python代码](./1.py)


### 2

[第2个谜题说明](http://www.pythonchallenge.com/pc/def/ocr.html) 

#### 解答思路:
根据提示,从网页源代码里面找到了raw数据,我们需要从raw数据中找到字符们,从而修改url进入下一题.  
[raw数据](./2.txt)  
[python代码](./2.py)

### 3

[第3个谜题说明](http://www.pythonchallenge.com/pc/def/equality.html) 

#### 解答思路:
说明中只有一句话:One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.  
到这里毫无思路,无意间察看了网页源代码,又是一大片字符.  
以为和第二题的一样,其实不然.那么我们再次用第二题解析,这次发现结果有一大堆.  
然后观察输出的这一堆字符串,联系提示的那句话,恍然大悟:一个小写字母左右各有三个大写字母,我们写个正则解析.[A-Z]{3}([a-z]{1})[A-Z]{3}  
发现结果还是一堆.  
目前为止思路没错,我们再看提示的话,小写字母周围各有三个大写字母,这个EXACTLY暗示正好只有三个.我们修改一下正则表达式即可.[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]  

解析的结果为linkedlist,替代equality,跳出linkedlist.php,这才是最终答案.


[python代码](./3.py)


### 4

[第4个谜题说明](http://www.pythonchallenge.com/pc/def/linkedlist.html) 

#### 解答思路:


[python代码](./3.py)

