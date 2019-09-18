import numpy as np
np.random.seed(17)
nproblem = 8 # magic
nstudent = 140 # magic

problems = [r"""\begin{problem} (From Problem Set 1)
What is the relationship between the energy $E$ and wavelength
$\lambda$ of a photon? Give a formula that involves energy $E$,
Planck's Constant $h$, the speed of light $c$, and wavelength
$\lambda$ (or whatever you need).
\end{problem}""", r"""\begin{problem} (From Problem Set 1)
What is the approximate thickness of a stack of 1000 20-dollar bills?
No need to be precise, and use any units you like.
\end{problem}
""", r"""\begin{problem} (From the reading)
Classical mechanics, or Newtonian mechanics, is only valid in certain
circumstances. When do the laws of classical mechanics, like $F =
m\,a$ become wrong or break down? There are many answers to this
problem; I will take anything correct.
\end{problem}
""", r"""\begin{problem} (From the reading)
What musical instrument did Einstein most enjoy playing?
\end{problem}
""", r"""\begin{problem} (From the Math Review Lab)
What is this number? Give your answer in scientific notation.
$$
\frac{(7\times10^{-34})\times(3\times10^8)}{5\times10^{-7}}
$$
You don't need a calculator to solve this problem (\textit{hint: $3/5=0.6$}).
\end{problem}
""", r"""\begin{problem} (From the Kinematics Lab)

\end{problem}
""", r"""\begin{problem} (From Lecture on 2019-09-??)
\end{problem}
""", r"""\begin{problem} (From Lecture on 2019-09-17)
If you are traveling at 60 miles per hour, how long does
it take you to go 300 miles?
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
\noindent
Name: \rule[-1ex]{0.60\textwidth}{0.1pt}
NetID: \rule[-1ex]{0.20\textwidth}{0.1pt}

\section*{\textsl{Einstein's Universe} Term Exam 1}
\setcounter{problem}{1}

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
