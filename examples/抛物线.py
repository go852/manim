from manim import *

class PlotGraph(Scene):
    def construct(self):
        # 创建等距的坐标轴
        axes = Axes(
            x_range=[-3, 3, 1],  # x轴范围从-3到3，步长为1
            y_range=[0, 9, 1],   # y轴范围从0到9，步长为1
            x_length=4,          # x轴长度
            y_length=6,          # y轴长度（与x轴等距）
            axis_config={"color": BLUE},
        )

        # 创建y = x^2的曲线
        graph = axes.plot(lambda x: x**2, color=YELLOW)

        # 添加坐标轴和曲线的标签
        graph_label = axes.get_graph_label(graph, label='y=x^2')

        # 创建坐标轴和曲线的动画
        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Write(graph_label, lag_ratio=0.2))

        # 保持显示
        self.wait(2)

# 运行代码
if __name__ == "__main__":
    scene = PlotGraph()
    scene.render()