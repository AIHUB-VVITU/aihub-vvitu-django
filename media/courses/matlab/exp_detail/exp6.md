
**Topic:** Jacobian Matrix and Functional Dependence

> Take a look at the list of functions and/or commands given below using MATLAB ‘help’  
>  
> `syms`, `diff()`, `double()`, `solve()`, `linspace()`, `matlabFunction()`, `length()`, `subs()`, `sprintf()`, `num2str()`, `imag()`, `plot()`, `xlabel()`, `ylabel()`, `title()`, `legend()`, `hold on`, `hold off`, `grid on`, etc.  
>  
> Implement the task given below.

**Objective**

To grasp and analyse the fundamental principles and formation of the Jacobian matrix, the idea of functional dependence or independence. Illustrating its application of Robotics and also in Machine learning and Deep Learning for functions of several variables using MATLAB.

**Theory**

**Jacobian Matrix**

Consider a vector-valued function:
      
![](/media/courses/matlab/exp_outputs/exp6a.png)

The **Jacobian matrix** of F is a matrix consisting of the first-order partial derivatives of each function with respect to each variable:
![](/media/courses/matlab/exp_outputs/exp6b.png)

This matrix describes how a vector function changes with respect to its input variables and plays a critical role in linear approximations, transformations, and system modelling.

**Functional Dependence**

A set of functionsf1,f2,...,fm​ are said to be **functionally dependent** if there exists a non-trivial relation among them, such that:

Φ(f1,f2,...,fm)=0

where Φ is not identically zero.

To test this, we analyse the **Jacobian matrix** of the functions. If the **rank** of the Jacobian is less than the number of functions, it indicates that the functions are **functionally dependent**. If the rank equals the number of functions, the functions are **independent**.

**Key Equations:**

![](/media/courses/matlab/exp_outputs/exp7b.png)=0

**MATLAB Code**

**Part – I:**  

Compute Jacobian matrix and check functional dependence for a system of functions

**Procedure**

Step 1: Define symbolic variables syms x y;

Step 2: Define a vector-valued function F = [f1, f2], Example: f1 = x^2 + y, f2 = x\*y (potentially dependent functions)

Step 3: Compute the Jacobian matrix using jacobian()

Step 4: Check functional dependence by computing the determinant (for 2x2 Jacobian) using det()

Step 5: Simplify the determinant to check if it's identically zero using simplify()

Step 6: Analyze functional dependence

Step 7: Evaluate determinant at a point to confirm (e.g., x=1, y=1)

Step 8: Visualize the functions f1 and f2 using meshgrid(), subs(), etc.

**code walkthrought:**[ link](./experiments/experiment_viewer.html?exp=exp7)

**Part – II:**  

Compute Jacobian for a 2D robotic arm to relate joint angles to end-effector position

**Procedure**

Step 1: Define symbolic variables for joint angles syms theta1 theta2 L1 L2;

Step 2: Define arm lengths (constants for simplicity)

Step 3: End-effector position (x, y) for a 2-link planar arm

Step 4: Compute Jacobian with respect to [theta1, theta2]

Step 5: Evaluate Jacobian at a specific configuration (theta1 = pi/4, theta2 = pi/4)

Step 6: Analyze functional dependence

Step 7: Plot end-effector path for varying theta2

**code walkthrough:**[ link](./experiments/experiment_viewer.html?exp=exp7)

**Part – III:**  

Use Jacobian in Newton's method for minimizing a loss function

**Procedure**

Step 1: Define a simple loss function (e.g., for a neural network)

Step 2: Compute gradient (Jacobian of scalar function = transpose of gradient)

Step 3: Compute Hessian (Jacobian of gradient for second derivatives)

Step 4: Newton's method to find critical points → solve grad\_loss = 0 using solve()

Step 5: Evaluate Hessian at a critical point to check for minimum

Step 6: Check positive definiteness (simplified check for 2x2 matrix)

Step 7: Plot end-effector path for varying theta2

**code walkthrough:**[ link](./experiments/experiment_viewer.html?exp=exp7)

**Discussion**

The experiment successfully demonstrates the computation and application of the Jacobian matrix across three distinct contexts: functional dependence, robotics, and machine learning optimization. In Part I, the Jacobian of the functions f1 = x^2 + y and f2 = x*y is correctly computed, and the determinant analysis appropriately identifies the functions as functionally independent, as the determinant 2x2 - y is not identically zero. The visualization of the functions aids in understanding their behavior, though additional analysis of the determinant's zero set could further clarify dependence regions.

In Part II, the application to a 2D robotic arm effectively illustrates the Jacobian's role in relating joint angles to end-effector positions, a critical concept in robotics for velocity kinematics and control. The trajectory plot enhances the understanding of the arm's motion, but analyzing singularities (where the Jacobian is singular) would provide deeper insight into configurations where the arm loses degrees of freedom.

Part III successfully applies the Jacobian in the context of optimization, computing the gradient and Hessian of a loss function to find critical points. However, the positive definiteness check for the Hessian at  (w1, w2) = (0, 0)  is flawed due to an incorrect trace-based condition. Correctly, the Hessian is not positive definite, indicating a saddle point, but the code's logic needs adjustment to use proper criteria (e.g., checking leading principal minors or eigenvalues). Evaluating additional critical points would also strengthen the analysis.

Overall, the experiment effectively bridges theoretical concepts with practical applications, using MATLAB's Symbolic Math Toolbox to perform complex computations. The visualizations enhance comprehension, and the code is robust, though minor improvements in error handling and analysis depth would enhance its educational value. **However, following issues still can be addressed**

**Part I:**
The code assumes a 2x2 Jacobian for determinant-based dependence checking, which is valid for two functions and two variables. However, it could note that for more functions or variables, rank computation (e.g., using rank() in MATLAB) would be needed.

The visualization is clear, but adding a plot of the determinant's behavior over a range of  x  and  y  could enhance understanding of where dependence occurs (e.g., along 2x^2 - y = 0).

**Part II:**

The code does not check for singularities (where the Jacobian becomes singular, i.e., $ \det(J) = 0 $), which is critical in robotics to identify configurations where control is lost.

The comment about fixing a "symbolic variable error" for $ \theta\_2 $ is unclear, as the code works correctly without apparent issues.

**Part III:**

The positive definiteness check is flawed. A 2x2 matrix is positive definite if det (H) > 0  and the first leading principal minor (e.g., H(1,1) ) is positive. At (0, 0), H(1,1) = -4 < 0 , confirming the Hessian is not positive definite, but the code's reliance on the trace is misleading.

The code only evaluates the Hessian at the first critical point (0, 0). Analyzing other critical points would provide a more complete picture.

The loss function is complex, and simpler examples (as commented out, e.g., w_1^2  sin(w_2)) could be included for clarity.

**Conclusion**

The MATLAB experiment successfully achieves its objectives of computing the Jacobian matrix, analyzing functional dependence, and applying these concepts to robotics and machine learning. The code accurately computes Jacobians, determinants, gradients, and Hessians, with clear visualizations that aid in understanding. The results align with theoretical expectations, except for a minor error in the Hessian positive definiteness check in Part III, which can be corrected by using proper criteria for positive definiteness. The experiment effectively demonstrates the Jacobian's utility in diverse engineering applications, from robotic kinematics to optimization, making it a valuable learning tool. Future improvements could include singularity analysis in robotics and comprehensive critical point analysis in optimization to deepen the exploration of these concepts.

**References**
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Exercise**: Will be made available shortly
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Use cases**: Will be made available shortly
