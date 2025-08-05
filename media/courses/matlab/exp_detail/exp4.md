
**Topic:** Taylor Series Approximation of Functions

> Take a look at the list of functions and/or commands given below using MATLAB ‘help’  
>  
> `syms`, `diff()`, `double()`, `solve()`, `linspace()`, `matlabFunction()`, `length()`, `subs()`, `sprintf()`, `num2str()`, `imag()`, `plot()`, `xlabel()`, `ylabel()`, `title()`, `legend()`, `hold on`, `hold off`, `grid on`, etc.  
>  
> Implement the task given below.

**Objective**

1. To understand the concept of Taylor series and how it approximates functions using polynomials.
1. To learn how to derive Taylor polynomials for single-variable functions.
1. To visualize the accuracy of the Taylor approximation for different numbers of terms.
1. To implement Taylor series approximation using MATLAB.
1. To analyze the error between the actual function and its Taylor approximation.
1. Approximating transcendental functions like sin(x),cos(x),e^x,log(1+x), etc., and in solving differential equations and analyzing the stability of systems in control engineering. 

**Theory**

**Taylor Series Definition**

If a function f(x) is infinitely differentiable at a point a, then the Taylor series of f(x) about x=a is:

![](/media/courses/matlab/exp_outputs/exp4a.png)

Where:

: n<sup>th</sup> derivative evaluated at x=a
: Remainder or truncation error after n terms

**Maclaurin Series**

A special case of the Taylor series when a = 0

![](/media/courses/matlab/exp_outputs/exp4b.png)

Key Equations and assumptions:

- ![](/media/courses/matlab/exp_outputs/exp4c.png) (For Taylor’s series)
- ![](/media/courses/matlab/exp_outputs/exp4d.png) (For Maclurin’s series)
- The function f(x) must be infinitely differentiable in some neighbourhood of x=a. 
- The series converges to f(x) for x within the radius of convergence.

**Procedure**

1. Define symbolic variables and function
1. Initialize Taylor series as a cell array
1. Compute Taylor series for each order using diff(f, k)and subs(df, x, a)
1. Convert symbolic function to numerical for plotting using matlabFunction(f)
1. Plot original function and Taylor approximations using plot()        
1. Compute and plot truncation error using semilogy()      

**code walkthrought :**[link](./experiments/experiment_viewer.html?exp=exp7)

**Discussion**

The Taylor Series for  e^x,sin(x), converge for all $ x $, while ln(1 + x) has a limited radius of convergence ( x≤1 ).

Near the expansion point ( x≈a ), fewer terms are needed for a good approximation.

Functions with rapidly growing derivatives (e.g.,  e^x) may require more terms for larger  |x - a| . 

**Limitations**

Convergence: The series may not converge for all $ x $, or may converge but not to f(x) (e.g., at boundary points).

Computational Cost: Higher-order terms require computing higher derivatives, which can be tedious.

Non-Smooth Functions: Taylor Series cannot be used for functions that are not sufficiently differentiable.

**Applications**

- Numerical Approximation: Taylor Series are used in calculators and computers to compute functions like  e^x,sin(x), etc.
- Physics and Engineering: Approximating complex systems (e.g., small oscillations approximated by linear terms).
- Differential Equations: Solving equations via series solutions.
- Error Analysis: Estimating truncation errors in computations.

**Conclusion**

The Taylor Series is a versatile method for approximating functions using polynomials. By computing the series for functions like e^x,sin(x), and ln(1 + x), we verified its accuracy and explored its convergence properties. Understanding the remainder term helps quantify errors, making the Taylor Series a practical tool in mathematical and applied contexts.

**References**
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Exercise**: Will be made available shortly
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Use cases**: Will be made available shortly
