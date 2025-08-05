**Topic:** Verifying Rolle’s and Lagrange’s Mean Value Theorems

> Take a look at the list of functions and/or commands given below using MATLAB `help`  
>  
> `syms`, `diff()`, `double()`, `solve()`, `linspace()`, `matlabFunction()`, `length()`, `subs()`, `sprintf()`, `num2str()`, `imag()`, `plot()`, `xlabel()`, `ylabel()`, `title()`, `legend()`, `hold on`, `hold off`, `grid on`, etc.  
>  
> Implement the task given below.


**Objective**

To verify Rolle’s and Lagrange’s Mean Value Theorems for a given function using MATLAB and illustrate their application in analyzing vehicle motion in traffic engineering.

**Theory**

Rolle’s Theorem states that for a function f(x) that is continuous on [a, b], differentiable on a, b, and satisfies f(a) = f(b), there exists at least one point c ∈(a, b) such that f'(c) = 0. This implies a point where the tangent is horizontal.

Lagrange’s Mean Value Theorem generalizes this, stating that for a function f(x) continuous on [a, b] and differentiable on (a, b), there exists at least one point c∈			(a, b) such that: f'(c)=(f(b)– f(a))/b-a. This represents the point where the instantaneous rate of change equals the average rate of change over the interval.

In traffic engineering, these theorems help analyze vehicle motion. For instance, if a car returns to its starting position (Rolle’s), there’s a moment its velocity is zero. For Lagrange’s, the theorem identifies when instantaneous velocity matches average velocity over a trip, aiding in speed monitoring systems.

**Key Equations:**

- Rolle’s: f'(c) = 0
- Lagrange’s: f'(c)=(f(b)– f(a))/ b-a

**Procedure**

1. Initialize the MATLAB environment by clearing the workspace and command window using clear all and clc.
1. Rolle’s Theorem:
   1. Define the symbolic function f(x) = x^2 - 2x + 1 and the interval [a, b] = [0, 2].
   1. Evaluate f(0) and f(2) using subs to verify f(a) = f(b), with a tolerance of 10^{-6}.
   1. Compute the derivative f'(x) = 2x - 2 using diff.
   1. Solve f'(x) = 0 using solve to find the critical point c within (0, 2).
   1. Plot the function over [0, 2] using matlabFunction and plot, marked the critical point, and added a horizontal tangent line at c.
   1. Add labels, title, and legend to the plot (Figure 1).
1. Mean Value Theorem:
   1. Define the symbolic function f(x) = x^3- 3x + 1 and the interval [a, b] = [0, 2].
   1. Calculate the secant slope (f(2)– f(0))/2 - 0 using subs.
   1. Compute the derivative f'(x) = 3x^2- 3 using diff.
   1. Solve f'(x)=secant slope using solve to find point(s) c within (0, 2).
   1. Plot the function, secant line, and tangent lines at each c over [0, 2], marking critical points.
   1. Add labels, title, and legend to the plot (Figure 2).
1. Displayed results and explanations in the command window, including critical points and theorem interpretations.
1. Saved plots for inclusion in the report.

**Discussion**

The experiment successfully verified Rolle’s and Mean Value Theorems using MATLAB. For Rolle’s Theorem, the function f(x) = x^2- 2x + 1 satisfied f(0) = f(2) = 1, and the critical point c = 1 was found where f'(1) = 0. The plot (Figure 1) visually confirmed a horizontal tangent at the vertex of the parabola, aligning with the theorem’s prediction of a “turning point.” The use of a tolerance 10-6  ensured robust numerical comparison of f(0) and f(2).

For the Mean Value Theorem, the function f(x) = x^3- 3x + 1 yielded a secant slope of 1 over [0, 2]. Two point, c≈1.1547 was found where f'(c) = 1. Figure 2 showed the tangent lines at these points parallel to the secant line, confirming the theorem’s assertion that the instantaneous rate of change equals the average rate at some point(s).

No numerical errors were observed, as MATLAB’s symbolic solver (solve) provided exact solutions, and floating-point precision was adequate. The code’s robustness was enhanced by filtering real solutions within the open interval (a, b). A potential improvement could involve testing functions with more complex behavior (e.g., trigonometric) to explore cases with multiple critical points.

In traffic engineering, Rolle’s Theorem applies to a vehicle returning to its starting position, implying a moment of zero velocity (e.g., a car stopping at a traffic light). The Mean Value Theorem models when a vehicle’s instantaneous speed matches its average speed, critical for speed monitoring systems or accident reconstruction. This experiment deepened understanding of these theorems’ geometric and practical significance.

**Conclusion**

The MATLAB experiment confirmed Rolle’s Theorem for f(x) = x^2- 2x + 1 at c = 1 and the Mean Value Theorem for f(x) = x^3- 3x + 1 at c≈1.1547with zero computational error. Visualizations clarified the theorems’ geometric interpretations, showing horizontal tangents and parallel secant-tangent lines. The exercise reinforced calculus concepts and their application in traffic engineering, highlighting MATLAB’s utility in numerical and graphical analysis. 

**References**:
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Exercise**: Will be made available shortly
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Use cases**: Will be made available shortly
