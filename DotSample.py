from manim import *

config.background_color = BLUE_E # 设置背景颜色

class DotSample(Scene):
    def construct(self):
        # 设置背景颜色
        # self.camera.background_color = BLUE_E
        t1 = Text("如何用一笔画4条直线段连接以下9个点", color=WHITE, font_size=36, font='Songti SC')
        dots = []
        i = 1
        for x in range(-1, 2):
            for y in range(-1, 2):
                dots.append(Dot([x, y, 0], color=ORANGE, radius=0.1))
                i += 1
        t2 = Text("思考5秒...", color=WHITE, font_size=36, font='Songti SC')
        t3 = Text("换成用3条直线段连接4个点，再试一下...", color=WHITE, font_size=36, font='Songti SC')
        t4 = Text("看明白了吗？", color=WHITE, font_size=36, font='Songti SC')
        l21 = Line([-1, 1, 0], [1, 1, 0], color=ORANGE, z_index=0)
        l22 = Line([1, 1, 0], [-1, -1, 0], color=ORANGE, z_index=0)
        l23 = Line([-1, -1, 0], [-1, 1, 0], color=ORANGE, z_index=0)
        l31 = Line([-1, 1, 0], [2, 1, 0], color=ORANGE, z_index=0)
        l32 = Line([2, 1, 0], [-1, -2, 0], color=ORANGE, z_index=0)
        l33 = Line([-1, -2, 0], [-1, 1, 0], color=ORANGE, z_index=0)
        l34 = Line([-1, 1, 0], [1, -1, 0], color=ORANGE, z_index=0)

        self.play(AddTextLetterByLetter(t1.next_to([0, 2, 0], UP)), runtime=0.1)
        # print(Text("").font_list()) # 获得可用字体列表
        # 绘制 9个点
        for dot in dots:
            self.add(dot)

        self.play(AddTextLetterByLetter(t2.next_to([0, -2, 0], DOWN), runtime=0.1))
        self.wait(5)
        for i in [8, 7, 6, 3, 0]:
            self.remove(dots[i])
        self.remove(t1)
        self.play(AddTextLetterByLetter(t3.next_to([0, 2, 0], UP)))


        self.play(Create(l21), run_time=2, z_index=0)
        self.play(Create(l22), run_time=2, z_index=0)
        self.play(Create(l23), run_time=2, z_index=0)
        self.remove(t2)

        self.play(AddTextLetterByLetter(t4.next_to([0, -2, 0], DOWN)))
        self.wait(5)

        self.remove(t3)
        self.wait(0.5)
        self.play(AddTextLetterByLetter(t1.next_to([0, 2, 0], UP)))
        self.wait(0.5)
        self.remove(l23)
        self.remove(l22)
        self.remove(l21)
        self.wait(0.1)

        for i in [0, 3, 6, 7, 8]:
            self.play(FadeIn(dots[i], runtime=0.1))
        self.play(Create(l31), run_time=2, z_index=0)
        self.play(Create(l32), run_time=2, z_index=0)
        self.play(Create(l33), run_time=2, z_index=0)
        self.play(Create(l34), run_time=2, z_index=0)
