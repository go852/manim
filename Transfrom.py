from manim import *
from math import *

class Transfrom(Scene):
    def construct(self):
        circle1 = Circle(radius=2, color=ORANGE) # 半径：2
        square = Square(side_length=4, color=BLUE) # 边长：4
        circle2 = Circle(radius=square.side_length/2*sqrt(2)) # 外接圆半径
        p1 = circle1.point_at_angle(0) # 获取圆上指定角度的坐标点
        p2 = circle1.point_at_angle(PI/2) # 获取圆上指定角度的坐标点
        p3 = circle1.point_at_angle(PI) # 获取圆上指定角度的坐标点
        p4 = circle1.point_at_angle(PI*3/2) # 获取圆上指定角度的坐标点
        d1 = Dot(point=p1, color=RED) # 根据坐标点绘制点
        d2 = Dot(point=p2, color=RED)
        d3 = Dot(point=p3, color=RED)
        d4 = Dot(point=p4, color=RED)
        # square.surround(circle)
        self.play(Create(circle1))
        circle1.save_state() # 保存圆的状态
        self.wait(0.5)
        self.play(FadeIn(d1, d2, d3, d4))
        self.wait(0.5)
        self.play(Create(square))
        self.wait(0.5)
        self.play(Create(circle2))
        self.wait(0.5)
        vg = VGroup(square, d1, d2, d3, d4) # 创建组
        self.play(Rotate(vg, PI/4)) # 旋转制定角度
        self.wait(0.5)
        self.play(Rotate(vg, PI))
        self.wait()
        self.clear()
        self.wait(0.5)
        self.play(Restore(circle1)) # 恢复圆的状态
        self.wait(0.5)
        self.play(TransformFromCopy(circle1, square)) # 变形
        self.wait(0.5)