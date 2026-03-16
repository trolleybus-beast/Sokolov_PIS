$(document).ready(function(){
     $('.one-post').hover(function(event){
         $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.1'}, 300);
     }, function(event){
         $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
     });
     $('.header img').hover(function(){
        $(this).css('width', '338px');
     }, function(){
        $(this).css('width', '318px');
     });
});