from manim import *

class SquareExample(Scene):
    square = Square()

    def construct(self):
        # 改变正方形的属性
        square = self.square
        square.set_fill(BLUE, opacity=0.5)  # 设置填充颜色和透明度
        square.set_stroke(RED, width=4)     # 设置边框颜色和宽度
        self.play(Create(square))           # 动画创建正方形
        self.wait()
        self.play(square.animate.scale(2))
        self.wait()
        self.play(square.animate.shift(UP*2))
        self.wait()
        # 显示边长与对角线长度
        text1 = Text(f"Side Length: {self.square.side_length:.2f}")
        text2 = Text(f"Diagonal Length: {self.get_diagonal_length():.3f}")
        text3 = Text(f"{square.get_vertices()}")
        text1.to_edge(DOWN)
        text2.next_to(text1, UP)
        text3.next_to(text2, UP)
        self.add(text1, text2, text3, square)
        self.wait(5)



    def get_diagonal_length(self):
        # 计算对角线长度
        diagonal_length = self.square.side_length * np.sqrt(2)
        return diagonal_length
