"""
写一个Manim程序
创建包含9*9乘法表的计算结果
表格字号设置60
表格需要所有的边框
边框粗细为2
表格水平和垂直间距均为1.2
表格放大0.4倍
表格对齐到左边
等待2秒
左上角4个单元格填充橙色
"""
from manim import *
config.background_color = "#2F7F5F" # 设置背景颜色

from manim import *

class MultiplicationTable(Scene):
    def construct(self):
        # 创建一个9x9的表格
        table = Table(
            [[f"{i*j}" for j in range(1, 10)] for i in range(1, 10)],
            include_outer_lines=True,  # 包含所有边框
            line_config={"stroke_width": 2},  # 边框粗细为2
            element_to_mobject_config={"font_size": 60},  # 字号设置为60
            v_buff=1.2,  # 垂直间距为1.2
            h_buff=1.2,  # 水平间距为1.2
        )

        # 缩放表格为0.4倍
        table.scale(0.3)

        # 将表格对齐到左边
        table.to_edge(LEFT)

        # 添加表格到场景中
        self.add(table)

        diagonal_line_1 = Line(table.get)
        # 选择左上角的4个单元格及其内容
        selected_cells = VGroup()
        for i in range(1,3):
            for j in range(1,3):
                cell = table.get_cell((i,j))
                selected_cells.add(cell)
                # 添加单元格的内容
                selected_cells.add(cell.get_data())
        # 向右移动6个单位
        self.play(selected_cells.animate.shift(RIGHT*6))
        self.wait(2)

# 运行场景
if __name__ == "__main__":
    scene = MultiplicationTable()
    scene.render()