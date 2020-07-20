binf = "utf8tocp932.bin"

def readbin():
    u2 = 0
    u3 = 0
    with open(binf, mode='rb') as f:
        u1 = f.read(1)
        # 1byte目を数値化 3byteか？
        i1 = ord(u1)
        if  i1 >= 0xe0 and i1 <= 0xef:
            u2 = f.read(1)
            u3 = f.read(1)
        # 2byte    
        if  i1 >= 0xc0 and i1 <= 0xdf:
            u2 = f.read(1)
        print(hex(i1))
        u2 = f.read(1)
        u3 = f.read(1)
        s1 = f.read(1)
        s2 = f.read(1)
    print(u1,u2,u3)
    print(s1,s2)

#
# sjisをi.utf8にする。
#
# baはbytearray
#
def cp932_to_utf8(ba):
    sjis = ba.decode('cp932',errors="ignore")
    utf = sjis.encode('utf-8')
    return utf
0x81
#
# sjis すべての全角文字をutf8に変換する。
#
# sjis  上位 0x81 - 0x9f と 0xe0 - 0xef 
#       下位 0x40 - 0x7e と 0x80 - 0xfc
#
#

def main():
    #
    # sjisをいれるためのbytearray
    #
    ba = bytearray(2)
    #
    # 変換テーブル書き込み用ファイルをバイナリでオープンする。
    #
    f = open(binf,'wb')
    #
    # sjis 上位開始バイト
    #
    s1 = 0x81
    while s1 <= 0xef:
        #
        # sjis が存在しないコードは除く
        #
        if s1 >= 0xa0 and s1 <= 0xdf :
            s1 = s1 + 1
            continue
        #
        # sjis 下位開始バイト
        #
        s2 = 0x40
        while s2 <= 0xfc:
            #
            # sjis が存在しないコードは除く
            #
            if s2 == 0x7f :
                s2 = s2 + 1
                continue
            #
            # bytearrayにsjisをいれる
            #
            ba[0] = s1
            ba[1] = s2
            #
            # sjisをutf8に変換する
            #
            utf = cp932_to_utf8(ba)
            #
            # バイナリをファイルに書き込む
            #
            utflen = len(utf)
            if utflen == 3 :
                f.write(utf)
                f.write(ba)
            s2 = s2 + 1
        s1 = s1 + 1
    f.close()

main()
