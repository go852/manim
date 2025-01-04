from manim import *

class SquareExample(Scene):
    def construct(self):
        # 创建一个默认的正方形
        square = Square()
        
        # 改变正方形的属性
        square.set_fill(BLUE, opacity=0.5)  # 设置填充颜色和透明度
        square.set_stroke(RED, width=4)     # 设置边框颜色和宽度
        self.play(Create(square))           # 动画创建正方形
        self.wait()
        self.play(square.animate.scale(2))
        self.wait()
        self.play(square.animate.shift(UP*2))
        self.wait()
