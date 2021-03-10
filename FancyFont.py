import pyperclip
import tkinter
import threading
import time


abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

fonts = {
    'double' : '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘',
    'old' : '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ1234567890',
    'old_bold' : '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅1234567890',
    'handwriting' : '𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢',
    'handwriting_bold' : '𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩1234567890',
    'spaced' : 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０',
    'small_blocks' : '🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉1234567890',
    'curved_blocks' : '🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉1234567890',
    'circles' : 'ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ①②③④⑤⑥⑦⑧⑨⓪',
    'squiggle' : 'ค๒ς๔єŦﻮђเןкɭ๓ภ๏קợгรՇยשฬאץչค๒ς๔єŦﻮђเןкɭ๓ภ๏קợгรՇยשฬאץչ1234567890',
    'cherokee' : 'ᏗᏰፈᎴᏋᎦᎶᏂᎥᏠᏦᏝᎷᏁᎧᎮᎤᏒᏕᏖᏬᏉᏇጀᎩፚᏗᏰፈᎴᏋᎦᎶᏂᎥᏠᏦᏝᎷᏁᎧᎮᎤᏒᏕᏖᏬᏉᏇጀᎩፚ1234567890',
    'russia' : 'ΛBᄃDΣFGΉIJKᄂMПӨPQЯƧƬЦVЩXYZΛBᄃDΣFGΉIJKᄂMПӨPQЯƧƬЦVЩXYZ1234567890',
    'lines' : '₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ1234567890',
    'japan' : 'ﾑ乃ᄃり乇ｷムんﾉﾌズﾚﾶ刀のｱゐ尺丂ｲひ√Wﾒﾘ乙ﾑ乃ᄃり乇ｷムんﾉﾌズﾚﾶ刀のｱゐ尺丂ｲひ√Wﾒﾘ乙1234567890',
    'china' : '卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙1234567890',
    'armen' : 'ąҍçժҽƒցհìʝҟӀʍղօքզɾʂէմѵա×վՀȺβ↻ᎠƐƑƓǶįلҠꝈⱮហටφҨའϚͲԱỼచჯӋɀ𝟙ϩӠ५ƼϬ7𝟠९⊘',
    'mix' : '𝒶𝒷¢𝕕єⓕᎶʰίנＫＬ𝓜η𝓞ƤɊ𝐫𝐬𝓉𝕌𝕍𝕎ⓧⓨＺⒶᗷc𝕕ᗴᶠᎶнιנＫℓ𝓂𝐧ｏρ𝔮ŕѕт𝐔νｗx𝔂z１➁❸４➄➅➆➇９０',
    'curved' : 'ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭YᘔᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ1234567890',
    'fuzzy' : ['a░', 'b░', 'c░', 'd░', 'e░', 'f░', 'g░', 'h░', 'i░', 'j░', 'k░', 'l░', 'm░', 'n░', 'o░', 'p░', 'q░', 'r░', 's░', 't░', 'u░', 'v░', 'w░', 'x░', 'y░', 'z░', 'A░', 'B░', 'C░', 'D░', 'E░', 'F░', 'G░', 'H░', 'I░', 'J░', 'K░', 'L░', 'M░', 'N░', 'O░', 'P░', 'Q░', 'R░', 'S░', 'T░', 'U░', 'V░', 'W░', 'X░', 'Y░', 'Z░','1░', '2░', '3░', '4░', '5░', '6░', '7░', '8░', '9░', '0░']
}

font_names = []
for key in fonts.keys():
    font_names.append(key)


def generate():
    global changed_text
    global text_entry
    global fontvar

    while True:
        font_name = fontvar.get().strip()

        text = text_entry.get("1.0", tkinter.END)

        if text == 'fonts':
            for font in fonts.keys():
                print(font)
        else:
            for i in range(0,len(abc)):
                text = text.replace(abc[i], fonts[font_name][i])

            changed_text.delete('1.0', tkinter.END)
            changed_text.insert(tkinter.END, text + '\n')

        time.sleep(0.3)

def copy():
    global changed_text

    pyperclip.copy(changed_text.get('1.0', tkinter.END))

top = tkinter.Tk()
top.geometry('420x700')
top.configure(bg='powder blue')

title = tkinter.Label(text='Fancy Fonts', font=("Courier", 30), bg='powder blue')
title.pack()
tkinter.Label(bg='powder blue').pack() #Spacer
prompt = tkinter.Label(text="Type some text", font=("Courier", 10), bg='powder blue')
prompt.pack()
text_entry = tkinter.Text(font=("fsdfsdfs", 15), height=10, bg='azure')
text_entry.pack()

tkinter.Label(bg='powder blue').pack() 

fontvar = tkinter.StringVar(top)
fontvar.set(font_names[0])
opt = tkinter.OptionMenu(top, fontvar, *font_names)
opt.config(bg='khaki1', activebackground='khaki2')
opt["menu"].config(bg='powder blue', activebackground='khaki2')
opt.pack()

changed_text = tkinter.Text(font=("fsdfsdfs", 15), height=10)
changed_text.pack()


coppy_button = tkinter.Button(text="Copy text", command=copy, bg='khaki1', activebackground='khaki2')
coppy_button.pack()
tkinter.Label(bg='powder blue').pack() #Spacer


thread = threading.Thread(target=generate)
thread.start()


top.mainloop()
