from manim_imports_ext import *
from _2019.diffyq.part2.wordy_scenes import *


class IveHeardOfThis(TeacherStudentsScene):
    def construct(self):
        point = VectorizedPoint()
        point.move_to(3 * RIGHT + 2 * UP)
        self.student_says(
            "I've heard\\\\", "of this!",
            index=1,
            target_mode="hooray",
            bubble_config={
                "height": 3,
                "width": 3,
                "direction": RIGHT,
            },
            run_time=1,
        )
        self.play_student_changes(
            "thinking", "hooray", "thinking",
            look_at=point,
            added_anims=[self.teacher.change, "happy"]
        )
        self.wait(3)
        self.student_says(
            "But who\\\\", "cares?",
            index=1,
            target_mode="maybe",
            bubble_config={
                "direction": RIGHT,
                "width": 3,
                "height": 3,
            },
            run_time=1,
        )
        self.play_student_changes(
            "pondering", "maybe", "pondering",
            look_at=point,
            added_anims=[self.teacher.change, "guilty"]
        )
        self.wait(5)


class InFouriersShoes(PiCreatureScene, WriteHeatEquationTemplate):
    def construct(self):
        randy = self.pi_creature
        fourier = ImageMobject("Joseph Fourier")
        fourier.set_height(4)
        fourier.next_to(randy, RIGHT, LARGE_BUFF)
        fourier.align_to(randy, DOWN)

        equation = self.get_d1_equation()
        equation.next_to(fourier, UP, MED_LARGE_BUFF)

        decades = list(range(1740, 2040, 20))
        time_line = NumberLine(
            x_min=decades[0],
            x_max=decades[-1],
            tick_frequency=1,
            tick_size=0.05,
            longer_tick_multiple=4,
            unit_size=0.2,
            big_tick_numbers=decades,
            numbers_to_show=decades,
            decimal_number_config={
                "group_with_commas": False,
            },
            stroke_width=2,
        )
        time_line.add_numbers()
        time_line.move_to(ORIGIN, RIGHT)
        time_line.to_edge(UP)
        triangle = ArrowTip(start_angle=-90 * DEGREES)
        triangle.set_height(0.25)
        triangle.move_to(time_line.n2p(2019), DOWN)
        triangle.set_color(WHITE)

        self.play(FadeIn(fourier, 2 * LEFT))
        self.play(randy.change, "pondering")
        self.wait()
        self.play(
            DrawBorderThenFill(triangle, run_time=1),
            FadeInFromDown(equation),
            FadeIn(time_line),
        )
        self.play(
            Animation(triangle),
            ApplyMethod(
                time_line.shift,
                time_line.n2p(2019) - time_line.n2p(1822),
                run_time=5
            ),
        )
        self.wait()


class SineCurveIsUnrealistic(TeacherStudentsScene):
    def construct(self):
        self.student_says(
            "But that would\\\\never happen!",
            index=1,
            bubble_config={
                "direction": RIGHT,
                "height": 3,
                "width": 4,
            },
            target_mode="angry"
        )
        self.play_student_changes(
            "guilty", "angry", "hesitant",
            added_anims=[
                self.teacher.change, "tease"
            ]
        )
        self.wait(3)
        self.play(
            RemovePiCreatureBubble(self.students[1]),
            self.teacher.change, "raise_right_hand"
        )
        self.play_all_student_changes(
            "pondering",
            look_at=3 * UP,
        )
        self.wait(5)


class IfOnly(TeacherStudentsScene):
    def construct(self):
        self.teacher_says(
            "If only!",
            target_mode="angry"
        )
        self.play_all_student_changes(
            "confused",
            look_at=self.screen
        )
        self.wait(3)


class SoWeGotNowhere(TeacherStudentsScene):
    def construct(self):
        self.student_says(
            "So we've gotten\\\\nowhere!",
            target_mode="angry",
            added_anims=[
                self.teacher.change, "guilty"
            ]
        )
        self.play_all_student_changes("angry")
        self.wait()
        text = OldTex(
            "&\\text{Actually,}\\\\",
            "&\\sin\\left({x}\\right)"
            "e^{-\\alpha {t}}\\\\",
            "&\\text{isn't far off.}",
            tex_to_color_map={
                "{x}": GREEN,
                "{t}": YELLOW,
            }
        )
        text.scale(0.8)
        self.teacher_says(
            text,
            content_introduction_class=FadeIn,
            bubble_config={
                "width": 4,
                "height": 3.5,
            }
        )
        self.play_all_student_changes(
            "pondering",
            look_at=self.screen
        )
        self.wait(3)
