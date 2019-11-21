import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 115 # magic

problems = [r"""\begin{problem}
(From Problem Set 5)
What value of the ratio $v/c$ corresponds to a Doppler factor of 10?
\end{problem}""", r"""\begin{problem}
(From Problem Set 5)
What is the insolation on Pluto in watts per square meter?
\end{problem}""", r"""\begin{problem}
(From Problem Set 5)
How long does it take light to travel a distance corresponding to the altitude of the mountain K2?
\end{problem}""", r"""\begin{problem}
(From the reading)
In Newtonian mechanics, planets travel on perfect ellipses. General
relativity changes this slightly, especially for Mercury. What happens
to Mercury's orbit?
\end{problem}""", r"""\begin{problem}
(From the reading)
Why was Einstein's position at the University in Berlin terminated in 1933?
\end{problem}""", r"""\begin{problem}
(From Lecture)
You are looking at a clock that is moving towards you very
quickly. This clock will appear to you to be running slowly? Or
running quickly?
\end{problem}""", r"""\begin{problem}
(From Lecture)
What is the age of the Universe?
\end{problem}""", r"""\begin{problem}
(From the Lab)
If a galaxy is moving away at 1 percent of the speed of light, the K
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
