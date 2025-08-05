
**Topic:** Evaluating maxima or minima of a single variable function using Taylors series.

> Take a look at the list of functions and/or commands given below using MATLAB `help`  
>  
> `syms`, `diff()`, `double()`, `solve()`, `linspace()`, `matlabFunction()`, `length()`, `subs()`, `sprintf()`, `num2str()`, `plot()`, `xlabel()`, `ylabel()`, `title()`, `legend()`, `hold on`, `hold off`, `grid on`, etc.  
>  
> Implement the task given below.

**Introduction**:

To evaluate the maxima or minima of a single-variable function using Taylor series in MATLAB, we can demonstrate the concept by focusing on the first and second derivatives to identify critical points and determine their nature (maxima, minima, or saddle points). The Taylor series expansion around a point provides insight into the function's behavior, and we can use MATLAB to visualize all these things. Carefully examine the figures below to understand various critical points pertaining to any given function of single variable. 

<div style="display: flex; justify-content: space-between;">
  <img src="./problem_statement/images/exp3a.png" alt="Input" style="width: 48%;">
  <img src="./problem_statement/images/exp3b.png" alt="Output" style="width: 48%;">
</div>


Note that the saddle points are the points on the flat curve/surfaces of the functions. Understanding critical points become little more complex for functions of multiple variables. 

In this experiment, you have to create a nonlinear function of single variable, detect the critical points and then determine their types. 

**Conceptual Overview**

Critical Points: A function f(x) has a potential maximum or minimum where its first derivative f'(x)= 0. These are called critical points.

Taylor Series: Near a critical point x=a, the Taylor series approximates the function as:

fx≈fa+f'ax-a+f''a2x-a2+higher-order terms

At a critical point, f'(a)= 0, so the series simplifies to:

fx≈fa+f''a2x-a2+higher-order terms

- If f''(a)> 0, the quadratic term is positive, indicating a local minimum (the function curves upward).
- If f''(a)< 0, the quadratic term is negative, indicating a local maximum (the function curves downward).
- If f''(a)=0, higher-order terms are needed to determine the nature of the point.

**Deliverables**:

Write a MATLAB program that will define a function, compute derivatives, find critical points, evaluate the second derivative, and visualize the function and its Taylor approximation to show how the quadratic term governs the behavior.

**Procedure**:

- Step 1: Define the function fx=x4-4x2using the symbolic variable x. 
- Step 2: Compute the first derivative
- Step 3: Find critical points by solving f'(x) = 0
- Step 4: Compute the second derivative
- Step 5: Evaluate the second derivative at critical points and determine maxima/minima
- Step 6: Taylor series approximation around each critical point. We'll use a second-order Taylor series: fx≈fa+f''a2x-a2+higher-order terms
- Step 7: Plot everything in one figure i.e, the original function as a continuous curve, indicate the critical points with dots, and then the Taylor series expansion in and around the critical points.

**code walkthrought:**[link](./experiments/experiment_viewer.html?exp=exp3)

**Conclusion**:

This script and approach make the concept of maxima and minima accessible while leveraging MATLAB’s computational and visualization power.

- **Simplicity**: The function x4-4x2 is polynomial, making derivatives and Taylor series straightforward to compute and visualize.
- **Visualization**: The plot clearly shows the function and its quadratic approximations, helping students see the connection between  f''(x)  and the shape of the curve.
- **Interactivity**: The script can work for any function in fact to experiment with other examples, fostering hands-on learning.


**References**:
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Exercise**: Will be made available shortly
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Use cases**: Will be made available shortly
