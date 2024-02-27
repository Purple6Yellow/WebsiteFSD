//Ajax functie 

$(document).ready(function () {
   
    $('#btnLoad').on('click', function () {
        
        $('#divResult1').load('/Blog5.html div:first');
        $('#divResult2').load('/Blog5.html #tweede');
        $('#divResult3').load('/Blog5.html div:third');

    });
   
    $('#btnLoad').on('click', function () {   
    const urlPagina = '/Blog5.html';
        $.ajax({
            url: urlPagina, 
            success: function(data){
                //Toon data in de div in de pagina
                $('#divResult11').html(data);
                $('#divResult1').load('/Blog5.html div:first');
                $('#divResult2').load('/Blog5.html #tweede');
                $('#divResult3').load('/Blog5.html #derde');
            },
            error: function(){
                $('#divResult1').html('FOUT: Er is iets fout gegaan!');
            }
            //Overige configuratieparameters
        });
});


});
