var c = function (e) {
    function t(e, t) {
        return e << t | e >>> 32 - t
    }

    function n(e, t) {
        var n, o, r, i, a;
        return r = 2147483648 & e,
            i = 2147483648 & t,
            a = (1073741823 & e) + (1073741823 & t),
            (n = 1073741824 & e) & (o = 1073741824 & t) ? 2147483648 ^ a ^ r ^ i : n | o ? 1073741824 & a ? 3221225472 ^ a ^ r ^ i : 1073741824 ^ a ^ r ^ i : a ^ r ^ i
    }

    function o(e, o, r, i, a, s, c) {
        return n(t(e = n(e, n(n(function (e, t, n) {
            return e & t | ~e & n
        }(o, r, i), a), c)), s), o)
    }

    function r(e, o, r, i, a, s, c) {
        return n(t(e = n(e, n(n(function (e, t, n) {
            return e & n | t & ~n
        }(o, r, i), a), c)), s), o)
    }

    function i(e, o, r, i, a, s, c) {
        return n(t(e = n(e, n(n(function (e, t, n) {
            return e ^ t ^ n
        }(o, r, i), a), c)), s), o)
    }

    function a(e, o, r, i, a, s, c) {
        return n(t(e = n(e, n(n(function (e, t, n) {
            return t ^ (e | ~n)
        }(o, r, i), a), c)), s), o)
    }

    function s(e) {
        var t, n = "", o = "";
        for (t = 0; 3 >= t; t++)
            n += (o = "0" + (e >>> 8 * t & 255).toString(16)).substr(o.length - 2, 2);
        return n
    };


    var c, u, p, l, f, d, m, y, g, v;
    for (v = function (e) {
        for (var t, n = e.length, o = n + 8, r = 16 * ((o - o % 64) / 64 + 1), i = new Array(r - 1), a = 0, s = 0; n > s;)
            a = s % 4 * 8,
                i[t = (s - s % 4) / 4] = i[t] | e.charCodeAt(s) << a,
                s++;
        return a = s % 4 * 8,
            i[t = (s - s % 4) / 4] = i[t] | 128 << a,
            i[r - 2] = n << 3,
            i[r - 1] = n >>> 29,
            i
    }(e = function (e) {
        for (var t = "", n = 0; n < e.length; n++) {
            var o = e.charCodeAt(n);
            128 > o ? t += String.fromCharCode(o) : o > 127 && 2048 > o ? (t += String.fromCharCode(o >> 6 | 192),
                t += String.fromCharCode(63 & o | 128)) : (t += String.fromCharCode(o >> 12 | 224),
                t += String.fromCharCode(o >> 6 & 63 | 128),
                t += String.fromCharCode(63 & o | 128))
        }
        return t
    }(e)),
             d = 1732584193,
             m = 4023233417,
             y = 2562383102,
             g = 271733878,
             c = 0; c < v.length; c += 16)
        u = d,
            p = m,
            l = y,
            f = g,
            m = a(m = a(m = a(m = a(m = i(m = i(m = i(m = i(m = r(m = r(m = r(m = r(m = o(m = o(m = o(m = o(m, y = o(y, g = o(g, d = o(d, m, y, g, v[c + 0], 7, 3614090360), m, y, v[c + 1], 12, 3905402710), d, m, v[c + 2], 17, 606105819), g, d, v[c + 3], 22, 3250441966), y = o(y, g = o(g, d = o(d, m, y, g, v[c + 4], 7, 4118548399), m, y, v[c + 5], 12, 1200080426), d, m, v[c + 6], 17, 2821735955), g, d, v[c + 7], 22, 4249261313), y = o(y, g = o(g, d = o(d, m, y, g, v[c + 8], 7, 1770035416), m, y, v[c + 9], 12, 2336552879), d, m, v[c + 10], 17, 4294925233), g, d, v[c + 11], 22, 2304563134), y = o(y, g = o(g, d = o(d, m, y, g, v[c + 12], 7, 1804603682), m, y, v[c + 13], 12, 4254626195), d, m, v[c + 14], 17, 2792965006), g, d, v[c + 15], 22, 1236535329), y = r(y, g = r(g, d = r(d, m, y, g, v[c + 1], 5, 4129170786), m, y, v[c + 6], 9, 3225465664), d, m, v[c + 11], 14, 643717713), g, d, v[c + 0], 20, 3921069994), y = r(y, g = r(g, d = r(d, m, y, g, v[c + 5], 5, 3593408605), m, y, v[c + 10], 9, 38016083), d, m, v[c + 15], 14, 3634488961), g, d, v[c + 4], 20, 3889429448), y = r(y, g = r(g, d = r(d, m, y, g, v[c + 9], 5, 568446438), m, y, v[c + 14], 9, 3275163606), d, m, v[c + 3], 14, 4107603335), g, d, v[c + 8], 20, 1163531501), y = r(y, g = r(g, d = r(d, m, y, g, v[c + 13], 5, 2850285829), m, y, v[c + 2], 9, 4243563512), d, m, v[c + 7], 14, 1735328473), g, d, v[c + 12], 20, 2368359562), y = i(y, g = i(g, d = i(d, m, y, g, v[c + 5], 4, 4294588738), m, y, v[c + 8], 11, 2272392833), d, m, v[c + 11], 16, 1839030562), g, d, v[c + 14], 23, 4259657740), y = i(y, g = i(g, d = i(d, m, y, g, v[c + 1], 4, 2763975236), m, y, v[c + 4], 11, 1272893353), d, m, v[c + 7], 16, 4139469664), g, d, v[c + 10], 23, 3200236656), y = i(y, g = i(g, d = i(d, m, y, g, v[c + 13], 4, 681279174), m, y, v[c + 0], 11, 3936430074), d, m, v[c + 3], 16, 3572445317), g, d, v[c + 6], 23, 76029189), y = i(y, g = i(g, d = i(d, m, y, g, v[c + 9], 4, 3654602809), m, y, v[c + 12], 11, 3873151461), d, m, v[c + 15], 16, 530742520), g, d, v[c + 2], 23, 3299628645), y = a(y, g = a(g, d = a(d, m, y, g, v[c + 0], 6, 4096336452), m, y, v[c + 7], 10, 1126891415), d, m, v[c + 14], 15, 2878612391), g, d, v[c + 5], 21, 4237533241), y = a(y, g = a(g, d = a(d, m, y, g, v[c + 12], 6, 1700485571), m, y, v[c + 3], 10, 2399980690), d, m, v[c + 10], 15, 4293915773), g, d, v[c + 1], 21, 2240044497), y = a(y, g = a(g, d = a(d, m, y, g, v[c + 8], 6, 1873313359), m, y, v[c + 15], 10, 4264355552), d, m, v[c + 6], 15, 2734768916), g, d, v[c + 13], 21, 1309151649), y = a(y, g = a(g, d = a(d, m, y, g, v[c + 4], 6, 4149444226), m, y, v[c + 11], 10, 3174756917), d, m, v[c + 2], 15, 718787259), g, d, v[c + 9], 21, 3951481745),
            d = n(d, u),
            m = n(m, p),
            y = n(y, l),
            g = n(g, f);
    return (s(d) + s(m) + s(y) + s(g)).toLowerCase()
}


