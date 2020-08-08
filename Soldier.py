from Gun import ak47
import Gun


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:  # is 身份运算符用来判断引用对象是否为同一个
            print("%s还没有枪" % self.name)
            return
        print("冲啊。。%s" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


xusanduo = Soldier("许三多")
# print(xusanduo.gun)
xusanduo.gun = ak47
# print(xusanduo.gun)
xusanduo.fire()
