from manim import *
import os
config.background_color = "#2F7F5F" # 设置背景颜色

class CoverScene(Scene):
    cover_filename = "cover.png"
    logo = Text("@数理编程", font_size=36, font='Xingkai SC', weight="BOLD").to_edge(UP).to_edge(RIGHT)
    def construct(self):
        self.add_cover()
        self.wait(2)
    
    def font_list(self):
        print(Text.font_list())

    def save_cover(self, filename):
        self.remove(self.logo)
        self.wait(0.001)
        # 获取当前帧并保存为图片
        frame = self.camera.get_image()
        frame.save(filename)
        self.bring_to_front(self.logo)

    def add_cover(self):
        # # 设置背景颜色
        # self.camera.background_color = "#2F7F5F"
        if not os.path.isfile(self.cover_filename):
            self.add_logo()
            return
        # 加载 PNG 文件
        cover = ImageMobject(self.cover_filename)
        # 调整图像大小以适应屏幕
        cover.scale_to_fit_height(config.frame_height)
        # 将图像添加到场景中
        self.add(cover)
        # 保持封面显示0.5秒
        self.add_logo()
        self.wait(0.5)
        # 移除封面
        self.remove(cover)

    def add_logo(self):
        # self.font_list()
        self.add(self.logo)