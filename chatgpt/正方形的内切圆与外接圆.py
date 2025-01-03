from manim import *

class SquareAndCircles(Scene):
    def construct(self):
        # 创建一个边长为4的正方形，颜色为绿色
        square = Square(side_length=4, color=GREEN)
        self.play(Create(square))

        # 绘制正方形的四个顶点，颜色为橙色
        vertices = square.get_vertices()
        for vertex in vertices:
            dot = Dot(point=vertex, color=ORANGE)
            self.add(dot)

        # 绘制每条边的中点，颜色为橙色
        for i in range(4):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % 4]
            mid_point = (p1 + p2) / 2
            dot = Dot(point=mid_point, color=ORANGE)
            self.add(dot)

        # 画正方形的黄色对角线
        diagonal1 = DashedLine(vertices[0], vertices[2], color=YELLOW)
        diagonal2 = DashedLine(vertices[1], vertices[3], color=YELLOW)
        self.add(diagonal1, diagonal2)

        # 计算对角线的长度，作为外接圆的直径
        diagonal_length = np.linalg.norm(vertices[0] - vertices[2])

        # 画外接圆，颜色为蓝色
        circumscribed_circle = Circle(radius=diagonal_length / 2, color=BLUE)
        circumscribed_circle.move_to(square.get_center())
        self.play(Create(circumscribed_circle))

        # 画外接圆的半径线段，并标注半径为r_o
        radius_line_outer = Line(square.get_center(), vertices[0], color=BLUE)
        self.play(Create(radius_line_outer))
        radius_label_outer = MathTex("r_o", color=WHITE).next_to(radius_line_outer, UP)
        self.play(Write(radius_label_outer))

        # 画正方形的内切圆，颜色为红色
        inscribed_circle = Circle(radius=2, color=RED)  # 内切圆的半径是边长的一半
        inscribed_circle.move_to(square.get_center())
        self.play(Create(inscribed_circle))

        # 画内切圆的半径线段，并标注半径为r_i，紫色线段与外接圆半径增加45度角
        # 计算45度的旋转矩阵
        radius_line_inner = Line(square.get_center(), vertices[1], color=PURPLE)
        radius_line_inner.shift(LEFT * 0.5)  # 让紫色线段偏移一些位置，形成角度
        radius_label_inner = MathTex("r_i", color=WHITE).next_to(radius_line_inner, RIGHT)
        self.play(Create(radius_line_inner), Write(radius_label_inner))

        # 画两条正方形的中线，分别是水平和垂直方向的中线
        horizontal_line = Line(LEFT * 2, RIGHT * 2, color=WHITE)
        vertical_line = Line(UP * 2, DOWN * 2, color=WHITE)
        self.play(Create(horizontal_line), Create(vertical_line))
