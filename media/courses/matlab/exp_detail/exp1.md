
**Topic:** First and Second order derivatives of functions of a single variable.

> **Take a look at the list of functions and/or commands given below using MATLAB ‘help’**
> `syms`, `diff()`, `subs()`, `input()`, `double()`, `num2str()`, `plot()`, `xlabel()`, `ylabel()`, `title()`, `legend()`, `hold on`, `hold off`, `grid on`, etc.
> **Implement all Tasks given below.**

**Introduction**:

The computation of derivatives of functions is fundamental to calculus and has widespread importance across numerous fields of science, engineering, economics, and even daily life. Let fx be a real-valued function of a real variablex, then its first and second order derivatives are denoted by f'(x)  and f''(x) respectively. But these derivatives may not exist for some of the functions. Every f(x) must satisfy certain conditions for their derivatives to exist.

This experiment basically aimed at performing a computational exploration and demonstration of how to find and understand derivatives of single-variable functions using MATLAB. 

[Mandatory] First, we primarily focus on programmatically performing two key aspects of differentiation:

1. Symbolic Differentiation
1. Numerical Differentiation: 

[Optional] Then, we programmatically investigate whether or not a given function satisfies the following necessary and sufficient conditions for the existence of their derivatives:

1. Continuity
1. Smoothness

[Optional] Finally, we look into a few of its use cases or applications in some real world scenarios such as:

1. Rate of change: In physics, engineering, economics, and biology
1. Optimization (maxima or minima): In business, engineering, and logistics
1. Approximation of functions using linear approximation or Taylor series
1. Modeling and prediction: In Weather forecasting, Financial market analysis, Spread of epidemics, and Design of control systems

**Deliverables**:

**Symbolic Differentiation**

Symbolic Differentiation enables us to analytically compute exact derivative expressions using MATLAB's Symbolic Math Toolbox. This provides the foundational understanding of what a derivative is as a mathematical expression.

- **Learn to**
  - Define symbolic variables: Use syms to declare your variable(s) as symbolic. 
    - Reference [1]: Check this [link](https://math.umd.edu/~jmr/241/calc.html) to learn 
  - Define the function: Write your function using the symbolic variable.
  - Use diff:
    - diff(f): Calculates the first derivative of f with respect to the default independent variable (usually x if defined first, or t if defined first, etc.).
    - diff(f, var): Calculates the first derivative of f with respect to the specified variable var.
    - diff(f, n): Calculates the *n*-th derivative of f with respect to the default independent variable.
    - diff(f, var, n): Calculates the *n*-th derivative of f with respect to the specified variable var.
    - subs(expression, old, new): substitutes new for old in the expression.

- **Perform**: Write a MATLAB program to perform symbolic differentiations of the following

  **Task#1.1:** $f(x) = x^3 - 2x^2 + 5x - 1$

  - Step 1: Define xas a symbolic variable
  - Step 2: Define the function fx= x3-2x2+5x-1 in terms of that symbolic variable x.
  - Step 3: Compute the first order derivative of fx using diff(f) and display it as a symbolic expression.
  - Step 4: Compute the second order derivative of fx using diff(f,2)and display it as a symbolic expression.
  - Step 5: Evaluate the function f(x), first order derivative f'(x), and the second order derivative f''(x) at specific points, say x=2, and then display those numerical values. 


**Task#1.2:** gt=sin⁡t2

- Step 1: Define g(t)as a symbolic function
- Step 2: Read the function gt=sin⁡t2by asking the user to enter it.
- Step 3: Compute the first order derivative of gt using diff(g) and display it as a symbolic expression.
- Step 4: Compute the second order derivative of gt using diff(g,2)and display it as a symbolic expression.
- Step 5: Evaluate the function g(t), first order derivative g'(t), and the second order derivative g''(t) at specific points, say t=π4, and then display those numerical values.


**Numerical Differentiation (Approximation)**

While diff is primarily for symbolic differentiation, we can also perform numerical differentiation on arrays of data using diff. However, this is an approximation based on finite differences and is generally used when you have discrete data points rather than a continuous function. This demonstrates the practical application when exact function forms are unknown, highlighting the trade-offs between accuracy and data characteristics (like noise).

Key concepts: 

- **Learn**:

  The derivative is approximated by the change in y divided by the change in x.

- Formula for first derivative:

dydx≈ΔyΔx

- Formula for second derivative:

  The second derivative can be approximated by applying the first derivative approximation to the results of the first derivative.

- **Perform:** Write a MATLAB program to compute numerical derivatives from data points. Let's say you have a set of (x, y) data points and want to estimate the derivatives.

  **Task#1.3:** Numerical Derivatives from Data Points: Let's say you have a set of (x, y) data points and want to estimate the derivatives.

  - Step 1: Create some sample data points(x, y), some sequence of values at regular intervals for x and the corresponding y values as two different arrays.

    Note: Take the data points such that we can verify this numerical approximation of the derivatives are same as that of the analytical derivatives that can be simulated using symbolic functions. Example:y=x2.

- Step 2: Compute the first derivative as per the formula given above by computing the Δx and Δy individually using diff() function and then finding their ratio.
- Step 3: Calculate the midpoint of each x interval.
- Step 4: Compute the second derivative as per the formula given above i.e., by applying approximate derivative formula on the result of first derivative
- Step 5:  Plot the (x, y) data points, their first derivative, and the second derivative.
- Step 6: For the same function taken in step 1, compute the analytical first and second order derivatives using the built-in diff() function.

**Conclusion**:

**Accuracy**: Numerical differentiation is an approximation. The accuracy depends on the step size (diff(x\_data)). Smaller step sizes generally lead to better approximations, but too small can introduce numerical noise.

**Data Length**: When you use diff(array), the resulting array will have one less element than the original. This is why the x\_midpoints are used for plotting to align the derivatives with the original data.

**Noise Sensitivity**: Numerical differentiation is highly sensitive to noise in the data. If your data is noisy, the derivatives will be very noisy. You might need to smooth your data first.

**Choosing the Right Method:**

- Symbolic Differentiation (diff with syms): 

  Use this when you have a mathematical expression for your function and you want the exact analytical derivative expression. This is the most common and recommended approach for finding derivatives of known functions.

- Numerical Differentiation (diff on arrays): 

  Use this when you only have a set of discrete data points and cannot define an explicit function. Be aware of the limitations regarding accuracy and noise.

**References**:
