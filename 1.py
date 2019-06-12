
def deal_one(strings):
    """
        一个简单的加密算法,加密过程如下:输入一个英文字母,向后移动两位,输入移动后的字母.
        比如 a->c, z->b
    """
    result = []
    for char in strings:
        if char.isalpha():
            order = ord(char) + 2
            char = chr(order) if order < (26+97) else chr(order%(26+96)+96)
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    s = """
    g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
    bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
    sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
    """
    result = deal_one(s)
    print(result)

if __name__ == "__main__":
    main()