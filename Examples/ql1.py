from manim import *

class AreaRelationshipInRectangle(Scene):
    def construct(self):
        # 创建长方形和正方形
        rectangle = Rectangle(width=6, height=4, color=BLUE, fill_opacity=0.3)
        square = Square(side_length=3, color=GREEN, fill_opacity=0.5)

        # 定位正方形到长方形内的一个位置
        square.move_to(rectangle.get_center() + UP * 0.5)

        # 添加长方形和正方形到场景
        self.play(Create(rectangle))
        self.play(Create(square))

        # 添加题目说明
        question = Tex(
            r"已知长方形面积为 $6 \times 4$，正方形面积为 $3^2$，"
            r"请计算正方形与长方形面积差是多少?"
        )
        question.scale(0.8)
        question.to_edge(UP)
        self.play(Write(question))

        # 动画：显示长方形的面积和正方形的面积
        area_rect = Tex(r"长方形面积 = $6 \times 4 = 24$").next_to(rectangle, DOWN)
        area_square = Tex(r"正方形面积 = $3^2 = 9$").next_to(area_rect, DOWN)
        
        self.play(Write(area_rect))
        self.play(Write(area_square))

        # 等待3秒
        self.wait(3)
