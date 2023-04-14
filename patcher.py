import marshal
import types
import dis
import sys

HEADER = ""

def write_pyc_file(code_obj, pyc_file):
    code_bytes = marshal.dumps(code_obj)

    with open(pyc_file, "wb") as file:
        file.write(HEADER + code_bytes)
    
def read_pyc_file(pyc_file):
    global HEADER

    with open(pyc_file, "rb") as file:
        HEADER = file.read(16)
        file.seek(16)
        
        return marshal.load(file)
    
if __name__ == "__main__":
    if (sys.version_info.major, sys.version_info.minor) == (3, 11):
        print("Python 3.11 is required for patching ttClient.")
        sys.exit(0)

    if len(sys.argv) != 3:
        print("Usage: python patcher.py <file> <output file>") 
        sys.exit(0)
    
    filename = sys.argv[1]
    output_file = sys.argv[2]

    code_obj = read_pyc_file(filename)
    print(f"File: {filename}")

    print("Patching constant values...")

    new_const_list = list(code_obj.co_consts)

    new_const_list[code_obj.co_consts.index('cls & title ttClient 1.4')] = 'cls & title ttClient 1.4 [CRACKED]'
    new_const_list[code_obj.co_consts.index('\x1b]0;ttClient 1.02x07')] = '\x1b]0;ttClient 1.02x07 [CRACKED]'
    new_const_list[code_obj.co_consts.index('              ttClient 1.4,         .gg/ttClient')] = '              ttClient 1.4,         [CRACKED]'
    new_const_list[code_obj.co_consts.index('                    Made by neiry & salih6169 ----- iletişim için ne1ry#1881: ')] = '                    CRACKED BY XXXX -------------------- '

    new_entry_function_code = """def B7():
    global An, Ao, Y

    try:
        Y(AC.RED + '                     [X] ' + AC.LIGHTBLUE_EX + "Giriş yapmak için 1'e Basınız!")
        A = C7(AC.RED + '                     -->  ' + AC.LIGHTBLUE_EX)

        if A == '1':
            #An = C7(AC.RED + '                     lisans anahtarınızı girin: ' + AC.LIGHTBLUE_EX)
            #AS.license(An)
            An = "CRACKED"
            Ao = "INF"
            Y(AC.GREEN + '                     Giriş başarılı!')

        else:
            Y("\\n                     Lütfen 1'e basınız.")
            E.sleep(1)
            d.system('cls')
            B7()
            
    except KeyboardInterrupt:
        d._exit(0) # d._exit()
    except:
        raise"""

    new_entry_function = compile(new_entry_function_code, code_obj.co_filename, "exec").co_consts[0].replace(co_firstlineno = 112)
    
    new_const_list[85] = new_entry_function

    
    gui_class = code_obj.co_consts[-3]

    retranslate_ui_method = gui_class.co_consts[2]
    new_retranslate_ui_method_const_list = list(retranslate_ui_method.co_consts)
    new_retranslate_ui_method_const_list[retranslate_ui_method.co_consts.index('Made By Neiry&Salih6169')] = "CRACKED BY XXXX"
    new_retranslate_ui_method = retranslate_ui_method.replace(co_consts = tuple(new_retranslate_ui_method_const_list))

    discordgg_method = gui_class.co_consts[-9]
    new_discordgg_method_const_list = list(discordgg_method.co_consts)
    new_discordgg_method_const_list[discordgg_method.co_consts.index('https://discord.gg/24XcWXKCcT')] = ''
    new_discordgg_method = discordgg_method.replace(co_consts = tuple(new_discordgg_method_const_list))

    youtubegg_method = gui_class.co_consts[-8]
    new_youtubegg_method_const_list = list(youtubegg_method.co_consts)
    new_youtubegg_method_const_list[youtubegg_method.co_consts.index('https://www.youtube.com/@neiry3910/featured')] = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    new_youtubegg_method = youtubegg_method.replace(co_consts = tuple(new_youtubegg_method_const_list))

    new_gui_class_const_list = list(gui_class.co_consts)
    new_gui_class_const_list[2] = new_retranslate_ui_method
    new_gui_class_const_list[-9] = new_discordgg_method
    new_gui_class_const_list[-8] = new_youtubegg_method

    new_gui_class = gui_class.replace(co_consts= tuple(new_gui_class_const_list))
    
    new_const_list[-3] = new_gui_class

    print("All necessary constants has been patched!")

    print("Editing bytecode...")

    new_co_code = code_obj.co_code.replace(b"\x02\x00\x65\x4b\x64\x4f\x64\x50\x64\x51\x64\x52\x02\x00\x65\x60\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xac\x53\xa6\x05\x00\x00\xab\x05\x00\x00\x00\x00\x00\x00\x00\x00\x5a\x61", b"").replace(b"\x02\x00e)\x02\x00efee\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]\x9bZgeeeg\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00dV\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00Zh\x02\x00eTji\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00e\x1aeeeg\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00dW\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0j\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00dX\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Zkeeeg\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00dY\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00al\x02\x00e\x1at\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00alt\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00dZz\x0b\x00\x00ZmemdZz\x0b\x00\x00Zn\x02\x00eoen\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Zn\x02\x00e3e=jp\x00\x00\x00\x00\x00\x00\x00\x00d[t\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02z\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c\x9c", b"").replace(b"\x65\x61\x6a\x63\x00\x00\x00\x00\x00\x00\x00\x00\x6a\x64\x00\x00\x00\x00\x00\x00\x00\x00\x5a\x65", b"").replace(b"\x65\x61\xa0\x72\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x5a\x73", b"").replace(b"es\x80\x03d]Ztn+\x02\x00e)\x02\x00efes\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]\x16Zgeteseg\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00d^\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00d_z\x00\x00\x00z\r\x00\x00Z\x74\x8c\x17", b"").replace(b"\x02\x00\x65\x4b\x65\x03\x64\xdd\x64\xde\x64\xdf\x02\x00\x65\x60\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xac\x53\xa6\x05\x00\x00\xab\x05\x00\x00\x00\x00\x00\x00\x00\x00\x5a\x61", b"").replace(b"\x64\x31\x64\x35\x6c\x4a\x6d\x4b\x5a\x4b\x01\x00", b"")

    print("Bytecode has been edited!")

    print("Initializing code object...")

    new_codeobj = code_obj.replace(co_consts = tuple(new_const_list), co_code = new_co_code)

    print("Code object was initialized.")

    print("Writing to pyc file...")

    write_pyc_file(new_codeobj, output_file)

    print("Writed to pyc file!")
    print("Operation successful!")

