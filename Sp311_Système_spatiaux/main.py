from math import sqrt, asin, sin, cos, radians, acos, pi, degrees, tan

class SpProblem:
    def __init__(self, a: float, e: float, i: float, mu: float, w: float, iterate: list, lomega: float) -> None:
        """
        Parameters
        ---

        - a : demi grand axe
        - e : exentricité
        - i : inclinaison
        - mu : reduction gravitationnelle
        - w : argument de periaxe
        - iterate : liste des angles de calcul
        """
        self.a = a ; self.e = e ; self.i = i; self.mu = mu; self.vc = acos(-e); self.w = w; self.lomega = lomega

        self.T = 2 * pi * sqrt(a ** 3 / mu)
        self.alpha_o = 360 / 86128

        self.tpbase = self.tp(assend=True)
        self.ts = [self.t(i) for i in iterate]

        self.lasRad = [self.la(i) for i in iterate]
        self.lasDeg = [round(degrees(i), 1) for i in self.lasRad]

        self.losRad = [self.lo(i, j) for i, j in zip(self.lasRad, iterate)]
        self.losDeg = [round(degrees(i), 1) for i in self.losRad]

        self.lssRad = [self.ls(i, j) for i, j in zip(self.losRad, self.ts)]
        self.lssDeg = [round(degrees(i), 1) for i in self.lssRad]

    def intermed(self, v: float) -> float:
        return sqrt(1 - self.e**2) * sin(v) / (1 + self.e * cos(v))

    def tp(self, v: float = 0, assend: bool = False):
        if assend:
            v = - self.w

        coef = 0 if abs(v) <= self.vc else 1 if abs(v) <= 2*pi - self.vc else 2
        m = 1 if v < - self.vc else 0
        j = 0 if self.i < 90 else 1

        upper = (-1) ** m * (-1) ** j * coef * pi
        multiplier = (-1) ** coef
        returned = sqrt(self.a**3 / self.mu) * (upper + multiplier * asin(self.intermed(v)) - self.e * self.intermed(v))

        if assend:
            return - returned
        return returned

    def t(self, v: float):
        return self.tp(v) + self.tp(assend=True)
    
    def la(self, v: float):
        return asin(sin(self.i)*sin(self.w + v))
    
    def lo(self, la: float, v: float):
        upper = - ((( - self.w + pi / 2) - v) // pi) # coté graduel positif
        sign = (-1) ** (upper)
        return pi * upper + sign * asin(tan(la)/tan(self.i))
    
    def ls(self, lo: float, t: float):
        return self.lomega + lo - radians(self.alpha_o * t)
    
class Orbital:
    def __init__(self, mu: float, a: float = 0, e: float = 0, ra: float = 0, rp: float = 0) -> None:
        self.a = (ra + rp) / 2 if a == 0 else a
        self.e = (ra - rp) / (ra + rp)
        self.ra = a * (1 + e) if ra == 0 else ra
        self.rp = a * (1 - e) if rp == 0 else rp
        self.rt = 6373
        self.va = self.velocity(ra, mu)
        self.vp = self.velocity(rp, mu)
        self.T =  2 * pi * sqrt(a**3 / mu)

    def velocity(self, r: float, mu: float):
        return sqrt(mu * (2 / r - 1 / self.a))

iterate = [-200, -160, 40, 80, 160, 200]
iterate = [radians(i) for i in iterate]

new = SpProblem(87734, 0.799, radians(70.2), 398600, radians(-150), iterate, radians(51.6))
print(new.losDeg)
print(new.lssDeg)
 