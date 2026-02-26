from fractions import Fraction

def unfrac(frac):
    """
    frac: 100/6000s
    """
    if frac == '0s':
        frac = '0/6000s'
    num, denom = frac[:-1].split('/')
    num = eval(num)
    denom = eval(denom)
    # reduce fraction first
    output = Fraction(num, denom)
    return output.numerator, output.denominator

def to_denom(frac, denom):
    """
    frac: p/q
    denom: D
    solution: n/D
    n ~ pD/q
    n = round(pD/q)
    solution = round(pD/q)/D
    """
    p = frac.numerdator
    q = frac.denominator
    D = denom
    n = round(p*D/q)
    return Fraction(n, D)

def to_fps(frac, fps):
    """
    frac = a/b
    fps = p/q
    frac ~ np/q
    n ~ aq/bp
    n = round(aq/bp)
    solution = round(aq/bp)*p/q
    """
    p, q = unfrac(fps)
    a = frac.numerator
    b = frac.denominator
    n = round(a*q/(b*p))
    return Fraction(n*p, q)

# DEPRECIATED. NEVER USE IT UNLESS YOU DON'T MIND INACCURACY. RESULTS DRIFT.
def fcpsec2float(text: str, fps: str='100/6000s') -> float:
    """
    text: xxxx/yyys

    output: float

    >>> fcpsec2float('4.866666666666666s', '100/6000s')
    4.866666666666666

    >>> fcpsec2float('346/60s', '100/6000s')
    5.766666666666667
    """
    if text == '0s':
        num, denom = unfrac(fps)
        text = f'0/{denom}s'
    output = float(Fraction(text[:-1]))
    return output

# DEPRECIATED. NEVER USE IT UNLESS YOU DON'T MIND INACCURACY. RESULTS DRIFT.
def float2fcpsec(x: float, fps: str='100/6000s') -> str:
    """
    x: xxx.yy
    fps: 100/6000s

    output: aaaaaa/bbs
    """
    frac = Fraction(x)
    frac = to_fps(frac, fps)
    return f"{frac.numerator}/{frac.denominator}s"

def fcpsec2frac(text: str):
    if not ('/' in text):
        text = text[:-1] + '/1s'
    return Fraction(text[:-1])

def frac2fcpsec(frac, fps='100/6000s', debug=False):
    num, denom = unfrac(fps)
    if debug:
        print(f"frac2fcpsec. frac: {frac}, desired_denominator: {denom}")
    frac = to_fps(frac, fps)
    if debug:
        print(f"frac2fcpsec. modified_frac: {frac}")
    return f"{frac.numerator}/{frac.denominator}s"

def fcpsec_add(a: str, b: str, fps: str='100/6000s') -> str:
    """
    a: xxxx/yys
    b: aaaa/bbs
    fps: 100/6000s

    returns a plus b
    """
    a = fcpsec2frac(a)
    b = fcpsec2frac(b)
    output = frac2fcpsec(a+b, fps)
    return output

def fcpsec_subtract(a: str, b: str, fps: str='100/6000s') -> str:
    """
    a: xxxx/yys
    b: aaaa/bbs
    fps: 100/6000s

    returns a minus b
    """
    a = fcpsec2frac(a)
    b = fcpsec2frac(b)
    output = frac2fcpsec(a-b, fps)
    return output

def fcpsec_geq(a, b):
    """
    a >= b
    """
    a = fcpsec2frac(a)
    b = fcpsec2frac(b)
    return a >= b

def fcpsec_gt(a, b):
    """
    a > b
    """
    a = fcpsec2frac(a)
    b = fcpsec2frac(b)
    return a > b

# WARNING. USE THIS FOR ROUGH APPROXIMATION WORK, NEVER FOR PRECISE RESULTS.
# FCPSEC TO FLOAT CONVERSION HERE IS VERY ROUGH
def dict2list(x: list[dict]) -> list[list[float]]:
    """
    x: [{'start': 'xxxx/yyys', 'end': 'aaaa/bbs'}, ...]
    output: [[xxx.yy, aaa.bb], ...]
    """
    output = []
    for e in x:
        start = fcpsec2float(e['start'])
        end = fcpsec2float(e['end'])
        output.append([start, end])
    return output

# WARNING. USE THIS FOR ROUGH APPROXIMATION WORK, NEVER FOR PRECISE RESULTS.
# FCPSEC TO FLOAT CONVERSION HERE IS VERY ROUGH
def list2dict(x: list[list[float]]) -> list[dict]:
    """
    x: [[xxx.yy, aaa.bb], ...]
    output: [{'start': 'xxxx/yyys', 'end': 'aaaa/bbs'}, ...]
    """
    output = []
    for e in x:
        d = {}
        d['start'] = float2fcpsec(e[0])
        d['end'] = float2fcpsec(e[1])
        output.append(d)
    return output
