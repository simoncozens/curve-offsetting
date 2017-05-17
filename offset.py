# "Offsetting parameterised Bezier curves"

# Preparatory stuff: Simplified affine transforms

# Find a simplified affine transform
def unitize(a,b,c,d):
  # Not going to do rotation here, just translation and scaling for now;
  # assume all points are orthogonal
  return { "dx": -a[0], "dy": -d[1], "scale": float(a[1]-d[1])}

def apply1(a, transform):
  return [ (a[0]+transform["dx"]) / transform["scale"],
           (a[1]+transform["dy"]) / transform["scale"] ]

def unapply1(a, transform):
  return [ (a[0]*transform["scale"])-transform["dx"],
           (a[1]*transform["scale"])-transform["dy"] ]

def applyTransform(bez, transform):
  return map(lambda (z): apply1(z,transform), bez)

def applyInvertedTransform(bez, transform):
  return map(lambda (z): unapply1(z,transform), bez)

# Preparatory stuff: Determining curve tension
# (Mostly stolen with modification from mekkablue)

# We could simplify this dramatically given that we're expecting
# orthogonality, but hey, generalize first and things are free later.
def lineLineIntersection(a,b,c,d):
  xdiff = (a[0] - b[0], c[0] - d[0])
  ydiff = (a[1] - b[1], c[1] - d[1])

  def det(a, b):
      return a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
     raise Exception('lines do not intersect')

  d = (det(a,b), det(c,d))
  x = det(d, xdiff) / float(div)
  y = det(d, ydiff) / float(div)
  return [x, y]

def pointDistance( a, b):
  return ( (float(b[0]) - float(a[0]))**2 + (float(b[1]) - float(a[1]))**2 ) ** 0.5

def lerp(t,a,b):
  return [int((1-t)*a[0] + t*b[0]), int((1-t)*a[1] + t*b[1])]

def normalizedTunniPoint(a,b):
  return [max(a[0],b[0]),max(a[1],b[1])]

def tension(bez):
  tunniP = lineLineIntersection( *bez )
  percentageP1P2 = pointDistance( bez[0], bez[1] ) / pointDistance( bez[0], tunniP )
  percentageP3P4 = pointDistance( bez[3], bez[2] ) / pointDistance( bez[3], tunniP )
  return ( percentageP1P2 + percentageP3P4 ) / 2

def curveWithTension(start, end, tension):
  return [start,
    lerp(tension, start, normalizedTunniPoint(start, end)),
    lerp(tension, end, normalizedTunniPoint(start, end)),
  end]

# Glyphs stuff
# def arrayToGSPath(bez):
#   p = GSPath.new()
#   nodes = map(lambda f: GSNode(NSMakePoint(f[0],f[1]),OFFCURVE), bez)
#   nodes[0].type = LINE
#   nodes[3].type = CURVE
#   p.nodes = nodes
#   p.closed = False
#   return p

# def segToArray(s):
#   return map(lambda f: [f.x,f.y], s)

# Now the offsetting code

def findBeta(x,alpha,dStart,dEnd):
  i = 0
  beta = alpha
  while i < 5:
    i = i + 1
    newtonstep = (6*(218*dEnd**4 + 218*dStart**3*(1 + dStart) + dEnd**2*dStart*(75 + 150*dStart - 2431*x) + dEnd*dStart**2*(-2431 - 2431*dStart + 75*x) + dEnd**3*(-2431*dStart + 218*x)) - 162*alpha**3*(28 + 15*dEnd*x + 30*x**2 + 28*dEnd*x**3 + 28*x**4 + dStart*(28 + 15*x**2)) + 324*beta**3*(14 + 14*dEnd**4 + 56*dStart**3 + 14*dStart**4 + 56*dEnd**3*x + 15*x**2 + 14*x**4 + 3*dStart**2*(28 + 5*x**2) + 3*dEnd**2*(5 + 10*dStart + 5*dStart**2 + 28*x**2) + 2*dEnd*x*(15 + 30*dStart + 15*dStart**2 + 28*x**2) + dStart*(56 + 30*x**2)) + 81*beta**2*(135*dEnd**4 + 405*dEnd**3*x + dEnd*x*(161 + 644*dStart + 483*dStart**2 + 135*x**2) + dStart*(1 + dStart)*(135 + 270*dStart + 135*dStart**2 + 161*x**2) + dEnd**2*(161 + 483*dStart + 322*dStart**2 + 405*x**2)) + 18*beta*(518*dEnd**4 + dEnd**3*(-715*dStart + 1036*x) + dStart**2*(518 + 1036*dStart + 518*dStart**2 + 125*x**2) - 5*dEnd*dStart*(143 + 143*dStart**2 + dStart*(286 - 254*x) - 204*x + 143*x**2) + dEnd**2*(125 + 1270*dStart**2 + dStart*(1270 - 1430*x) + 518*x**2)) + 9*alpha**2*(54*beta*(28 + 30*x**2 + 28*x**4 + dStart**2*(28 + 5*x**2) + dEnd**2*(5 + 28*x**2) + 2*dEnd*x*(15 + 10*dStart + 28*x**2) + dStart*(56 + 30*x**2)) + 3*(dEnd**2*(161 + 405*x**2) + dEnd*x*(483 + 644*dStart + 405*x**2) + dStart*(405 + 483*x**2 + dStart*(405 + 161*x**2)))) - 3*alpha*(162*beta**2*(28 + 28*dStart**3 + 28*dEnd**3*x + 30*x**2 + 28*x**4 + 3*dStart**2*(28 + 5*x**2) + 3*dEnd**2*(5 + 5*dStart + 28*x**2) + 3*dEnd*x*(15 + 20*dStart + 5*dStart**2 + 28*x**2) + dStart*(84 + 45*x**2)) + 6*(518*dEnd**3*x + dStart**2*(518 + 518*dStart + 125*x**2) + dEnd**2*(125 + dStart*(635 - 715*x) + 518*x**2) + 5*dEnd*dStart*(-143 + 204*x - 143*x**2 + dStart*(-143 + 127*x))) + 18*beta*(405*dEnd**3*x + dEnd*x*(483 + 1288*dStart + 483*dStart**2 + 405*x**2) + dEnd**2*(322 + 483*dStart + 810*x**2) + dStart*(405 + 405*dStart**2 + 483*x**2 + dStart*(810 + 322*x**2)))))/(486*alpha**2*(28 + 30*x**2 + 28*x**4 + dStart**2*(28 + 5*x**2) + dEnd**2*(5 + 28*x**2) + 2*dEnd*x*(15 + 10*dStart + 28*x**2) + dStart*(56 + 30*x**2)) + 972*beta**2*(14 + 14*dEnd**4 + 56*dStart**3 + 14*dStart**4 + 56*dEnd**3*x + 15*x**2 + 14*x**4 + 3*dStart**2*(28 + 5*x**2) + 3*dEnd**2*(5 + 10*dStart + 5*dStart**2 + 28*x**2) + 2*dEnd*x*(15 + 30*dStart + 15*dStart**2 + 28*x**2) + dStart*(56 + 30*x**2)) + 162*beta*(135*dEnd**4 + 405*dEnd**3*x + dEnd*x*(161 + 644*dStart + 483*dStart**2 + 135*x**2) + dStart*(1 + dStart)*(135 + 270*dStart + 135*dStart**2 + 161*x**2) + dEnd**2*(161 + 483*dStart + 322*dStart**2 + 405*x**2)) + 18*(518*dEnd**4 + dEnd**3*(-715*dStart + 1036*x) + dStart**2*(518 + 1036*dStart + 518*dStart**2 + 125*x**2) - 5*dEnd*dStart*(143 + 143*dStart**2 + dStart*(286 - 254*x) - 204*x + 143*x**2) + dEnd**2*(125 + 1270*dStart**2 + dStart*(1270 - 1430*x) + 518*x**2)) - 3*alpha*(324*beta*(28 + 28*dStart**3 + 28*dEnd**3*x + 30*x**2 + 28*x**4 + 3*dStart**2*(28 + 5*x**2) + 3*dEnd**2*(5 + 5*dStart + 28*x**2) + 3*dEnd*x*(15 + 20*dStart + 5*dStart**2 + 28*x**2) + dStart*(84 + 45*x**2)) + 18*(405*dEnd**3*x + dEnd*x*(483 + 1288*dStart + 483*dStart**2 + 405*x**2) + dEnd**2*(322 + 483*dStart + 810*x**2) + dStart*(405 + 405*dStart**2 + 483*x**2 + dStart*(810 + 322*x**2)))))
    beta = beta - newtonstep
  return beta

# And this is the main routine
def offset(bez, d1, d2=None):
  if not d2:
    d2 = d1
  if bez[0][0] > bez[3][0]:
    bez = list(reversed(bez))
  tr = unitize(*bez)
  bez2 = applyTransform(bez,tr)
  alpha = tension(bez)
  scaledD1 = d1 / tr["scale"]
  scaledD2 = d2 / tr["scale"]
  beta = findBeta(bez2[3][0], alpha, scaledD1, scaledD2)
  offsetCurve = curveWithTension(
    [bez[0][0], bez[0][1]+d1],
    [bez[3][0]+d2, bez[3][1]],
    beta
  )
  return offsetCurve
