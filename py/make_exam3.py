import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 115 # magic

problems = [r"""\begin{problem}
(From Problem Set 3, problem 1)
In the Galaxy rest frame, Alpha Centauri is 4.4 light-years away from us.
My friend travels at $0.5\,c$ (relative to this frame) from us to Alpha Centari.
How long does that take, according to us?
That is, give the time in in the Galaxy rest frame, and give it in years.
\end{problem}""", r"""\begin{problem}
(From Problem Set 3, problem 2)
What is the speed of the International Space Station, in terms of the speed of light?
That is, what is v/c for the International Space Station? Approximately!
\end{problem}""", r"""\begin{problem}
(From Problem Set 3, problem 3)
Reproduce here the triangular path of light you drew for this problem, and label the lengths
of the sides of the triangle.
\end{problem}""", r"""\begin{problem}
(From the reading)
Muons live for a couple of milliseconds. Naively, they can't travel more than few hundred meters,
even traveling near the speed of light. And yet, they often are observed to travel many kilometers.
How is this possible?
\end{problem}""", r"""\begin{problem}
(From the reading)
Why did Einstein want to have astronomers precisely observe a Solar eclipse?
What was he hoping they would see?
\end{problem}""", r"""\begin{problem}
(From Lecture, 2019-10-10)
Alice and Bob pass each other at high speed.
When they pass, Bob observes Alice's clock to run slow.
If Bob also had a clock, would Alice observe Bob's clock to run fast or slow?
\end{problem}""", r"""\begin{problem}
(From Lecture, 2019-10-17)
What is the formula for the Lorentz factor $\gamma$, in terms of $v$ and $c$?
\end{problem}""", r"""\begin{problem}
(From the Photoelectric Effect Lab)
Which photons have more energy? Ultraviolet or Green?
\end{problem}"""]
assert len(problems) == nproblem

print(r"""
\documentclass[12pt, letterpaper]{article}
\include{eu}
\pagestyle{empty}

\begin{document}

""")

for student in range(nstudent):
    print(r"""
\examheader{Term Exam 3}

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
