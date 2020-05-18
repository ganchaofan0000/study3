### 1.Supervised Learning
1.model representation(give right answer to each example)

2.1 training set->learning algorithm->h(hypothesis)

2.2 $h(x)=\theta_0+\theta_1X$(univariate linear regression)

3.1 cost function($J(\theta_0,\theta_1)=\frac{1}{2m}\sum_{i=1}^{m}(h(x_i)-y_i)^2$)

3,2 minimize $J(\theta_0,\theta_1)$

4.1 gradient descent ($\theta_j:=\theta_j-\alpha\frac{\partial}{\partial x}J(\theta_0,\theta_1)\ (for\ j=0\ and\ j=1)$)

4.2 normal equation(pinv(x'*x)*x'*y(Octave))

5."Batch" gradient descent
### 2.Unsurpverised Learning
### 3.Matrix(矩阵的表示与运算)
### 4.choice of feature
### 5.Octave 的基本语法
