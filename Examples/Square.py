from manim import *

class SquareSample(Scene):
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
        self.clear()

        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)
        self.play(Create(square_1), Create(square_2), Create(square_3))
        self.wait(2)

        vs = square_3.get_vertices()
        print(*vs)
        for v in vs:
            print(*v)
        self.wait()