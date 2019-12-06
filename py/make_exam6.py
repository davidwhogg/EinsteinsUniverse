import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 120 # magic

problems = [r"""\begin{problem}
(From Problem Set 6)
foo
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
sup
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
bar
\end{problem}""", r"""\begin{problem}
(From the reading)
yo
\end{problem}""", r"""\begin{problem}
(From the reading)
suh
\end{problem}""", r"""\begin{problem}
(From Lecture)
GW
\end{problem}""", r"""\begin{problem}
(From Lecture)
THE
\end{problem}""", r"""\begin{problem}
(From the Lab)
foo
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
\noindent
Name: \rule[-1ex]{0.60\textwidth}{0.1pt}
NetID: \rule[-1ex]{0.20\textwidth}{0.1pt}

\section*{\textsl{Einstein's Universe} Term Exam 5}
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
