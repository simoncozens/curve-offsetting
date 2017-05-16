

<h2 class="titleHead">Offsetting parameterised Bezier curves</h2>
<div class="author" ><span 
class="cmr-12">Simon Cozens</span></div><br />
<div class="date" ><span 
class="cmr-12">May 16, 2017</span></div>

<!--l. 27--><p class="indent" >   A common problem in type design is the creation of pairs of curves representing the stroke of a pen: an
inner curve and an outer curve delimit the contours of a writing implement of fixed or flexible
thickness. While it is impossible to precisely offset a Bezier curve at a given width, this paper presents
a simple approximation by minimizing the error between desired distance and actual distance.
This can also be applied to situations where the thickness varies linearly across the width of the
curve.
<!--l. 29--><p class="indent" >   We use a simplification due to Tunni, who postulates that any curve <span 
class="cmbx-10">a</span><span 
class="cmmi-10">,</span><span 
class="cmbx-10">b</span><span 
class="cmmi-10">,</span><span 
class="cmbx-10">c</span><span 
class="cmmi-10">,</span><span 
class="cmbx-10">d</span> with straight handles (i.e.
where the control points <span 
class="cmbx-10">b </span>and <span 
class="cmbx-10">c </span>are positioned orthogonally to <span 
class="cmbx-10">a </span>and <span 
class="cmbx-10">d</span>respectively) can be represented in
terms of start and end points <span 
class="cmbx-10">a </span>and <span 
class="cmbx-10">d </span>and a curve tension <span 
class="cmmi-10">&#x03C4;</span>. To determine curve tension, compute the point <span 
class="cmbx-10">T</span>
where <span class='accentvec'><span 
class="cmbx-10">ab</span></span> intersects <span class='accentvec'><span 
class="cmbx-10">cd</span></span>:
<!--l. 32--><p class="indent" >    <img src="images/offset-1.svg" width="84.78429 " height="86.08057 "/>
<!--l. 43--><p class="indent" >   The curve tension is given by the mean of the ratios <img 
src="images/offset0x.png" alt="&#x2225;&#x2225;aabT&#x2225;&#x2225;" > and <img 
src="images/offset1x.png" alt="&#x2225;&#x2225;ddTc&#x2225;&#x2225;" >. Given the points <tspan font-family="cmbx" font-size="10">a</tspan><tspan font-family="cmmi" font-size="10">,</tspan><tspan font-family="cmbx" font-size="10">d</tspan>
and a tension <tspan font-family="cmmi" font-size="10">&#x03C4; </tspan>we can compute the Bezier control points <tspan font-family="cmbx" font-size="10">b</tspan><tspan font-family="cmmi" font-size="10">,</tspan><tspan font-family="cmbx" font-size="10">c</tspan> by setting them at the appropriate
ratios.
<!--l. 45--><p class="indent" >   This conceptualization enables us to find similar parameters for an offset Bezier curve. We will
approach the problem in small pieces, demonstrating the technique first before solving the general
case.
   <h3 class="sectionHead"><span class="titlemark">1   </span> <a 
 id="x1-10001"></a>Outer offset of a unit Bezier curve</h3>
<!--l. 49--><p class="noindent" >Consider first the unit Bezier curve <tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">A</tspan></sub> with <tspan font-family="cmbx" font-size="10">a </tspan>= (0<tspan font-family="cmmi" font-size="10">,</tspan>1)<tspan font-family="cmmi" font-size="10">,</tspan><tspan font-family="cmbx" font-size="10">d </tspan>= (1<tspan font-family="cmmi" font-size="10">,</tspan>0) and <tspan font-family="cmbx" font-size="10">c </tspan>and <tspan font-family="cmbx" font-size="10">d </tspan>chosen as orthogonal control
points with a curve tension <tspan font-family="cmmi" font-size="10">&#x03B1;</tspan>. What are the parameters for a Bezier curve <tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">B</tspan></sub> offsetting this curve on the
outside at a fixed distance <tspan font-family="cmmi" font-size="10">&#x03B4;</tspan>?
<!--l. 52--><p class="indent" >    <img src="images/offset-2.svg" width="78.47368 " height="78.47368 "/>
                                                                                      
                                                                                      
<!--l. 64--><p class="indent" >   Clearly we have <tspan font-family="cmbx" font-size="10">a </tspan>= (0<tspan font-family="cmmi" font-size="10">,</tspan>1 + <tspan font-family="cmmi" font-size="10">&#x03B4;</tspan>)<tspan font-family="cmmi" font-size="10">,</tspan><tspan font-family="cmbx" font-size="10">d </tspan>= (1 + <tspan font-family="cmmi" font-size="10">&#x03B4;,</tspan>0), so it remains to find the curve tension <tspan font-family="cmmi" font-size="10">&#x03B2;</tspan>.
<!--l. 66--><p class="indent" >   As a function of time, the distance between the two curves is:
   <table 
class="equation"><tr><td><a 
 id="x1-1001r1"></a>
   <center class="math-display" >
<img 
src="images/offset2x.png" alt="&#x2225;BA (t)&#x22C5;BB (t)&#x2225;
" class="math-display" ></center></td><td class="equation-label">[1]</td></tr></table>
<!--l. 68--><p class="nopar" >
<!--l. 70--><p class="indent" >   and at any point on the curve, the expected distance is <tspan font-family="cmmi" font-size="10">&#x03B4;</tspan>. Knowing it is impossible to achieve a perfect
offset, we can treat this as an optimization problem: find the value of <tspan font-family="cmmi" font-size="10">&#x03B2; </tspan>which minimizes the total error
function
   <table 
class="equation"><tr><td><a 
 id="x1-1002r2"></a>
   <center class="math-display" >
<img 
src="images/offset3x.png" alt="&#x222B; 1
   (&#x2225;BA (t)&#x22C5;BB (t)&#x2225; - &#x03B4;)2dt
 0
" class="math-display" ></center></td><td class="equation-label">[2]</td></tr></table>
<!--l. 73--><p class="nopar" >
<!--l. 75--><p class="indent" >   This integral turns out to be tricky to compute due to the presence of the square root, so instead we create
an equivalent error function using the square of the distance. We expect the square of the distance to be <tspan font-family="cmmi" font-size="10">&#x03B4;</tspan><sup><tspan font-family="cmr" font-size="7">2</tspan></sup>, and
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
<!--l. 77--><p class="nopar" >
<!--l. 79--><p class="indent" >   For a unit Bezier, we have:
                                                                                      
                                                                                      
<!--l. 81--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset5x.png" alt="       (    3         2          2   )
BA (t) =    t2+ 3(1- t)t + 3&#x03B1;3(1 - t) t 2
         3&#x03B1;t((1 - t)+ (1- t) + 3t(1 - t)                                        )
               (&#x0394; + 1)t3 + 3(1- t)t2((1- &#x03B2;)(&#x0394; +1) +&#x03B2; (&#x0394; + 1))+ 3&#x03B2;(&#x0394; + 1)(1 - t)2t
    BB(t) =  3&#x03B2; (&#x0394; + 1)t2(1 - t)+ 3t(1- t)2((1- &#x03B2;)(&#x0394; + 1)+ &#x03B2;(&#x0394; +1))+ (&#x0394; + 1)(1 - t)3
                                                (  (&#x0394; + 1)t(3&#x03B2;(t- 1)2 +t(3- 2t))  )
                                              =  (&#x0394; + 1)(- (t- 1))((3&#x03B2; - 2)t2 + t+ 1)
" ></td><td class="equation-label"><br />[4]<br /></td></tr></table>
<!--l. 97--><p class="indent" >   leading to a square distance
<!--l. 99--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset6x.png" alt="                2(       2                2           )2
|BA (t)&#x22C5;BB (t)| = t 3&#x03B1; (t - 1) - 3&#x03B2;(&#x0394; + 1)(t- 1) +&#x0394;t (2t - 3) +
                                          (t- 1)2(&#x0394; + t(&#x0394; + t(- 3&#x03B1; + 3&#x03B2;(&#x0394; + 1) - 2&#x0394; )))2
" ></td><td class="equation-label"><br />[5]<br /></td></tr></table>
<!--l. 103--><p class="indent" >   and therefore an error function
<!--l. 105--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset7x.png" alt="            &#x222B; 1                         1  (
E(BA, BB ) =   (|BA (t)&#x22C5;BB (t)|- &#x03B4;2)2dt = 30030 1161(&#x03B1;- &#x03B2; )4 - 36(129&#x03B2; + 148)&#x03B4;(&#x03B1;- &#x03B2; )3+
         (   02           ) 2      2                                 3
       18  387&#x03B2;  + 888&#x03B2; + 146 &#x03B4; (&#x03B1;- &#x03B2;) - 4(9&#x03B2;(3&#x03B2;(43&#x03B2; + 148)+ 146)- 2138)&#x03B4;(&#x03B1; - &#x03B2;)   )
                                          (&#x03B2;(9&#x03B2;(&#x03B2;(129&#x03B2; + 592)+ 292)- 8552)+ 2916)&#x03B4;4
" ></td><td class="equation-label"><br />[6]<br /></td></tr></table>
<!--l. 111--><p class="indent" >   This looks horrific, but it&#8217;s only a quartic, and is easily optimizable. Rather than solving the differential
equation for the general case, let&#8217;s be practical, remember that <tspan font-family="cmmi" font-size="10">&#x03B1; </tspan>and <tspan font-family="cmmi" font-size="10">&#x03B4; </tspan>will be given and go for a numerical
method to minimize the error function.
<!--l. 113--><p class="indent" >   Beginning with <tspan font-family="cmmi" font-size="10">&#x03B2;</tspan><sub><tspan font-family="cmr" font-size="7">1</tspan></sub> = <tspan font-family="cmmi" font-size="10">&#x03B1; </tspan>and applying the Newton-Raphson optimization method gives us an iterated
function
<!--l. 115--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset8x.png" alt="               &#x2032;
  &#x03B2;n+1 = &#x03B2;n - E-(BA,-BB-)
      (      E&#x2032;&#x2032;(BA, BB )            (                )                                 )
                                - 36 387&#x03B2;2 + 888&#x03B2; + 146 &#x03B4;2(&#x03B1; - &#x03B2;)
      ||             - 4(9&#x03B2; (129&#x03B2; + 3(43&#x03B2; + 148)) +9(3&#x03B2;(43&#x03B2; +148)+ 146))&#x03B4;3(&#x03B1; - &#x03B2;)            ||
      ||          +18(774&#x03B2; +888)&#x03B4;2(&#x03B1;- &#x03B2;)2 - 4644&#x03B4;(&#x03B1;- &#x03B2;)3 + 108(129&#x03B2; + 148)&#x03B4;(&#x03B1;- &#x03B2;)2      ||
      (                      - 4644(&#x03B1;- &#x03B2;)3 + (9&#x03B2;(&#x03B2;(129&#x03B2; + 592)+ 292)+                  )
      --&#x03B2;(9&#x03B2;(258&#x03B2;-+-592)+-9(&#x03B2;(129&#x03B2;-+-592)+-292))-- 8552)&#x03B4;4 +-4(9&#x03B2;(3&#x03B2;(43&#x03B2;-+-148)+-146)--2138)&#x03B4;3
= &#x03B2;n-       (              - 4(2322&#x03B2; + 18(129&#x03B2; + 3(43&#x03B2; +148)))&#x03B4;3(&#x03B1; - &#x03B2;)+          )
            |         13932&#x03B4;2(&#x03B1; - &#x03B2; )2 - 72(774&#x03B2; + 888)&#x03B4;2(&#x03B1;- &#x03B2;) + 27864&#x03B4;(&#x03B1; - &#x03B2; )2      |
            ||                       - 216(129&#x03B2; + 148)&#x03B4;(&#x03B1; - &#x03B2;)+                    ||
            ||               13932(&#x03B1; - &#x03B2; )2 + 36(387&#x03B2;2 + 888&#x03B2; + 146)&#x03B4;2+            ||
            |( (&#x03B2;(2322&#x03B2; + 18(258&#x03B2; + 592))+ 2(9&#x03B2; (258&#x03B2; + 592)+ 9(&#x03B2;(129&#x03B2; + 592) + 292)))&#x03B4;4+ |)
                        8(9&#x03B2;(129&#x03B2; + 3(43&#x03B2; + 148))+ 9(3&#x03B2; (43&#x03B2; + 148)+ 146))&#x03B4;3
" ></td><td class="equation-label"><br />[7]<br /></td></tr></table>
<!--l. 136--><p class="indent" >   quickly converges to the minimum error, giving us the optimal curve tension.
<!--l. 138--><p class="indent" >   As an example, plugging in <tspan font-family="cmmi" font-size="10">&#x03B1; </tspan>= 0<tspan font-family="cmmi" font-size="10">.</tspan>55<tspan font-family="cmmi" font-size="10">,</tspan>&#x0394; = 1:
<!--l. 140--><p class="indent" >
<table 
class="align-star">
                                     <tr><td 
class="align-odd"><tspan font-family="cmmi" font-size="10">&#x03B2;</tspan><sub><tspan font-family="cmr" font-size="7">1</tspan></sub> = 0<tspan font-family="cmmi" font-size="10">.</tspan>55</td>                                         <td 
class="align-even"></td>                                     <td 
class="align-label">
                                     </td></tr><tr><td 
class="align-odd"><tspan font-family="cmmi" font-size="10">&#x03B2;</tspan><sub><tspan font-family="cmr" font-size="7">2</tspan></sub> = 0<tspan font-family="cmmi" font-size="10">.</tspan>550987</td>                                     <td 
class="align-even"></td>                                     <td 
class="align-label">
                                     </td></tr><tr><td 
class="align-odd"><tspan font-family="cmmi" font-size="10">&#x03B2;</tspan><sub><tspan font-family="cmr" font-size="7">3</tspan></sub> = 0<tspan font-family="cmmi" font-size="10">.</tspan>550985</td>                                     <td 
class="align-even"></td>                                     <td 
class="align-label">
                                     </td></tr><tr><td 
class="align-odd"><tspan font-family="cmmi" font-size="10">&#x03B2;</tspan><sub><tspan font-family="cmr" font-size="7">4</tspan></sub> = 0<tspan font-family="cmmi" font-size="10">.</tspan>550985</td>                                     <td 
class="align-even"></td>                                     <td 
class="align-label"></td></tr></table>
<!--l. 147--><p class="noindent" >
   <h4 class="subsectionHead"><span class="titlemark">1.1   </span> <a 
 id="x1-20001.1"></a>We can cheat</h4>
<!--l. 149--><p class="noindent" >Thankfully, we find by inspection that the optimal value of <tspan font-family="cmmi" font-size="10">&#x03B2; </tspan>given <tspan font-family="cmmi" font-size="10">&#x03B1; </tspan>and &#x0394;, <tspan font-family="cmmi" font-size="10">&#x03B2;</tspan>(<tspan font-family="cmmi" font-size="10">&#x03B1;,</tspan>&#x0394;) turns out to be pretty
much linear in both <tspan font-family="cmmi" font-size="10">&#x03B1; </tspan>and &#x0394; when <tspan font-family="cmmi" font-size="10">&#x03B1; </tspan><tspan font-family="cmsy" font-size="10">&#x2265; </tspan>0<tspan font-family="cmmi" font-size="10">.</tspan>3. A very pleasing result is:
   <table 
class="equation"><tr><td><a 
 id="x1-2001r8"></a>
                                                                                      
                                                                                      
   <center class="math-display" >
<img 
src="images/offset9x.png" alt="&#x03B2;(&#x03B1;,1) = 0.275985+ &#x03B1;
                  2
" class="math-display" ></center></td><td class="equation-label">[8]</td></tr></table>
<!--l. 153--><p class="nopar" >
<!--l. 155--><p class="indent" >   Note that this gives exactly the answer given by our Newton-Raphson method above. A more general, but
less accurate, approximation is:
   <table 
class="equation"><tr><td><a 
 id="x1-2002r9"></a>
   <center class="math-display" >
<img 
src="images/offset10x.png" alt="&#x03B2;(&#x03B1;,&#x03B4;) = 0.513216&#x03B1; - 0.025407&#x03B4;+ 0.296638
" class="math-display" ></center></td><td class="equation-label">[9]</td></tr></table>
<!--l. 159--><p class="nopar" >
<!--l. 161--><p class="noindent" >
   <h3 class="sectionHead"><span class="titlemark">2   </span> <a 
 id="x1-30002"></a>Inner offsetting of a unit Bezier</h3>
<!--l. 163--><p class="noindent" >What if we want to go the other way, and find the inner curve at a fixed distance?
<!--l. 173--><p class="indent" >   <img src="images/offset-3.svg" width="82.38431 " height="90.84732 "/>
<!--l. 176--><p class="indent" >   A very similar pattern applies, but this time we construct <tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">B</tspan></sub> as <tspan font-family="cmbx" font-size="10">a </tspan>= (0<tspan font-family="cmmi" font-size="10">,</tspan>1 <tspan font-family="cmsy" font-size="10">-</tspan><tspan font-family="cmmi" font-size="10">&#x03B4;,</tspan><tspan font-family="cmbx" font-size="10">d </tspan>= (1 <tspan font-family="cmsy" font-size="10">-</tspan><tspan font-family="cmmi" font-size="10">&#x03B4;,</tspan>0) and the Newton
step <img 
src="images/offset11x.png" alt="E&#x2032;(BA,BB)-
E&#x2032;&#x2032;(BA,BB)" > is
<!--l. 180--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset12x.png" alt="( 18&#x03B1;2 (414&#x03B2;(&#x03B4;- 1)2 + 244(&#x03B4; - 1)2)+ 8&#x03B1; (1098&#x03B2; (&#x03B4; - 1)2 - 108(&#x03B4;- 1)2)+ )
(  4644&#x03B2;3(&#x03B4; - 1)4 + 15984&#x03B2;2(&#x03B4;- 1)4 + 72&#x03B2; (73&#x03B4;2 - 718&#x03B4; + 548) (&#x03B4; - 1)2 )
                - 8(1069&#x03B4;2 + 3439&#x03B4;- 4011)(&#x03B4;- 1)2
-(-----2------2-------------2--------2------4-------------4--)--
  7452&#x03B1; (&#x03B4;- 1) + 8784&#x03B1;((&#x03B4;-21) + 13932&#x03B2;)(&#x03B4;- 1)2+ 31968&#x03B2; (&#x03B4; - 1)+
                   72 73&#x03B4; - 718&#x03B4;+ 548 (&#x03B4;- 1)
" ></td><td class="equation-label"><br />[10]<br /></td></tr></table>
                                                                                      
                                                                                      
<!--l. 194--><p class="indent" >   Equally, we can invert our approximation <a 
href="#x1-2002r9">9<!--tex4ht:ref: approx --></a> above, giving:
   <table 
class="equation"><tr><td><a 
 id="x1-3002r11"></a>
   <center class="math-display" >
<img 
src="images/offset13x.png" alt="&#x03B1; = 1.9485&#x03B2; + 0.0495055&#x03B4;- 0.577999
" class="math-display" ></center></td><td class="equation-label">[11]</td></tr></table>
<!--l. 198--><p class="nopar" >
<!--l. 200--><p class="noindent" >
   <h3 class="sectionHead"><span class="titlemark">3   </span> <a 
 id="x1-40003"></a>Outer offsetting of an arbitrary normalized curve</h3>
<!--l. 202--><p class="noindent" >Real-world curves are not unit curves (0<tspan font-family="cmmi" font-size="10">,</tspan>1)<tspan font-family="cmsy" font-size="10">&#x22C5;&#x22C5;&#x22C5;</tspan>(1<tspan font-family="cmmi" font-size="10">,</tspan>0). However, we can always use affine transformation to locate
the start at <tspan font-family="cmbx" font-size="10">a </tspan>= (1<tspan font-family="cmmi" font-size="10">,</tspan>0), leaving the end at <tspan font-family="cmbx" font-size="10">d </tspan>= (0<tspan font-family="cmmi" font-size="10">,x</tspan>). The control points for a Bezier curve with tension <tspan font-family="cmmi" font-size="10">&#x03C4;</tspan> <tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">A</tspan></sub>
would then be set at <tspan font-family="cmbx" font-size="10">b </tspan>= (1 <tspan font-family="cmsy" font-size="10">-</tspan><tspan font-family="cmmi" font-size="10">&#x03C4;,</tspan>0)<tspan font-family="cmmi" font-size="10">,</tspan><tspan font-family="cmbx" font-size="10">c </tspan>= (0<tspan font-family="cmmi" font-size="10">,x</tspan>(1 <tspan font-family="cmsy" font-size="10">-</tspan><tspan font-family="cmmi" font-size="10">&#x03C4;</tspan>)). The problem, again, is to find the offset curve <tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">B</tspan></sub> which
best approximates a fixed distance <tspan font-family="cmmi" font-size="10">&#x03B4; </tspan>from <tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">A</tspan></sub>.
<!--l. 204--><p class="indent" >   Now we have <tspan font-family="cmbx" font-size="10">a </tspan>= (0<tspan font-family="cmmi" font-size="10">,</tspan>1 + <tspan font-family="cmmi" font-size="10">&#x03B4;</tspan>)<tspan font-family="cmmi" font-size="10">,</tspan><tspan font-family="cmbx" font-size="10">d </tspan>= (<tspan font-family="cmmi" font-size="10">x </tspan>+ <tspan font-family="cmmi" font-size="10">&#x03B4;,</tspan>0). Following exactly the procedure above, <tspan font-family="cmsy" font-size="10">|</tspan><tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">A</tspan></sub>(<tspan font-family="cmmi" font-size="10">t</tspan>) <tspan font-family="cmsy" font-size="10">&#x22C5;</tspan><tspan font-family="cmbx" font-size="10">B</tspan><sub><tspan font-family="cmbx" font-size="7">B</tspan></sub>(<tspan font-family="cmmi" font-size="10">t</tspan>)<tspan font-family="cmsy" font-size="10">|</tspan>, the square
of the distance between the two curves at point <tspan font-family="cmmi" font-size="10">t</tspan>, is
<!--l. 206--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset14x.png" alt="t2 (&#x03B4; (t(2t- 3)- 3&#x03B2;(t- 1)2) + 3(t- 1)2x(&#x03B1;- &#x03B2;))2 + (t- 1)2(&#x03B4; + t(&#x03B4; +t(- 3&#x03B1; + 3&#x03B2;(&#x03B4; + 1)- 2&#x03B4;)))2
" ></td><td class="equation-label"><br />[12]<br /></td></tr></table>
<!--l. 210--><p class="indent" >   and the total error across the curve is
<!--l. 212--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset15x.png" alt="             &#x222B; 1
 E(B  ,B  ) =   (|B  (t)&#x22C5;B  (t)|- &#x03B4;2)2dt
    A   B     0   A      B
  27(14x4 + 15x2 + 14) (&#x03B1; - &#x03B2;)4 - 9&#x03B4;(x+ 1)(&#x03B1;- &#x03B2;)3(3(56&#x03B2; + 45)+ x(- 78&#x03B2; + 3(56&#x03B2; +45)x + 26))
       +9 &#x03B4;2(&#x03B1; - &#x03B2;)2(566&#x03B2; + 9&#x03B2;2(x(33x + 20)+ 33)+ 2&#x03B2;x(283x+ 322)+ 4x(85- 6x)- 24)
                    +2 (9&#x03B2; (3&#x03B2;(43&#x03B2; + 148) +146) - 2138)&#x03B4;3(x + 1)(&#x03B1; - &#x03B2;)
                      + (&#x03B2;(9&#x03B2; (&#x03B2; (129&#x03B2; + 592) + 292) - 8552)+ 2916)&#x03B4;4
= --------------------------------------30030--------------------------------------
" ></td><td class="equation-label"><br />[13]<br /></td></tr></table>
<!--l. 222--><p class="indent" >   Once again, it&#8217;s only a quartic and three of the variables are given. We can apply the Newton-Raphson
method again, giving:
<!--l. 224--><p class="indent" >   <table 
class="multline"><tr><td><img 
src="images/offset16x.png" alt="               &#x2032;
  &#x03B2;n+1 = &#x03B2;n - E-(BA,-BB-)= &#x03B2;n-
             E&#x2032;&#x2032;(BA, BB )     (                           )
                       (   4  1161&#x03B2;3 +)3996&#x03B2;2 + 1314&#x03B2; -( 2138 &#x03B4;4    )
             - 54&#x03B4;(x+ 1) 28x2 -(13x + 28 (&#x03B1; - &#x03B2;)3 -)108 14x4 + 15x2 +14 (&#x03B1; - &#x03B2;)3
                   (      - 18 387&#x03B2;2 +888&#x03B2; + 146 &#x03B4;3(x + 1)(&#x03B1; - &#x03B2;)              )
       - 18&#x03B4;2(&#x03B1; - &#x03B2;) 566&#x03B2; + 9&#x03B2;2(x(33x+ 20)+ 33)+ 2&#x03B2;x(283x+ 322)+ 4x(85- 6x)- 24 +
                   9&#x03B4;2(&#x03B1; - &#x03B2;)2(18&#x03B2;(x(33x+ 20)+ 33)+ 2x(283x+ 322)+ 566)
               +27 &#x03B4;(x + 1)(&#x03B1; - &#x03B2;)2(3(56&#x03B2; + 45)+ x(- 78&#x03B2; + 3(56&#x03B2; + 45)x+ 26))+
-------------------------2(9&#x03B2;(3&#x03B2;(43&#x03B2; +-148)+-146)--2138)&#x03B4;3(x-+1)-------------------------
    18(2(387&#x03B2;2 +888&#x03B2; + 146)&#x03B4;4 + 18&#x03B4;(x+ 1)(28x2 - 13x+ 28)(&#x03B1; - &#x03B2;)2 + 18(14x4 + 15x2 + 14)
       (&#x03B1;- &#x03B2;)2 - 6(129&#x03B2; + 148)&#x03B4;3(x + 1)(&#x03B1; - &#x03B2;)+ 9&#x03B4;2(x (33x + 20)+ 33)(&#x03B1; - &#x03B2;)2 - 2&#x03B4;2(&#x03B1; - &#x03B2;)
         (18&#x03B2;(x(33x+ 20)+ 33)+ 2x(283x+ 322)+ 566)- 3&#x03B4;(x+ 1)(&#x03B1; - &#x03B2;)(3(56&#x03B2; + 45)+
x(- 78&#x03B2; + 3(56&#x03B2; + 45)x+ 26))+ 2(387&#x03B2;2 + 888&#x03B2; + 146) &#x03B4;3(x + 1) + &#x03B4;2 (566&#x03B2; + 9&#x03B2;2(x(33x + 20)+ 33)+
                            2&#x03B2;x(283x+ 322)+ 4x(85- 6x)- 24))
" ></td><td class="equation-label"><br />[14]<br /></td></tr></table>
<!--l. 240--><p class="indent" >   By iterating this approximation, we can derive the tension for a curve at an offset of a given distance <tspan font-family="cmmi" font-size="10">&#x03B4; </tspan>from
an arbitrary Bezier curve specified by two points and a curve tension parameter.
<!--l. 242--><p class="indent" >   But wait, it gets more complicated.
<!--l. 244--><p class="noindent" >
   <h3 class="sectionHead"><span class="titlemark">4   </span> <a 
 id="x1-50004"></a>Offsetting at a linear-gradiated distance</h3>
<!--l. 246--><p class="noindent" >Strokes in fonts often have a feature called <tspan font-family="cmti" font-size="10">contrast</tspan>, meaning that the horizontal offset is not the same as the
vertical offset:
<!--l. 249--><p class="indent" >    <img src="images/offset-4.svg" width="97.04208 " height="78.07367 "/>
<!--l. 259--><p class="indent" >   To model this we will assume that the desired distance between curves is a linear function of curve time
<tspan font-family="cmmi" font-size="10">t</tspan>:
   <table 
class="equation"><tr><td><a 
 id="x1-5001r15"></a>
   <center class="math-display" >
<img 
src="images/offset17x.png" alt="&#x03B4;(t) = &#x03B4;s(1 - t)+ &#x03B4;et
" class="math-display" ></center></td><td class="equation-label">[15]</td></tr></table>
                                                                                      
                                                                                      
<!--l. 263--><p class="nopar" >
<!--l. 265--><p class="indent" >   And now our error function is
   <table 
class="equation"><tr><td><a 
 id="x1-5002r16"></a>
   <center class="math-display" >
<img 
src="images/offset18x.png" alt="                  2 2
(|BA (t)&#x22C5;BB (t)|- &#x03B4;(t)) = x
" class="math-display" ></center></td><td class="equation-label">[16]</td></tr></table>
<!--l. 268--><p class="nopar" >
<!--l. 270--><p class="indent" >   The total integrated error across the curve becomes&#x2026;&#x00A0;very complicated, but computable. We can apply a
similar Newton-Raphson method as above, leading to the functions given in the associated Python
script.

