from manim import *

class SquareAndCirclesWithColoredPoints(Scene):
    def construct(self):
        # 创建一个边长为4的绿色正方形
        square = Square(side_length=4, color=GREEN)

        # 计算正方形对角线的长度（对角线公式：sqrt(2) * 边长）
        diagonal_length = np.sqrt(2) * square.get_side_length()

        # 绘制外接圆，半径为对角线长度的一半，颜色为蓝色
        circumscribed_circle = Circle(radius=diagonal_length / 2, color=BLUE)
        circumscribed_circle.move_to(square.get_center())  # 外接圆与正方形中心对齐

        # 绘制内切圆，半径为正方形边长的一半，颜色为红色
        inscribed_circle = Circle(radius=square.get_side_length() / 2, color=RED)
        inscribed_circle.move_to(square.get_center())  # 内切圆与正方形中心对齐

        # 在正方形的四个顶点绘制橙色点
        vertices = [square.get_vertices()[i] for i in range(4)]
        vertex_dots = [Dot(point=vertex, color=ORANGE) for vertex in vertices]

        # 在每条边的中点绘制橙色点
        midpoints = [
            (square.get_vertices()[0] + square.get_vertices()[1]) / 2,
            (square.get_vertices()[1] + square.get_vertices()[2]) / 2,
            (square.get_vertices()[2] + square.get_vertices()[3]) / 2,
            (square.get_vertices()[3] + square.get_vertices()[0]) / 2,
        ]
        midpoint_dots = [Dot(point=midpoint, color=ORANGE) for midpoint in midpoints]

        # 动画：先绘制正方形，再绘制外接圆、内切圆和点
        self.play(Create(square))
        self.play(Create(circumscribed_circle))
        self.play(Create(inscribed_circle))
        self.play(*[Create(dot) for dot in vertex_dots])  # 绘制顶点上的点
        self.play(*[Create(dot) for dot in midpoint_dots])  # 绘制边的中点上的点

        # 等待3秒钟，方便查看结果
        self.wait(3)
