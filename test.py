
import simui
from simui import sim_class, sim_meth, sim_func, init_sim_global


"""
attr type的含义
None, "",  都会被认为是一行文本框
int 整形文本框

"""

@sim_func("这里测试一下全局函数", {"iPrior": 0})
def main():
    print("这里测试一下全局函数！！！！！！！！！！！！")

attr_list2 = [
    ["aaa", "全局属性aaa", None, {"iPrior": 4, "default": "EEEEEEEEEEEEEEEEEEEEEEEEEE"}],
    ["bbb", "全局属性bbb",  None, {"iPrior": -1}],
    ["a1", "",  "int(-100, 100)", {"iPrior": 0}],
]

gg = init_sim_global("gg", attr_list2)
# gg.aaa = "我爱编程"
# gg.bbb = "泪流满面"






attr_list = [
    ["m_AAA1", "属性1", None],
    ["m_Attr2", "",  None],
    ["m_Test1", "",  "ChildTest"],
]
@sim_class("BB",  attr_list)
class AA:
    @sim_meth("这里测试一下方法")
    def XXSSS(self):
        print("这里测试一下方法!!!!!!", self.gggg)

        def End():
            print("test end")
    
        global b
        
        def Dian():
            print("test dian")
        
        simui.show_sub_win(b, "test sub win", End, [[Dian, "点点点"]])


attr_list2 = [
    ["a1", "", "SimList"],
    ["float_test", "",  "float"],
    ["float_test2", "",  "float(-100, 1000)"],
    ["int_test", "",  "int"],
    ["int_test2", "",  "int(-100, 100)"],
    ["bool_test", "",  "bool"],
    ["box_test", "",  "box", {"options":["aaaa", "bbbb", "eeeee", "ddddddd"]}],
    ["box_test2", "",  "box", {"options":["aaaa", "bbbb", "eeeee", "ddddddd"], "show_options":["啊啊啊啊", "巴巴爸爸", "额鹅鹅鹅", "顶顶顶顶"]}],
    ["text_test", "",  "text"],
    ["image_test", "",  "image", ],
    ["image_test2", "",  "image", {"size":{300,300}}],
]
@sim_class("CCDD", attr_list2)
class EEE:
    @sim_meth("这里又是测试方法")
    def XsssssXSSS(self):
        print("这里又是测试方法!!!!!!手动阀手动阀")



attr_list4 = [
    ["int_testcc", "",  "int"],
    ["bool_testcc", "",  "bool"],
    ["image_testcc", "",  "image"],
]
@sim_class("子模块", attr_list4)
class ChildTest:
    @sim_meth("这里")
    def CCCCC(self):
        print("这里又是测试方法!!yes")



a = AA()
a.gggg = 1111
a.gggg1 = 1111
a.sdfnsdklfd = 22334
a.bind_json("__save/aaaa.json")

b = EEE()
b.bind_json("__save/bbbb.json")
simui.add_show_obj(a)

# simui.add_show_obj(b)



    
    
def cb():
    print("333333333333333333333!!!!!!!!!!!!!!!")
    gg.a1 = 77
    print("cb")
simui.add_timer("main", 3000, cb)
simui.show_ui("test ui")
