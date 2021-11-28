import numpy as np
np.random.seed(17)
nproblem = 8 # magic
nstudent = 150 # magic

problems = [
r"""\begin{problem} (From Problem Set 1)
What is the relationship between the energy $E$ and wavelength
$\lambda$ of a photon? Give a formula that involves energy $E$,
Planck's Constant $h$, the speed of light $c$, and wavelength
$\lambda$ (or whatever you need; but if you need anything else,
be very clear with me what it is).
\end{problem}""",
r"""\begin{problem} (From Problem Set 1)
How many cubic millimeters are there in a liter?
\end{problem}
""",
r"""\begin{problem} (From Problem Set 1)
What are the SI units for pressure, in base units?
That is, what
combination of kg (kilograms), m (meters), and s (seconds)
has units of pressure?
\end{problem}
""",
r"""\begin{problem} (From the reading)
Classical mechanics, or Newtonian mechanics, is only valid in certain
circumstances. When do the laws of classical mechanics, like $\vec{F} =
m\,\vec{a}$ for example, become wrong or break down? There are many answers
to this problem; I will take anything correct.
\end{problem}
""",
r"""\begin{problem} (From the reading)
What musical instrument did Einstein most enjoy playing?
\end{problem}
""",
r"""\begin{problem} (From the Math Review Lab)
What is this number? Give your answer in scientific notation.
$$
\frac{(6\times10^{-34})\times(3\times10^8)}{9\times10^{-7}}
$$
You don't need a calculator to solve this problem.
\end{problem}
""",
r"""\begin{problem} (From Lecture)
Which of the following physical quantities are vectors?
\\
\textsl{(a)}~energy,
\textsl{(b)}~mass,
\textsl{(c)}~force,
\textsl{(d)}~momentum,
\textsl{(e)}~acceleration.
\end{problem}
""",
r"""\begin{problem} (From Lecture)
Complete this statement of Newton's third law. Make it as specific as
you can.\\[2ex]
\textbf{For every force on object A from object B, there will be...}
\end{problem}
"""]
assert len(problems) == nproblem

print(r"""
\documentclass[12pt, letterpaper]{article}
\include{eu}
\pagestyle{empty}

\begin{document}

""")

for student in range(nstudent):
    print(r"""
\examheader{Term Exam 1}

""")
    pindx = np.argsort(np.random.uniform(size=nproblem))
    for problem, indx in enumerate(pindx):
        print(problems[indx])
        print(r"""
\vfill ~
""")
        if problem == 3:
            print(r"""
\clearpage

""")
    print(r"""
\cleardoublepage

""")

print(r"""
\end{document}
""")
