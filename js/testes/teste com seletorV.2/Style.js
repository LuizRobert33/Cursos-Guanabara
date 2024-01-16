function Somar(){
    var tn1 = window.document.getElementById("N1")
    var tn2 = window.document.getElementById("N2")
    var res = window.document.getElementById("res")
    n1 = Number(tn1.value)
    n2 = Number(tn2.value)
    var s = n1 + n2
    res.innerText = `A soma entre ${n1} e ${n2} e ${s}`



}