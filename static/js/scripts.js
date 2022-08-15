window.addEventListener('scroll', function () {
    let navbar = document.querySelector("nav");
    let nav_bg = document.querySelector("#nav_bg");
    let serach_text = document.querySelector("#search_text");
    let nav_cart_btn = document.querySelector("#nav_cart_btn");
    let nav_cart_badge = document.querySelector("#nav_cart_badge");
    let home_link = document.querySelector("#home_link");
    let tracking_link = document.querySelector("#tracking_link");
    //let about_link = document.querySelector("#about_link");
    let shop_link = document.querySelector(".shop_linked");
    let account_link = document.querySelector(".account_linked");
    let login_link = document.querySelector("#login_link");
    let singUP_link = document.querySelector("#singUP_link");
    let manu_bar_color = document.querySelector("#manu_bar_color");

    if (window.pageYOffset > 0) {
        navbar.classList.add('sticky');
        nav_bg.classList.remove('bg_black');
        serach_text.classList.remove('search_text');
        serach_text.classList.remove('text-white');
        nav_cart_btn.classList.remove('nav_cart_btn');
        nav_cart_badge.classList.remove('nav_cart_badge');
        home_link.classList.add('home_link');
        tracking_link.classList.add('tracking_link');
        //about_link.classList.add('about_link');
        shop_link.classList.add('shop_link');
        account_link.classList.add('shop_link');
        login_link.classList.add('login_link');
        singUP_link.classList.add('singUP_link');
        manu_bar_color.classList.add('manu_bar_color');


    } else {
        navbar.classList.remove('sticky');
        nav_bg.classList.add('bg_black');
        serach_text.classList.add('search_text');
        nav_cart_btn.classList.add('nav_cart_btn');
        nav_cart_badge.classList.add('nav_cart_badge');
        home_link.classList.remove('home_link');
        tracking_link.classList.remove('tracking_link');
        //about_link.classList.remove('about_link');
        shop_link.classList.remove('shop_link');
        account_link.classList.remove('shop_link');
        login_link.classList.remove('login_link');
        singUP_link.classList.remove('singUP_link');
        manu_bar_color.classList.remove('manu_bar_color');
        serach_text.classList.add('text-white');
        
        
    }
});



//login page______________________
(function () {
    'use strict'

    var forms = document.querySelectorAll('.needs-validation')

    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }
                form.classList.add('was-validated')
            }, false)
        })
})()


//quick view descriptions_______________________

$(function () {
    $('.product_info_btn').click(function(){
        var value = this.innerHTML;
        if(value=="Description"){
          $(".descriptions").show('slow');
          $(".more_info").hide('slow');
          $(".reviews").hide('slow');
        }else if(value=="More Info"){
          $(".descriptions").hide('slow');
          $(".more_info").show('slow');
          $(".reviews").hide('slow');
        }else if(value=="Reviews"){
          $(".descriptions").hide('slow');
          $(".more_info").hide('slow');
          $(".reviews").show('slow');
        }
    })
  }); 

//order list
$(function () {
    $('.AllOrderBtn').click(function(){
        var ListCategory = this.innerHTML;
        if(ListCategory=="All"){
            $(".AllOrderList").show('slow');
            $(".DeliverdOrderList").hide('slow');
            $(".CancelledOrderList").hide('slow');
        }else if(ListCategory=="Delivered"){
            $(".AllOrderList").hide('slow');
            $(".DeliverdOrderList").show('slow');
            $(".CancelledOrderList").hide('slow');
        }else if(ListCategory=="Cancelled"){
            $(".AllOrderList").hide('slow');
            $(".DeliverdOrderList").hide('slow');
            $(".CancelledOrderList").show('slow');
        }
    })
  }); 


//change store banner
$(function () {
    $('.banner_form_open_btn').click(function(){
        $(".store_banner_form").stop().toggle('slow');
    })
  }); 

//banner image live show
function previewImage(event){
    const showImage = document.getElementById("previewImage");
    showImage.src = URL.createObjectURL(event.target.files[0]);
}






