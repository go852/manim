from manim import *

########################################
# x_range = []，x轴的取值范围
# include_tip = True or False，是否显示箭头
# tip_width = 0.2, 箭头宽度
# tip_height = 0.2, 箭头高度
# include_ticks = True # 显示刻度
# tick_size = 0.1, # 刻度线长度，浮点型
# include_numbers = True, 包括刻度数值
# font_size = 0.5, # 刻度数值字体大小
# length = 1 # 数轴的长度
########################################
class pNumberLine(Scene):
    def construct(self):
        l1 = NumberLine(
            x_range = [-9, 9], # x轴的取值范围
            include_tip = True, # 是否显示箭头
            tip_width = 0.2, # 箭头宽度
            tip_height = 0.2, # 箭头高度
            tip_shape = StealthTip, # 箭头形状，StealthTip：尖箭头
            include_ticks = True, # 显示刻度线
            tick_size = 0.1, # 刻度线长度，浮点型
            include_numbers = True, # 是否包含刻度数值
            line_to_number_buff = 0.2, # 刻度数值与数轴的距离
            font_size = 14, # 刻度数值字体大小
            unit_size = 2, #
            length = 12, # 数轴长度
            stroke_width = 2, # 数轴线粗细
            color = BLUE # 颜色
        )
        self.add(l1)
        self.play(Create(l1))
