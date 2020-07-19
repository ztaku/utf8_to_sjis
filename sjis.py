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
    sjis = ba.decode('cp932')
    utf = sjis.encode('utf-8')
    return utf

def sjisarea():
    f = open("bin.bin",'w')
    s1 = 0x81
    while s1 <= 0xef:
        if ( s1 >= 0xa0 and s1 < 0xdf ) or ( s1 >= 0xf0 ) :
            s1 = s1 + 1
            continue:
        s2 = 0x40
        while s2 <= 0xfc:
            if s2 == 0x7f or ( s2 >= 0xfd ):
                s2 = s2 + 1
                continue
            h1 = hex(s1)
            h2 = hex(s2)
            str = h1+h2+"\n"
            f.write(str)
            s2 = s2 + 1
        s1 = s1 + 1
    f.close()

def main():
    ba = bytearray(b'ba')
    ba[0] = 0x81
    ba[1] = 0x42
    print(hex(ba[0]),hex(ba[1]))
    utf = cp932_to_utf8(ba)
    print(utf)
    print(utf[0],utf[1],utf[2])
    with open(binf, mode='wb') as f:
        f.write(utf)
        f.write(ba)

#readbin()
sjisarea()

