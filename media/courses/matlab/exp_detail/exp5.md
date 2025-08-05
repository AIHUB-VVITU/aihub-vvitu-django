**Topic:** Partial Derivatives and Gradient Visualization

> Take a look at the list of functions and/or commands given below using MATLAB ‘help’  
>  
> `syms`, `diff()`, `double()`, `solve()`, `linspace()`, `matlabFunction()`, `length()`, `subs()`, `sprintf()`, `num2str()`, `imag()`, `plot()`, `xlabel()`, `ylabel()`, `title()`, `legend()`, `hold on`, `hold off`, `grid on`, etc.  
>  
> Implement the task given below.


**Objective**

- To understand how functions change with respect to each independent variable in a multivariable context.
- To compute partial derivatives with respect to x, y, z.
- To interpret the gradient vector in 3D space.
- To apply these concepts in engineering analysis and design. 

**Theory**

***Partial derivatives***:

Let f(x, y, z) be a scalar field. The **partial derivative** with respect to a variable is defined as the rate of change of the function in that direction, keeping other variables constant:

![](/media/courses/matlab/exp_outputs/exp5a.png)

![](/media/courses/matlab/exp_outputs/exp5b.png)

![](/media/courses/matlab/exp_outputs/exp5c.png)

These represent the slope or rate of change of the function along each axis.

**Gradient Vector**:

The **gradient** of a scalar function f(x, y, z) is a **vector field** given by:

![](/media/courses/matlab/exp_outputs/exp5d.png)

Where:

- ![](/media/courses/matlab/exp_outputs/exp5e.png)are unit vectors in the x, y, and z directions
- ∇f points in the direction of maximum rate of increase of ‘f’.

**Key Equations:**

1. Partial derivatives: ![](/media/courses/matlab/exp_outputs/exp5f.png)
1. Gradient Vector: ![](/media/courses/matlab/exp_outputs/exp5g.png)
1. Directional Derivative in the direction of a unit vector ![](/media/courses/matlab/exp_outputs/exp5h.png)
1. Magnitude of Gradient: ![](/media/courses/matlab/exp_outputs/exp5i.png)

**Procedure**

Step 1: Define symbolic variables and function

Step 2: Compute partial derivatives using diff(f, x)and diff(f, y)

Step 3: Compute gradient using gradient(f, [x, y])

Step 4: Convert symbolic functions to numerical for plotting using meshgrid()

Step 5: Create mesh for visualization using meshgrid() 

Step 6: Plot 3D surfcace of the function using surfc()

Step 7: Plot 2D contour with gradient vector field using contour() and quiver()        

Step 8: Plot 3D surfcace with gradient vectors using surfc()       

Step 9: Plot partial derivatives as surfaces using surfc()       

Step 10: Display symbolic results using disp()

**code walkthrought:**[ link](./experiments/experiment_viewer.html?exp=exp6)

**Discussion**

The experiment successfully demonstrated how to compute and visualize partial derivatives and the gradient vector of scalar functions of two variables using MATLAB. By defining symbolic expressions and converting them to numerical functions for plotting, the changes in the function with respect to each independent variable were effectively illustrated.

The surface plots showed the overall shape of the function, while the contour plots combined with gradient vectors clearly indicated the direction and magnitude of the steepest ascent at each point in the domain. In particular, the quiver plots helped to interpret the gradient as pointing perpendicularly to the level curves, aligning with theoretical expectations from vector calculus (Stewart, 2015).

The partial derivative surfaces provided insight into how the slope varies along each axis individually. For example, for the function f(x,y)=x2+y2, the partial derivatives ∂f∂x=2x and ∂f∂y=2y were linear in each variable, and the gradient magnitude increased proportionally with the distance from the origin, consistent with the radial symmetry of the function (Thomas et al., 2014).

By changing the function to other examples (e.g., f(x,y)=x2sin⁡(y)), students observed how the gradient vector field adapted to the function’s local curvature and oscillations. These visualizations reinforce understanding that the gradient vector is not constant but depends on both variables and reflects local properties of the scalar field.

**Engineering Applications**

Partial derivatives and gradients are widely used in various engineering domains:

1. **Mechanical engineering**: Stress-strain relationships, heat conduction in 3D solids
1. **Electrical Engineering**: Electric and magnetic field distribution
1. **Civil Engineering**: Surface slope analysis, fluid pressure gradients
1. **Chemical Engineering**: Reaction rate changes with temperature, pressure, concentration
1. **Data Science / AI**: Optimization of cost functions using gradients (e.g., in gradient descent)

**Conclusion**

The MATLAB experiment provided a practical and visual approach to understanding partial derivatives and gradients in multivariable calculus. The key outcomes were:

- Successfully computing symbolic partial derivatives and gradients of selected functions.
- Converting symbolic results into numerical grids for visualization.
- Plotting surfaces, contours, and gradient vector fields to interpret how the function changes in different directions.
- Demonstrating that the gradient points in the direction of maximum increase and that its magnitude corresponds to the steepest slope at each point.

These results confirm the theoretical definitions of partial derivatives and gradients and illustrate their relevance in engineering analysis, such as optimization of surfaces and understanding heat or fluid flow over domains. Overall, the experiment achieved its objectives of linking symbolic computation with graphical interpretation in MATLAB.

**References**

1. Stewart, J. (2015). Calculus: Early Transcendentals (8th ed.). Cengage Learning.
1. Thomas, G. B., Weir, M. D., & Hass, J. (2014). Thomas’ Calculus (3th ed.). Pearson.

<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Exercise**: Will be made available shortly
<hr style="border: none; border-top: 1.5px solid #000; margin: 0.5em 0;">

**Use cases**: Will be made available shortly