import sys
import os

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def addPorperty(content,porpertys):
    for porperty in porpertys:
        content += "\n@property (nonatomic,strong)NSString *" + porperty + ";"
    return content
def add_method_block(method_block_content):
    return "{\n" + method_block_content +"\n}"
def add_interface_init_with_porpertys(content,porpertys):
    method_interface = "-(instancetype)initWith"
    for porperty in porpertys:
        method_interface += porperty.capitalize() + ":(NSString *)" + porperty.capitalize() + " "
    method_interface = method_interface[:-1]
    method_interface += ";"
    content += method_interface
    return content
def add_interface_and_metod_init_with_porpertys(content,porpertys):
    content = add_interface_init_with_porpertys(content,porpertys)[:-1]
    method_content = "if (self = [super init]) {\n"
    for porperty in porpertys:
        method_content += "\nself." + porperty + " = " + porperty.capitalize() + ";"
    method_content += "\n}"
    method_content += "\nreturn self;"
    content += add_method_block(method_content)
    return  content
def h_file_content_add_import(file_content):
    import_library = "#import <Foundation/Foundation.h>\n"
    file_content += import_library
    return file_content
def h_file_content_add_class(file_content,file_name,super_file_name,porpertys):
    file_content += "\n@interface" + file_name + " : " + super_file_name + "\n"
    file_content = add_interface_init_with_porpertys(file_content,porpertys)
    file_content += "\n@end"
    return file_content

def create_h_file(file_path,file_name,super_file_name,porpertys):
    file_path_h = file_path + "/" + file_name + ".h"
    f_h = open(file_path_h ,'w')
    file_content = h_file_content_add_import("")
    file_content = h_file_content_add_class(file_content,file_name,super_file_name,porpertys)
    f_h.write(file_content)
    f_h.close()

def m_file_content_add_import(file_content,file_name):
    import_library = "#import " + "\""+file_name + ".h" + "\"" +"\n"
    file_content += import_library
    return file_content
def m_file_content_add_extension(file_content,file_name,porpertys):
    file_content += "\n@interface " + file_name + "()"
    file_content = addPorperty(file_content ,porpertys)
    file_content += "\n@end"
    return file_content
def m_file_content_add_implementation(file_content,file_name,porpertys):
    file_content += "\n@implementation " + file_name
    file_content = add_interface_and_metod_init_with_porpertys(file_content,porpertys)
    file_content += "\n@end"
    return file_content

def create_m_file(file_path,file_name,porpertys):
    file_path_m = file_path + "/" + file_name + ".m"
    f_m = open(file_path_m ,'w')
    file_content = ""
    file_content += m_file_content_add_import(file_content,file_name)
    file_content = m_file_content_add_extension(file_content,file_name,porpertys)
    file_content = m_file_content_add_implementation(file_content,file_name,porpertys)
    f_m.write(file_content)
    f_m.close()


def get_class_and_super_class_name():
    file_path = cur_file_dir()
    print("enter FileName:")
    file_name = raw_input()
    print("super FileName:")
    super_file_name = raw_input()
    return (file_path,file_name,super_file_name)

def get_class_porperty():
    porperty_array = []
    porperty_name = ""
    while(porperty_name != "Exit"):
        print("enter porperty:(press \"Exit\" exit)")
        porperty_name = raw_input()
        porperty_array.append(porperty_name)
    return porperty_array[:-1]


file_info_tuple =get_class_and_super_class_name()
porpertys = get_class_porperty()
create_h_file(file_info_tuple[0],file_info_tuple[1],file_info_tuple[2],porpertys)
print(porpertys)
create_m_file(file_info_tuple[0],file_info_tuple[1],porpertys)
