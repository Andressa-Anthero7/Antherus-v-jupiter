 function goBack() {
            document.location.reload(true);
        }

        window.onload = function(){
            document.getElementById("btn-back").style.visibility="hidden";
            document.getElementById("caixa-leads").style.background="yellow";
            document.getElementById("caixa-leads").classList.add('disabled');
            document.getElementById("cx-leads-novos").style.visibility="hidden";
            document.getElementById("cx-leads-positivo").style.visibility="hidden";
            document.getElementById("cx-leads-neutro").style.visibility="hidden";
            document.getElementById("cx-leads-negativo").style.visibility="hidden";



        };


        document.getElementById("caixa-leads").onmouseclick = function(){desabilitaCaixa()}
        function desabilitaCaixa(){
            document.getElementById("caixa-leads").style.background="yellow";
            document.getElementById("caixa-leads").style.color="black";
            document.getElementById("leads-novos").style.visibility="hidden";
            document.getElementById("leads-positivo").style.visibility="hidden";
            document.getElementById("leads-neutro").style.visibility="hidden";
            document.getElementById("leads-negativo").style.visibility="hidden";
            document.getElementById("btn-back").style.visibility="visible";
            document.getElementById("btn-back").style.position="relative";
            document.getElementById("btn-back").style.top="-150px";

        };


        document.getElementById("leads-novos").onmouseclick = function() {desabilitaNovos()};
        function desabilitaNovos(){
             document.getElementById("leads-novos").style.background="yellow";
             document.getElementById("leads-novos").style.color="black";
             document.getElementById("leads-novos").style.position="relative";
             document.getElementById("leads-novos").style.top="-39px";
             document.getElementById("leads-novos").classList.add('disabled');

             document.getElementById("caixa-leads").style.visibility="hidden";
             document.getElementById("leads-positivo").style.visibility="hidden";
             document.getElementById("leads-neutro").style.visibility="hidden";
             document.getElementById("leads-negativo").style.visibility="hidden";

             document.getElementById("btn-back").style.visibility="visible";
             document.getElementById("btn-back").style.position="relative";
             document.getElementById("btn-back").style.top="-151px";

             document.getElementById("leads-novos").classList.add('disabled');
             document.getElementById("cx-leads-novos").style.visibility="visible";
             document.getElementById("cx-leads").style.visibility="hidden";




        };

        document.getElementById("leads-positivo").onmouseclick = function() {desabilitaPositivo()};
        function desabilitaPositivo(){
             document.getElementById("leads-positivo").style.background="yellow";
             document.getElementById("leads-positivo").style.color="black";
             document.getElementById("leads-positivo").style.position="relative"
             document.getElementById("leads-positivo").style.top="-73px";
             document.getElementById("leads-positivo").classList.add('disabled');
             document.getElementById("caixa-leads").style.visibility="hidden";
             document.getElementById("leads-novos").style.visibility="hidden";
             document.getElementById("leads-neutro").style.visibility="hidden";
             document.getElementById("leads-negativo").style.visibility="hidden";
             document.getElementById("btn-back").style.visibility="visible";
             document.getElementById("btn-back").style.position="relative";
             document.getElementById("btn-back").style.top="-151px";

             document.getElementById("cx-leads").style.visibility="hidden";
             document.getElementById("cx-leads-novos").style.visibility="hidden";
             document.getElementById("cx-leads-positivo").style.visibility="visible";



        };

        document.getElementById("leads-neutro").onmouseclick = function() {desabilitaNeutro()};
        function desabilitaNeutro(){
             document.getElementById("leads-neutro").style.background="yellow";
             document.getElementById("leads-neutro").style.color="black";
             document.getElementById("leads-neutro").style.position="relative"
             document.getElementById("leads-neutro").style.top="-113px";
             document.getElementById("leads-neutro").classList.add('disabled');
             document.getElementById("caixa-leads").style.visibility="hidden";
             document.getElementById("leads-novos").style.visibility="hidden";
             document.getElementById("leads-positivo").style.visibility="hidden";
             document.getElementById("leads-negativo").style.visibility="hidden";
             document.getElementById("btn-back").style.visibility="visible";
             document.getElementById("btn-back").style.position="relative";
             document.getElementById("btn-back").style.top="-151px";
             document.getElementById("cx-leads").style.visibility="hidden";
             document.getElementById("cx-leads-neutro").style.visibility="visible";


        };

        document.getElementById("leads-negativo").onmouseclick = function() {desabilitaNegativo()};
        function desabilitaNegativo(){
           document.getElementById("leads-negativo").style.background="yellow";
             document.getElementById("leads-negativo").style.color="black";
             document.getElementById("leads-negativo").style.position="relative"
             document.getElementById("leads-negativo").style.top="-153px";
             document.getElementById("leads-negativo").classList.add('disabled');

             document.getElementById("caixa-leads").style.visibility="hidden";
             document.getElementById("leads-novos").style.visibility="hidden";
             document.getElementById("leads-positivo").style.visibility="hidden";
             document.getElementById("leads-neutro").style.visibility="hidden";
             document.getElementById("btn-back").style.visibility="visible";
             document.getElementById("btn-back").style.position="relative";
             document.getElementById("btn-back").style.top="-151px";
             document.getElementById("cx-leads").style.visibility="hidden";
             document.getElementById("cx-leads-negativo").style.visibility="visible";


        };







