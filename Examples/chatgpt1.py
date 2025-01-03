from manim import *

class ParallelLinesAndTransformingTriangle(Scene):
    def construct(self):
        # 创建第一条平行线（下边线）
        line1 = Line(start=LEFT, end=RIGHT)

        # 创建第二条平行线（上边线），向上平移
        line2 = Line(start=LEFT, end=RIGHT).shift(UP)

        # 创建三角形，底边在下边线（line1），顶点在上边线的最左边
        triangle = Polygon(LEFT, RIGHT, UP)

        # 绘制平行线和三角形
        self.play(Create(line1), Create(line2))
        self.play(Create(triangle))

        # 将三角形的顶点沿着上边线变形
        # 使用 TransformFromCopy 将三角形的顶点沿上边线移动
        triangle_copy = triangle.copy()  # 创建三角形的副本
        self.play(TransformFromCopy(triangle_copy, triangle_copy.shift(4 * RIGHT)))  # 向右平移

        # 等待3秒钟，方便查看结果
        self.wait(3)
