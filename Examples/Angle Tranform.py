from manim import *

config.background_color = BLACK # 设置背景颜色

class DotSample(Scene):
    def construct(self):
        rotation_center = LEFT
        theta_tracker = ValueTracker(90)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(theta_tracker.get_value() * DEGREES, about_point=rotation_center)
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        theta_tex = Tex(
            r"$\theta = $",
            str(int(theta_tracker.get_value())),
            r"$^\circ$",
            font_size=50,
            color=RED,
        ).shift(UP * 2)

        self.add(line1, line_moving, a, tex, theta_tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )
        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )
        theta_tex.add_updater(
            lambda x: x.become(
                Tex(
                    r"$\theta = $",
                    str(int(theta_tracker.get_value())),
                    r"$^\circ$",
                    font_size=50,
                    color=RED,
                ).shift(UP * 2)
            )
        )

        self.play(theta_tracker.animate.set_value(90))
        self.play(theta_tracker.animate.increment_value(480), run_time=60)
