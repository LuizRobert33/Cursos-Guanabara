function verificar() {
    var data = new Date();
    var ano = data.getFullYear();
    var anof = window.document.getElementById('Numero');
    var res = window.document.getElementById('res');
    
    if(anof.value.length == 0 || anof.value > ano) {
      window.alert('[ERRO] TENTE NOVAMENTE!!');
    } else {
      var fsex = window.document.getElementsByName('radsex') //Se usar getElementsByid voce consegue selecionar so 1 id
      var idade = ano - Number(anof.value)
      genero = ''
      if(fsex[0].checked) {
        genero = 'Homem'
      } else if (fsex[1].checked){
        genero = 'Mulher'
      }
       res.innerHTML = `Detectamos ${genero} de ${idade} anos de idade `
       res.style.textAlign = 'Center'
    }
   
  }
  