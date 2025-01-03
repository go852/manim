from manim import *

class PolygramExample(Scene):
    def construct(self):
        rp1 = RegularPolygram(7, density=3) # 正多边形，隔density个顶点连接
        self.add(rp1)
        d = Dot()
        self.play(MoveAlongPath(d, rp1, runtime=5), runtime=5)
        self.wait()