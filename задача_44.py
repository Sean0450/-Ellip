# -*- coding: utf-8 -*-
"""Задача 44.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rf6gvD4oxG2TUHABv0a1fpWea7-iO85A
"""



"""##**44.Эллипс**
##Задачи:
1.Вычислить значение полуоси эллипса с помощью метода `scipy.optimize.brentq`, если его периметр L=10, а вторая полуось равна 1, на основании формулы.
$$
L=4a\int \limits _{0}^{\pi /2}{\sqrt{\strut 1-\varepsilon^2\cos^2\varphi}}\,d\varphi = 4a E(\varepsilon)
$$
2.Вычислить $E(\varepsilon)$ c помощью метода `scipy.special.ellipe`.

3.Построить график эллипса.

4.Сравнить полученное значение L с тем, что можно получить с помощью формулы: $$
L\approx 4\cdot{\frac {\pi ab+(a-b)^{2}}{a+b}}.
$$ 

5.Сделать выводы о полученных значениях.

Исходное уравнение длины дуги эллипса выглядит следующим образом:
$$
L=4a\int \limits _{0}^{\pi /2}{\sqrt{\strut 1-\varepsilon^2\cos^2\varphi}}\,d\varphi = 4a E(\varepsilon)
$$
Так как пределы интегрирования находятся между π/2 и 0, то мы имеем полное право заменить $ \cos^2\varphi $ на $\sin^2φ $.
Полученный таким образом интеграл представляет собой ` полный эллиптический интеграл второго рода`. 
$$
E(\varepsilon) =\int\limits _{0}^{\pi /2}{\sqrt{\strut 1-\varepsilon^2\sin^2\varphi}}\,d\varphi
$$
Решение находится с помощью бесконечного числового ряда $\left(\sum\limits_{j=1}^{∞} a_j\right)$

Займемся его вычислнием. Известно, что биномиальный ряд $(1+ x)^a$ равен:
$$
1 + ax + {\frac{a(a - 1)}{2!}}x^2 + {\frac{a(a - 1)(a -2)}{3!}}x^3 +  ...
$$
Подставим вместо $(1 + x)^a$ иррациональное выражение $\sqrt{1 + x}$ (что наложит на наш ряд модуль), а также преобразуем коэффициенты к следующему виду:
$$
1 + \frac{1}{2}x + \frac{1\cdot3}{2\cdot4}\cdot\frac{x^2}{3} + \frac{1\cdot3\cdot5}{2\cdot4\cdot6}\cdot\frac{x^3}{5} + ...
$$
Теперь заменим $x -> -x^2$, тогда:
$$
\sqrt{1-x^2} = 1 - \frac{1}{2}x^2 - \frac{1\cdot3}{2\cdot4}\cdot\frac{x^4}{3} + \frac{1\cdot3\cdot5}{2\cdot4\cdot6}\cdot\frac{x^6}{5} + ... =
$$
$$
1 - \left(\sum\limits_{j=1}^{∞}\frac{(2j - 1)!!}{2j!!}\cdot\frac{x^{2j}}{(2j-1)}\right)
$$
Заменим $x -> k\sin\varphi$, тогда:
$$
\sqrt{1-k^2\sin^2\varphi} = 1 - \left(\sum\limits_{j=1}^{∞}\frac{(2j - 1)!!}{2j!!}\cdot\frac{k^{2j}\cdot\sin^{2n}\varphi}{(2j-1)}\right)
$$
С учетом всех преобразований, интеграл принимает вид:
$$
E(\varepsilon) = \int \limits _{0}^{\pi /2} 1 - \left(\sum\limits_{j=1}^{∞}\frac{(2j - 1)!!}{2j!!}\cdot\frac{k^{2j}\cdot\sin^{2n}\varphi}{(2j-1)}\right)dt
$$
С помощью методов `scipy.optimize.newton`, а также `scipy.special.ellipe` подсчитаем точное значение неизвестной полуоси.
"""

from scipy.optimize import newton
from scipy.special import ellipe
from matplotlib import pyplot as plt
import numpy as np

L = 10
a = 1

def eps(b): return (1 - (b/a)** 2)

def eqv(b):
    epsilon = eps(b)
    return 4 * a * ellipe(epsilon) - L

def aproxx(b):
    return 4 * (np.pi * a * b + (a - b)**2) / (a + b) - L

b = newton(eqv, 3)
another_b = newton(aproxx, 2)

print("True >>> ", b)
print("Aprox >>>", another_b)
###Также по полученному значению построим график эллипса
centerx, centery=0, 0
t = np.linspace(0, 2*np.pi, 100)
plt.plot( centerx+a*np.cos(t) , centery+b*np.sin(t) )
plt.grid(color='lightgray',linestyle='--')
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.show()



"""##Вывод:Вычисление величины неизвестной полоуси оказалось намного точнее, с помощью эллиптического интеграла, разница в значениях получилась уже во втором знаке после запятой. При этом, сложно не отметить, что вычисления с помощью приближенной формулы намного проще, однако точность страдает слишком сильно, чтобы полагаться на вторую формулу."""