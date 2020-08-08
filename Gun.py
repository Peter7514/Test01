class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹了。。。")
            return
        self.bullet_count -= 1
        print("%s突突突突。。%d" % (self.model, self.bullet_count))


ak47 = Gun("Ak47")

