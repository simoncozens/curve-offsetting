

# Offsetting parameterised Bezier curves
### Simon Cozens

A common problem in type design is the creation of pairs of curves representing the stroke of a pen: an inner curve and an outer curve delimit the contours of a writing implement of fixed or flexible thickness. While it is impossible to precisely offset a Bezier curve at a given width, this paper presents a simple approximation by minimizing the error between desired distance and actual distance. This can also be applied to situations where the thickness varies linearly across the width of the
curve.

We use a simplification due to Tunni, who postulates that any curve **a**, **b**, **c**, **d** with straight handles (i.e. where the control points **b**and **c** are positioned orthogonally to **a** and **d** respectively) can be represented in terms of start and end points **a**and **d** and a curve tension *τ*. To determine curve tension, compute the point **T** where **ab**  intersects **cd**: 

<img src="images/offset-1.svg" width="84.78429 " height="86.08057 "/>

The curve tension is given by the mean of the ratios <img src="images/offset0x.png" alt="&#x2225;&#x2225;aabT&#x2225;&#x2225;" > and <img src="images/offset1x.png" alt="&#x2225;&#x2225;ddTc&#x2225;&#x2225;" >. Given the points **a**, **d** and a tension τ we can compute the Bezier control points **b**, **c** by setting them at the appropriate
ratios.

This conceptualization enables us to find similar parameters for an offset Bezier curve. We will approach the problem in small pieces, demonstrating the technique first before solving the general case.

## Outer offset of a unit Bezier curve

Consider first the unit Bezier curve **B**<sub>**A**</sub> with **a** = (0,1), **d** = (1,0) and **c** and **d** chosen as orthogonal control
points with a curve tension *α*. What are the parameters for a Bezier curve **B**<sub>**B**</sub> offsetting this curve on the
outside at a fixed distance *δ*?

<img src="images/offset-2.svg" width="78.47368 " height="78.47368 "/>

Clearly we have ***a** = (0, 1 + *δ*), **d** = (1 + *δ*, 0)*, so it remains to find the curve tension *β*.

As a function of time, the distance between the two curves is:

<table 
class="equation"><tr><td><a 
 id="x1-1001r1"></a>
   <center class="math-display" >
<img 
src="images/offset2x.png" alt="&#x2225;BA (t)&#x22C5;BB (t)&#x2225;
" class="math-display" ></center></td><td class="equation-label">[1]</td></tr></table>

and at any point on the curve, the expected distance is *δ*. Knowing it is impossible to achieve a perfect
offset, we can treat this as an optimization problem: find the value of *β* which minimizes the total error function

<table 
class="equation"><tr><td><a 
 id="x1-1002r2"></a>
   <center class="math-display" >
<img 
src="images/offset3x.png" alt="&#x222B; 1
   (&#x2225;BA (t)&#x22C5;BB (t)&#x2225; - &#x03B4;)2dt
 0
" class="math-display" ></center></td><td class="equation-label">[2]</td></tr></table>

This integral turns out to be tricky to compute due to the presence of the square root, so instead we create an equivalent error function using the square of the distance. We expect the square of the distance to be *δ*<sup>2</sup>, and
we square the difference of these two values to perform a least squares optimization. This leads to an error
function of

<table 
class="equation"><tr><td><a 
 id="x1-1003r3"></a>
   <center class="math-display" >
<img 
src="images/offset4x.png" alt="                 2 2
(|BA (t)&#x22C5;BB (t)|- &#x03B4; )
" class="math-display" ></center></td><td class="equation-label">[3]</td></tr></table>

For a unit Bezier, we have:

<table class="multline"><tr><td><img 
src="images/offset5x.png" alt="       (    3         2          2   )
BA (t) =    t2+ 3(1- t)t + 3&#x03B1;3(1 - t) t 2
         3&#x03B1;t((1 - t)+ (1- t) + 3t(1 - t)                                        )
               (&#x0394; + 1)t3 + 3(1- t)t2((1- *β*&#x0394; +1) +*β*&#x0394; + 1))+ 3*β*#x0394; + 1)(1 - t)2t
    BB(t) =  3*β*&#x0394; + 1)t2(1 - t)+ 3t(1- t)2((1- *β*&#x0394; + 1)+ *β*#x0394; +1))+ (&#x0394; + 1)(1 - t)3
                                                (  (&#x0394; + 1)t(3*β*- 1)2 +t(3- 2t))  )
                                              =  (&#x0394; + 1)(- (t- 1))((3*β* 2)t2 + t+ 1)
" ></td><td class="equation-label"><br />[4]<br /></td></tr></table>

leading to a square distance

<table class="multline"><tr><td><img
src="images/offset6x.png" alt="                2(       2                2           )2
|BA (t)&#x22C5;BB (t)| = t 3&#x03B1; (t - 1) - 3*β*#x0394; + 1)(t- 1) +&#x0394;t (2t - 3) +
                                          (t- 1)2(&#x0394; + t(&#x0394; + t(- 3&#x03B1; + 3*β*#x0394; + 1) - 2&#x0394; )))2
" ></td><td class="equation-label"><br />[5]<br /></td></tr></table>
<!--l. 103-->   and therefore an error function
<!--l. 105-->   <table 
class="multline"><tr><td><img 
src="images/offset7x.png" alt="            &#x222B; 1                         1  (
E(BA, BB ) =   (|BA (t)&#x22C5;BB (t)|- &#x03B4;2)2dt = 30030 1161(&#x03B1;- *β*4 - 36(129*β* 148)&#x03B4;(&#x03B1;- *β*3+
         (   02           ) 2      2                                 3
       18  387*β*+ 888*β* 146 &#x03B4; (&#x03B1;- *β*- 4(9*β**β*3*β* 148)+ 146)- 2138)&#x03B4;(&#x03B1; - *β*  )
                                          (*β**β*β*29*β* 592)+ 292)- 8552)+ 2916)&#x03B4;4
" ></td><td class="equation-label"><br />[6]<br /></td></tr></table>

This looks horrific, but it’s only a quartic, and is easily optimizable. Rather than solving the differential equation for the general case, let’s be practical, remember that *α* and *δ* will be given and go for a numerical method to minimize the error function.

Beginning with *β*<sub>1</sub> = *α* and applying the Newton-Raphson optimization method gives us an iterated
function

<table 
class="multline"><tr><td><img 
src="images/offset8x.png" alt="               &#x2032;
  *β*1 = *β*- E-(BA,-BB-)
      (      E&#x2032;&#x2032;(BA, BB )            (                )                                 )
                                - 36 387*β*+ 888*β* 146 &#x03B4;2(&#x03B1; - *β*      ||             - 4(9*β*129*β* 3(43*β* 148)) +9(3*β*3*β*148)+ 146))&#x03B4;3(&#x03B1; - *β*           ||
      ||          +18(774*β*888)&#x03B4;2(&#x03B1;- *β* - 4644&#x03B4;(&#x03B1;- *β* + 108(129*β* 148)&#x03B4;(&#x03B1;- *β*      ||
      (                      - 4644(&#x03B1;- *β* + (9*β*β*29*β* 592)+ 292)+                  )
      --*β**β*58*β*-592)+-9(*β*29*β*-592)+-292))-- 8552)&#x03B4;4 +-4(9*β**β*3*β*-148)+-146)--2138)&#x03B4;3
= *β*       (              - 4(2322*β* 18(129*β* 3(43*β*148)))&#x03B4;3(&#x03B1; - *β*          )
            |         13932&#x03B4;2(&#x03B1; - *β*2 - 72(774*β* 888)&#x03B4;2(&#x03B1;- *β*+ 27864&#x03B4;(&#x03B1; - *β*2      |
            ||                       - 216(129*β* 148)&#x03B4;(&#x03B1; - *β*                    ||
            ||               13932(&#x03B1; - *β*2 + 36(387*β*+ 888*β* 146)&#x03B4;2+            ||
            |( (*β*322*β* 18(258*β* 592))+ 2(9*β*258*β* 592)+ 9(*β*29*β* 592) + 292)))&#x03B4;4+ |)
                        8(9*β*29*β* 3(43*β* 148))+ 9(3*β*43*β* 148)+ 146))&#x03B4;3
" ></td><td class="equation-label"><br />[7]<br /></td></tr></table>

which quickly converges to the minimum error, giving us the optimal curve tension.

As an example, plugging in *α = 0.55, δ = 1*:

*β*<sub>1</sub> = 0.55

*β*<sub>2</sub> = 0.550987

*β*<sub>3</sub> = 0.550985

*β*<sub>4</sub> = 0.550985

## We can cheat

Thankfully, we find by inspection that the optimal value of *β* given *α* and *δ*, *β(α, δ)* turns out to be pretty much linear in both *α* and *δ* when *α >= 0.3*. A very pleasing result is:

 <table 
class="equation"><tr><td><a 
 id="x1-2001r8"></a>
                                                                                      
                                                                                      
   <center class="math-display" >
<img 
src="images/offset9x.png" alt="*β*#x03B1;,1) = 0.275985+ &#x03B1;
                  2
" class="math-display" ></center></td><td class="equation-label">[8]</td></tr></table>


Note that this gives exactly the answer given by our Newton-Raphson method above. A more general, but less accurate, approximation is:

<table class="equation"><tr><td><a
 id="x1-2002r9"></a>
   <center class="math-display" >
<img 
src="images/offset10x.png" alt="*β*#x03B1;,&#x03B4;) = 0.513216&#x03B1; - 0.025407&#x03B4;+ 0.296638
" class="math-display" ></center></td><td class="equation-label">[9]</td></tr></table>

## Inner offsetting of a unit Bezier

What if we want to go the other way, and find the inner curve at a fixed distance?

<img src="images/offset-3.svg" width="82.38431 " height="90.84732 "/>

A very similar pattern applies, but this time we construct ***B**<sub>**B**</sub>* as ***a** = (0, 1-δ), **d** = (1-δ, 0)* and the Newton step <img
src="images/offset11x.png" alt="E&#x2032;(BA,BB)-
E&#x2032;&#x2032;(BA,BB)" > is
<!--l. 180-->   <table 
class="multline"><tr><td><img 
src="images/offset12x.png" alt="( 18&#x03B1;2 (414*β*#x03B4;- 1)2 + 244(&#x03B4; - 1)2)+ 8&#x03B1; (1098*β*&#x03B4; - 1)2 - 108(&#x03B4;- 1)2)+ )
(  4644*β*&#x03B4; - 1)4 + 15984*β*&#x03B4;- 1)4 + 72*β*73&#x03B4;2 - 718&#x03B4; + 548) (&#x03B4; - 1)2 )
                - 8(1069&#x03B4;2 + 3439&#x03B4;- 4011)(&#x03B4;- 1)2
-(-----2------2-------------2--------2------4-------------4--)--
  7452&#x03B1; (&#x03B4;- 1) + 8784&#x03B1;((&#x03B4;-21) + 13932*β*&#x03B4;- 1)2+ 31968*β*&#x03B4; - 1)+
                   72 73&#x03B4; - 718&#x03B4;+ 548 (&#x03B4;- 1)
" ></td><td class="equation-label"><br />[10]<br /></td></tr></table>
                                                                                      
                                                                                      
<!--l. 194-->   Equally, we can invert our approximation <a 
href="#x1-2002r9">9<!--tex4ht:ref: approx --></a> above, giving:
   <table 
class="equation"><tr><td><a 
 id="x1-3002r11"></a>
   <center class="math-display" >
<img 
src="images/offset13x.png" alt="&#x03B1; = 1.9485*β* 0.0495055&#x03B4;- 0.577999
" class="math-display" ></center></td><td class="equation-label">[11]</td></tr></table>

## Outer offsetting of an arbitrary normalized curve

Real-world curves are not unit curves (0,1)&#x22C5;&#x22C5;&#x22C5;(1, 0). However, we can always use affine transformation to locate
the start at **a** = (1, 0), leaving the end at **d** = (0,*x*). The control points for a Bezier curve with tension *τ* **B**<sub>**A**</sub>

would then be set at ***b** = (1-τ,0), **c** = (0,x(1-τ))*. The problem, again, is to find the offset curve **B**<sub>**B**</sub> which
best approximates a fixed distance *δ* from **B**<sub>**A**</sub>.

Now we have ***a** = (0, 1 + *δ*), **d** = (x + δ, 0)*. Following exactly the procedure above, the square
of the distance between the two curves at point *t* , is

<table class="multline"><tr><td><img 
src="images/offset14x.png" alt="t2 (&#x03B4; (t(2t- 3)- 3*β*- 1)2) + 3(t- 1)2x(&#x03B1;- *β*2 + (t- 1)2(&#x03B4; + t(&#x03B4; +t(- 3&#x03B1; + 3*β*#x03B4; + 1)- 2&#x03B4;)))2
" ></td><td class="equation-label"><br />[12]<br /></td></tr></table>

and the total error across the curve is

<table class="multline"><tr><td><img 
src="images/offset15x.png" alt="             &#x222B; 1
 E(B  ,B  ) =   (|B  (t)&#x22C5;B  (t)|- &#x03B4;2)2dt
    A   B     0   A      B
  27(14x4 + 15x2 + 14) (&#x03B1; - *β* - 9&#x03B4;(x+ 1)(&#x03B1;- *β*(3(56*β* 45)+ x(- 78*β* 3(56*β*45)x + 26))
       +9 &#x03B4;2(&#x03B1; - *β*(566*β* 9*β*x(33x + 20)+ 33)+ 2*β*283x+ 322)+ 4x(85- 6x)- 24)
                    +2 (9*β*3*β*3*β* 148) +146) - 2138)&#x03B4;3(x + 1)(&#x03B1; - *β*                      + (*β**β**β*129*β* 592) + 292) - 8552)+ 2916)&#x03B4;4
= --------------------------------------30030--------------------------------------
" ></td><td class="equation-label"><br />[13]<br /></td></tr></table>

Once again, it’s only a quartic and three of the variables are given. We can apply the Newton-Raphson
method again, giving:

<table 
class="multline"><tr><td><img 
src="images/offset16x.png" alt="               &#x2032;
  *β*1 = *β*- E-(BA,-BB-)= *β*
             E&#x2032;&#x2032;(BA, BB )     (                           )
                       (   4  1161*β*+)3996*β*+ 1314*β*( 2138 &#x03B4;4    )
             - 54&#x03B4;(x+ 1) 28x2 -(13x + 28 (&#x03B1; - *β* -)108 14x4 + 15x2 +14 (&#x03B1; - *β*
                   (      - 18 387*β*+888*β* 146 &#x03B4;3(x + 1)(&#x03B1; - *β*             )
       - 18&#x03B4;2(&#x03B1; - *β*566*β* 9*β*x(33x+ 20)+ 33)+ 2*β*283x+ 322)+ 4x(85- 6x)- 24 +
                   9&#x03B4;2(&#x03B1; - *β*(18*β*(33x+ 20)+ 33)+ 2x(283x+ 322)+ 566)
               +27 &#x03B4;(x + 1)(&#x03B1; - *β*(3(56*β* 45)+ x(- 78*β* 3(56*β* 45)x+ 26))+
-------------------------2(9*β**β*3*β*-148)+-146)--2138)&#x03B4;3(x-+1)-------------------------
    18(2(387*β*+888*β* 146)&#x03B4;4 + 18&#x03B4;(x+ 1)(28x2 - 13x+ 28)(&#x03B1; - *β* + 18(14x4 + 15x2 + 14)
       (&#x03B1;- *β* - 6(129*β* 148)&#x03B4;3(x + 1)(&#x03B1; - *β* 9&#x03B4;2(x (33x + 20)+ 33)(&#x03B1; - *β* - 2&#x03B4;2(&#x03B1; - *β*         (18*β*(33x+ 20)+ 33)+ 2x(283x+ 322)+ 566)- 3&#x03B4;(x+ 1)(&#x03B1; - *β*3(56*β* 45)+
x(- 78*β* 3(56*β* 45)x+ 26))+ 2(387*β*+ 888*β* 146) &#x03B4;3(x + 1) + &#x03B4;2 (566*β* 9*β*x(33x + 20)+ 33)+
                            2*β*283x+ 322)+ 4x(85- 6x)- 24))
" ></td><td class="equation-label"><br />[14]<br /></td></tr></table>

By iterating this approximation, we can derive the tension for a curve at an offset of a given distance *δ* from
an arbitrary Bezier curve specified by two points and a curve tension parameter.

But wait, it gets more complicated.

## Offsetting at a linear-gradiated distance

Strokes in fonts often have a feature called *contrast*, meaning that the horizontal offset is not the same as the
vertical offset:

<img src="images/offset-4.svg" width="97.04208 " height="78.07367 "/>

To model this we will assume that the desired distance between curves is a linear function of curve time *t* :

<table 
class="equation"><tr><td><a 
 id="x1-5001r15"></a>
   <center class="math-display" >
<img 
src="images/offset17x.png" alt="&#x03B4;(t) = &#x03B4;s(1 - t)+ &#x03B4;et
" class="math-display" ></center></td><td class="equation-label">[15]</td></tr></table>
 

And now our error function is

 <table 
class="equation"><tr><td><a 
 id="x1-5002r16"></a>
   <center class="math-display" >
<img 
src="images/offset18x.png" alt="                  2 2
(|BA (t)&#x22C5;BB (t)|- &#x03B4;(t)) = x
" class="math-display" ></center></td><td class="equation-label">[16]</td></tr></table>

The total integrated error across the curve becomes... very complicated, but computable. We can apply a similar Newton-Raphson method as above, leading to the functions given in the associated Python script.
