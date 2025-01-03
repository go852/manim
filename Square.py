from manim import *

class DotSample(Scene):
    def construct(self):
        t1 = Text("绘制正方形", color="#00FF00", font_size=36, font='Songti SC')
        t2 = Text("删除正方形", color="#00FF00", font_size=36, font='Songti SC')        
        t3 = Text("重绘正方形", color="#00FF00", font_size=36, font='Songti SC')
        s = Square(side_length=2, color=BLUE)

        self.play(Write(t1.next_to([0, 2, 0], UP)))
        self.play(Create(s))
        self.wait(1)

        self.remove(t1)
        self.play(Write(t2.next_to([0, 2, 0], UP)))
        self.remove(s)
        self.wait(1)
        
        self.remove(t2)
        self.play(Write(t3.next_to([0, 2, 0], UP)))       
        self.play(Create(s))
        self.wait(1)
