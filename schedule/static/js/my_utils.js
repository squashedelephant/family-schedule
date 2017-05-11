function convertSpace(s) {
    var l = s.split(" ");
    var s2 = "";
    for (word in l) {
        if (s2.length > 0) {
            s2 += "%20";
            s2 += l[word];
        } else {
            s2 = l[word];
        }
    }
    return s;
}

function displayTime() {
    function padValue(s) {
        if (s < 10) {
            s = "0" +s;
        }
        return s;
    }
    var t = new Date();
    var h, m, s;
    h = t.getHours();
    m = t.getMinutes();
    s = t.getSeconds();
    m = padValue(m);
    s = padValue(s);
    return h + ":" + m + ":" + s;
}
