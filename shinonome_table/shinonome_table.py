import json

jis_dict = {}
with open('JIS0208.TXT') as f:
    s = f.read()
    lines = s.splitlines()
    i = 0
    while lines[i][0] == "#":#先頭のコメントを無視する
        i = i + 1
    
    for line in lines[i:]:
        code = line.split("\t")
        jis_dict[str(code[1][2:])] = chr(int(code[2],16)) 

font_dict = {}
with open('shnmk16.txt') as f:
    s = f.read()
    fonts = s.split("STARTCHAR")[1:]#1文字ずつに分割する
    for font in fonts:
        code = font.splitlines()[0][1:].upper()#文字コードを大文字に変換する
        data = (font.split("BITMAP")[1]).splitlines()[1:17]
        for i in range(16):#16の行に0xを付与する
            data[i] = "0x" + data[i]
        
        font_dict[jis_dict[code]] = data

#ファイル出力 
json_str = json.dumps(font_dict, indent=2)
with open('font_dict.js', 'w',encoding='utf-8') as f:
    f.write("var font_dict={};\n".format(json_str))

