from manim import *

class SquareWithCircles(Scene):
    def construct(self):
        # 创建一个边长为4的正方形
        square = Square(side_length=4)
        square.move_to(ORIGIN)

        # 绘制正方形的4个顶点
        vertices = VGroup(*[Dot(point) for point in square.get_vertices()])

        # 绘制正方形的4个中点
        midpoints = VGroup(*[Dot(square.point_from_proportion(i * 0.25 + 0.125)) for i in range(4)])

        # 绘制对角线
        diagonals = VGroup(
            Line(square.get_vertices()[0], square.get_vertices()[2]),
            Line(square.get_vertices()[1], square.get_vertices()[3])
        )

        # 绘制中线
        midlines = VGroup(
            Line(square.get_top(), square.get_bottom()),
            Line(square.get_left(), square.get_right())
        )

        # 绘制外接圆
        circumcircle = Circle(radius=square.side_length * np.sqrt(2) / 2)
        circumcircle.move_to(square.get_center())

        # 绘制内切圆
        incircle = Circle(radius=square.side_length / 2)
        incircle.move_to(square.get_center())

        # 将所有元素添加到场景中
        self.play(Create(square))
        self.play(Create(vertices))
        self.play(Create(midpoints))
        self.play(Create(diagonals))
        self.play(Create(midlines))
        self.play(Create(circumcircle))
        self.play(Create(incircle))

        # 保持显示
        self.wait(2)

# 运行这个场景
if __name__ == "__main__":
    scene = Square