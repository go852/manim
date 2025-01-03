from manim import *

config.background_color = "#2F7F5F" # 设置背景颜色

class CurtainSample(Scene):
    def construct(self):
        offset = [-2, -1, 0]
        nud = 1.5 # number of up to down
        nlr = 4 # number of lef to right
        fs = 48 # font_size
        bfs = 60 # big font size
        sfs = 32 # small font size
        
        l1 = Line(LEFT*nlr, RIGHT*nlr).shift(UP*nud + offset)
        l2 = l1.copy().shift(DOWN*2*nud)
        pa = DOWN*nud + LEFT*nlr/2 + offset
        pb = DOWN*nud + RIGHT*nlr/2 + offset
        pc = UP * nud + LEFT * (nlr - 1) + offset
        pd = UP * nud + RIGHT * (nlr - 1) + offset
        pe = l2.get_projection(pc) # 获取垂足
        pf = l2.get_projection(pd) # 获取垂足
        d1 = Dot(pa)
        d2 = Dot(pb)
        d3 = Dot(pc)
        d4 = Dot(pd)

        t0 = Text("拉窗帘模型", font_size=bfs, weight=BOLD).to_edge(UP)
        ta = Text("A", font_size=sfs).next_to(d1, DOWN)
        tb = Text("B", font_size=sfs).next_to(d2, DOWN)
        tc = Text("C", font_size=sfs).next_to(d3, UP)
        td = Text("D", font_size=sfs).next_to(d4, UP)

        tr1 = Polygon(pa, pb, pc, fill_color=GREEN, fill_opacity=0.5)
        tr2 = Polygon(pa, pb, pd, fill_color=ORANGE, fill_opacity=0.5)
        l3 = DashedLine(pc, pe)
        l4 = DashedLine(pd, pf)
        bl0 = BraceLabel(Line(pa, pb), text="a", brace_direction=DOWN, color= WHITE, buff=0.1)
        bl1 = BraceLabel(l3, text="h", brace_direction=LEFT, color=WHITE, buff=0.1)
        bl2 = BraceLabel(l4, text="h", brace_direction=RIGHT, color=WHITE, buff=0.1)
        # tr4 = Intersection(tr1, tr2, fill_color=ORANGE, fill_opacity=0.5) # 交集

        self.play(Write(t0), run_time=3)
        self.add(l1, l2, d1, d2, d3, d4, ta, tb, tc, td)
        self.play(FadeIn(tr1), run_time=2, rate_func=linear)
        self.play(FadeIn(bl0), run_time=2, rate_func=linear)
        self.play(Create(l3), run_time=2)
        self.play(FadeIn(bl1), run_time=2)
        an11 = Transform(tr1.copy(), tr2)
        # an12 = l3.copy().shift(pc, pd)
        an21 = Transform(tr2.copy(), tr1)
        # an22 = l3.copy().shift(pd, pc)
        self.play(an11, run_time=5) # 也可以用TransformFromCopy
        self.play(Create(l4), run_time=2)
        self.play(FadeIn(bl2), run_time=2)
        self.play(an21, run_time=5) # 也可以用TransformFromCopy
        self.wait()

        e1 = MathTex(r"S_{\triangle ABC} = \frac{1}{2}\times a\times h", font_size=fs, color=ORANGE)
        e2 = MathTex(r"S_{\triangle ABD} = \frac{1}{2}\times a\times h", font_size=fs, color=ORANGE)
        e3 = MathTex(r"\therefore S_{\triangle ABC}=S_{\triangle ABD}", font_size=fs, color=ORANGE)
        self.play(Write(e1.next_to(l1, RIGHT)), run_time=3)
        self.play(Write(e2.next_to(e1, DOWN)), run_time=3)
        self.play(Write(e3.next_to(e2, DOWN)), run_time=3)
        self.wait(3)

if __name__ == "__main__":
    from os import system
    system("manim -pqk {}".format(__file__))