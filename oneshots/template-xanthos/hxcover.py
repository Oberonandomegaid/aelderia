"""House of Xanthos robe covers. make_front(art, out, focus) puts the one-shot's art in the robe's open V
with the gold pendant hanging low; make_back(out) is the robe's back with the reverse pendant as the clasp."""
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter
SRC = '/tmp/hx/'
W, H = 1632, 2112                      # page ratio 8.5x11

def _robe(name):
    im = Image.open(SRC + name).convert('RGBA')
    s = W / im.width; im = im.resize((W, round(im.height * s)), Image.LANCZOS)
    top = round(im.height * 0.05)                       # trim a little off the top
    return im.crop((0, top, W, top + H)), s, top

def chain(img, pts, scale=1.0, col=(201, 160, 72)):
    """Draw a link chain along a polyline on an RGBA image."""
    d = ImageDraw.Draw(img)
    P = np.array(pts, float); seg = np.diff(P, axis=0); L = np.hypot(*seg.T); cum = np.cumsum(L); tot = cum[-1]
    step = 15 * scale; n = int(tot / step)
    dark = tuple(int(c * .45) for c in col); hi = (246, 222, 150)
    for i in range(n + 1):
        t = min(i * step, tot - .01); k = int(np.searchsorted(cum, t)); t0 = t - (cum[k] - L[k])
        x, y = P[k] + seg[k] * (t0 / L[k]); ang = np.degrees(np.arctan2(seg[k][1], seg[k][0]))
        a, b = (11 * scale, 6 * scale) if i % 2 else (6 * scale, 4 * scale)
        lk = Image.new('RGBA', (int(40 * scale), int(40 * scale)), (0, 0, 0, 0)); ld = ImageDraw.Draw(lk)
        c = lk.width / 2
        ld.ellipse((c - a + 2, c - b + 3, c + a + 2, c + b + 3), outline=(0, 0, 0, 120), width=max(2, int(4 * scale)))
        ld.ellipse((c - a, c - b, c + a, c + b), outline=dark + (255,), width=max(3, int(5 * scale)))
        ld.ellipse((c - a, c - b, c + a, c + b), outline=col + (255,), width=max(2, int(3 * scale)))
        ld.arc((c - a, c - b, c + a, c + b), 200, 290, fill=hi + (255,), width=max(1, int(2 * scale)))
        lk = lk.rotate(-ang if i % 2 else -ang + 90, resample=Image.BICUBIC)
        img.alpha_composite(lk, (int(x - lk.width / 2), int(y - lk.height / 2)))

def hang(img, name, cx, top, width):
    p = Image.open(SRC + name).convert('RGBA'); s = width / p.width
    p = p.resize((int(p.width * s), int(p.height * s)), Image.LANCZOS)
    sh = Image.new('RGBA', p.size, (0, 0, 0, 0)); sh.putalpha(p.getchannel('A').point(lambda v: v * .55))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(sh, (int(cx - p.width / 2 + 14), int(top + 18)))
    img.alpha_composite(p, (int(cx - p.width / 2), int(top)))
    return p.size

def make_front(art, out, focus=(0.5, 0.35), pend_top=0.47, pend_w=0.2):
    robe, s, top = _robe('robe-front.png')
    a = Image.open(art).convert('RGB')
    # fill the V box (whole cover) with art, cropped to cover the page
    r = max(W / a.width, H / a.height); a = a.resize((round(a.width * r), round(a.height * r)), Image.LANCZOS)
    x = int((a.width - W) * focus[0]); y = int((a.height - H) * focus[1]); a = a.crop((x, y, x + W, y + H)).convert('RGBA')
    a.alpha_composite(robe)
    # where the inner lapel edges meet the top of the page
    al = np.array(robe.getchannel('A'))
    row = al[4]; holes = np.where(row < 128)[0]; xl, xr = holes.min(), holes.max()
    cx = W / 2; pt = H * pend_top; pw = W * pend_w
    loop_y = pt + 4
    chain(a, [(xl + 30, -10), (xl + 120, H * .2), (cx - 70, pt - 70), (cx, loop_y)], 1.6)
    chain(a, [(xr - 30, -10), (xr - 120, H * .2), (cx + 70, pt - 70), (cx, loop_y)], 1.6)
    hang(a, 'pendant.png', cx, pt, pw)
    a.convert('RGB').save(out, quality=90)

def make_back(out, pend_top=0.30, pend_w=0.15):
    robe, s, top = _robe('robe-back.jpg')
    img = robe.copy(); cx = W / 2; pt = H * pend_top; pw = W * pend_w
    chain(img, [(W * .27, -10), (W * .33, H * .12), (cx - 60, pt - 50), (cx, pt + 4)], 1.6)
    chain(img, [(W * .73, -10), (W * .67, H * .12), (cx + 60, pt - 50), (cx, pt + 4)], 1.6)
    hang(img, 'pendant-reverse.png', cx, pt, pw)
    img.convert('RGB').save(out, quality=90)

if __name__ == '__main__':
    make_front('/home/claude/aelderia/oneshots/template-standard/img/cover.jpg', '/tmp/hx/front_test.jpg')
    make_back('/tmp/hx/back_test.jpg')
