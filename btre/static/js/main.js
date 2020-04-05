const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);

// var messages = document.getElementById('message')
// for (var message in messages){
//     print(message)
//     setTimeout(function(){
//         $(message).fadeOut('slow')
//     }, 3000);
    
// }
