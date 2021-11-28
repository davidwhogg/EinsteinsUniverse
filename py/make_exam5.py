import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 150 # magic

problems = [r"""\begin{problem}
(From Problem Set 5)
What is the numerical value of the exact Doppler factor (not the approximate) for $v=2\times 10^8\,\m\,\s^{-1}$?
\end{problem}""", r"""\begin{problem}
(From Problem Set 5)
What, roughly, is the age of the Universe? Give your answer in any units you like.
\end{problem}""", r"""\begin{problem}
(From Problem Set 5)
By how much do the times differ between the clocks on top of K2 and at sea level, after one year? That is, what did you get for this problem?
\end{problem}""", r"""\begin{problem}
(From the reading)
In what decade was the expansion of the Universe discovered?
\end{problem}""", r"""\begin{problem}
(From the reading)
What was the policy introduced at the University in Berlin in 1933 that caused Einstein's job to be terminated?
\end{problem}""", r"""\begin{problem}
(From Lecture)
Bob is at the top of an elevator accelerating upwards. Alice is at the bottom of that same elevator.
Whose clock runs faster?
\end{problem}""", r"""\begin{problem}
(From Lecture)
How do we know the Universe is expanding?
\end{problem}""", r"""\begin{problem}
(From the Lab)
If a galaxy is moving away at 5 percent of the speed of light, the K
line (which is at a rest-frame or natural wavelength of around $\lambda =
3900$\,\AA), will be shifted to the red. What, roughly, will be the change
$\Delta\lambda$ in the wavelength of the line?
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
\examheader{Term Exam 5}

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
