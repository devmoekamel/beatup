



// var beat = new Audio("beatup.mp3");
beat.currentTime=0;

$("#play").click(function(){

// beat.play();

$("#play").hide();
$("#pause").show();

});


$("#min").click(function(){

    beat.volume -= 0.1;

    
    });

$("#plus").click(function(){

        beat.volume += 0.1;
        
        
        });



$("#pause").click(function(){

            // beat.pause();
            
            $("#play").show();
            $("#pause").hide();
            
 });
            