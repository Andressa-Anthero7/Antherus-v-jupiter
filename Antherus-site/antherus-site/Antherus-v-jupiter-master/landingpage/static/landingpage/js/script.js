/*function mascaraDeTelefone(telefone){
    const textoAtual = telefone.value;
    const isCelularnove = textoAtual.length === 11 || textoAtual.length === 10 ;

    const isnotCelular = textoAtual.length >11 || textoAtual.length < 10  ;

    let textoAjustado;
    if(isCelularnove) {
    	const ddd = textoAtual.slice(0,2)
        const parte1 = textoAtual.slice(2,11);

        textoAjustado = `(${ddd}) ${parte1}`
    } else{
    	const ddd = textoAtual.slice(0,2)
        const parte1 = textoAtual.slice(2,10);
        textoAjustado = `(${ddd}) ${parte1} `
    } if(isnotCelular){
        alert("Não é número de Celular Válido")
    }

    telefone.value = textoAjustado;
}
*/


const piscar = setInterval(function() {
	document.getElementById("text-blink").style.visibility="hidden";
	document.getElementById("text-static").style.visibility="visible";
	$('.btn').div(' btn-what-app').addClass('btn-warning');
}, 5000);






document.getElementById("abremenu").onmouseclick = function() {abreMenu()};




function abreMenu(){
	$("#img-banner").hide();
	document.getElementById("navegacao").style.width="100%";
	$("#img-main").hide();

	document.getElementById("conteudo-principal").style.position="relative";
	document.getElementById("conteudo-principal").style.top="400px";
	document.getElementById("footer").style.top="400px";


	$("#abre-menu").hide();
	document.getElementById("fecha-menu").style.display="initial"




};


document.getElementById("fechamenu").onmouseclick = function() {fechaMenu()};


function fechaMenu(){
	$("#img-main").show();
	document.getElementById("img-main").style.position="relative";
	document.getElementById("img-main").style.top="95px";
	document.getElementById("fecha-menu").style.display="none"

	document.getElementById("footer").style.top="120px";

	document.getElementById("conteudo-principal").style.position="relative";
	document.getElementById("conteudo-principal").style.top="100px";



	$("#abre-menu").show();



};