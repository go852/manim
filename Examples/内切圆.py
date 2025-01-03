from manim import *

class CircleSample(Scene):
    def construct(self):
        t1 = Triangle()
        self.add(t1)
        self.play((t2:=t1.copy()).animate.move_to(UP*3))
        self.play((t3:=t1.copy()).animate.shift(DOWN*3))
        g1 = Group(t1, t2, t3)
        self.play((g2:=g1.copy()).animate.shift(LEFT*3))
        self.play((g3:=g1.copy()).animate.shift(RIGHT*3))
        self.wait(0.5)
        G = Group(g1, g2, g3)
        self.play(Rotate(G, 90*DEGREES))
        self.wait()
        self.play(Rotate(G, 90*DEGREES))
        self.wait()
        self.play(Rotate(G, 90*DEGREES))
        self.wait()
        self.play(Rotate(G, 90*DEGREES))
        self.wait()