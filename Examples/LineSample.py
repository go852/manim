from manim import *

BACKGROUND_COLOR = "#2F7F5F"
config.background_color = BACKGROUND_COLOR # 设置背景颜色

class LineSample(Scene):
    def construct(self):

        start = LEFT * 2
        end = RIGHT * 2

        # print(LEFT, RIGHT, UP, DOWN, ORIGIN)
        L1 = DashedLine(start, end, color=ORANGE)
        L2 = DashedLine(start, end, dash_length=0.5, color=ORANGE)
        L3 = DashedLine(start, end, dash_length=1, dashed_ratio=0.8, color=ORANGE)
        L4 = DashedLine(start, end, dashed_ratio=0.1, color=ORANGE)
        t1 = Text("Line 1")
        t2 = Text("Line 2")
        t3 = Text("Line 3")
        t4 = Text("Line 4")
        
        self.play(AddTextLetterByLetter(t1, rate_func=lambda t: t))
        self.wait(1)
        self.play(Create(L1.next_to(t1, DOWN)))
        self.wait(1)

        self.remove(t1)
        self.remove(L1)
        self.play(AddTextLetterByLetter(t2, rate_func=lambda t: t))
        self.play(Create(L2.next_to(t2, DOWN)))

        self.remove(t2)
        self.remove(L2)
        self.play(AddTextLetterByLetter(t3, rate_func=lambda t: t))
        self.play(Create(L3.next_to(t3, DOWN)))

        self.remove(t3)
        self.remove(L3)
        self.play(AddTextLetterByLetter(t4, rate_func=lambda t: t))
        self.play(Create(L4.next_to(t4, DOWN)))
        self.wait(2)
