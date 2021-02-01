mini = true;
mostra= true;
//Função do Menu Lateral
function toggleSidebar() {
  if (mini) {
    document.getElementById("mySidebar").style.width = "200px";
    document.getElementById("main").style.marginLeft = "200px";
    document.getElementById("header2").style.marginLeft = "191px";

    this.mini = false;
  } else {
    document.getElementById("mySidebar").style.width = "60px";
    document.getElementById("main").style.marginLeft = "60px";
    document.getElementById("header2").style.marginLeft = "51px";
    this.mini = true;
  }
}

//Função para mostrar as opções do usuário no lado superior direito.
function mostra_usuario(){
  if(mostra){
    document.getElementById("log").style.display="block";
    mostra= false;
  } else {
    document.getElementById("log").style.display="none";
    mostra=true;
  }
}


