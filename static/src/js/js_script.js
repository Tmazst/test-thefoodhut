

// Form Submittion
// $(document).ready(function(){

//     $('.form-submit').submit(function(event){
//         event.preventDefault();

//         var formData = $(this).serialize();

//         $.ajax({
//             type:'POST',
//             url:'/vac_signup',
//             data:formData,

//             success: function(response){
//                 if(response== 'success'){
//                     alert('Form Submitted Successfully!');
//                 }else{;
//                     alert('Form Submittion failed, Please check fields with error below');
//                 }
//             },
//             error: function(){
//                 alert('Error Occurred while submitting the form');
//             }
            
//         });
//     });
// });



function sideNavFunc(event){
    // var popScrnLogo = document.getElementById("updates");
    // popScrnLogo.classList.toggle("show-popup");
    console.log("Side Nav");
    let sideNavBg = document.querySelector('#side-navig-bg');
    let sideNavCont = document.querySelector("#side-navig-cont");
    // document.querySelector("#commentField").value = "";
    sideNavBg.classList.toggle("show-popup");
    sideNavCont.classList.toggle("show-menu");
    };

function closeSideNavFunc(){
    // var popScrnLogo = document.getElementById("updates");
    // popScrnLogo.classList.toggle("show-popup");
    console.log("Side Nav");
    let sideNavBg = document.querySelector('#side-navig-bg');
    let sideNavCont = document.querySelector("#side-navig-cont");
    // document.querySelector("#commentField").value = "";
    sideNavBg.classList.remove("show-popup");
    sideNavCont.classList.remove("show-menu");

    };

document.addEventListener("DOMContentLoaded", function () {
    var usr = document.querySelector('.nav-link1');
    var trimmed = usr.innerHTML.substring(0,5);
    usr.innerHTML = trimmed+"...";

    
});

function showHideFbtns(){
    let fbtns = document.querySelector('.facilities-btns');
    let contHandle = document.querySelector('#cont-handle');
    fbtns.classList.toggle('show-it');
    contHandle.classList.toggle('rotate-45');
};


function hideShowFbtns(){
    let fbtns = document.querySelector('.food-ads-cont');
    let contHandle = document.querySelector('#cont-handle-1');
    fbtns.classList.toggle('hide');
    contHandle.classList.toggle('derotate');
};




// quoteBtns.forEach(function(btn){
function popMenuItem(id){

    // var popScrnLogo = document.getElementById("updates");
    // popScrnLogo.classList.toggle("show-popup");
    console.log("Pop-up on Chats");
    let popCont = document.querySelector('#pop_menucont_'+id);
    let popup = document.querySelector("#popup_menu_"+id);
    // document.querySelector("#commentField").value = "";
    popCont.classList.toggle("show-popup");
    popup.classList.toggle("show-popup");
    
};

function closeMenuPop(id){
    let popup = document.querySelector("#pop_menucont_"+id);
    let popCont = document.querySelector('#popup_menu_'+id);
    // document.querySelector("#comm/entField").value = "";
    popup.classList.remove("show-popup");
    popCont.classList.remove("show-popup");
};





const resizeObserver = new ResizeObserver(entries =>{

    for(let entry of entries){
        console.log('Viewport width(ResizeObserver):', window.innerWidth);
        if(window.innerWidth <= 700){
            var usr = document.querySelector('.nav-link1');
            var trimmed = usr.innerHTML.substring(0,5);
            usr.innerHTML = trimmed+"...";
            console.log('Smartphone View');
        }
    }

});

resizeObserver.observe(document.body);


let slideIndex = 0;
const slides = document.getElementsByClassName("images-slides");

function showSlides() {
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
        slides[i].classList.remove('show-img-slide');
    }
    slideIndex = (slideIndex + 1) % slides.length; // Go to the next slide
    slides[slideIndex].classList.add("show-img-slide");
    setTimeout(showSlides, 6000); // Change image every 3 seconds
}

// Start the slideshow
showSlides();


//Not working at the moment
function changeSlide(n) {
    slideIndex = (slideIndex + n + slides.length) % slides.length; // Calculate new index
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        // slides[i].classList.remove('show-img-slide');
    }
    // slides[slideIndex].classList.add("show-img-slide"); // Show the current slide
}



let currTouch = 0;
let initTouchX,endTouchX;

// var slider = document.querySelector('.slider');
// slider.addEventListener('touchstart', function(event){
//     initTouchX = event.touches[0].clientX;
//     slider.style.animationDuration='0s';
//     // let slideShow = getElementsByClassName();
// });

// slider.addEventListener('touchmove', function(event){
//     if (!initTouchX) return;

//     const touch = event.touches[0];
//     const diffX = touch.clientX - startX;

//     if (Math.abs(diffX) > 50){
//         event.preventDefault();

//         if (diffX > 0){
//             slider.scrollBy({
//                 left:-diffX,
//                 behavior: 'smooth'
//             });
//         }else{
//             // Swiped left - scroll right
//             slider.scrollBy({
//                 left: diffX,
//                 behavior: 'smooth'
//             });
//         }
//          // Reset startX to prevent repeated scrolls
//          initTouchX = touch.clientX;       
//     }
// });

// container.addEventListener('touchend', function() {
//     initTouchX = null;
//     // Resume sliding
//     slider.style.animationDelay='3s';
//     slider.style.animationDuration='1s';
// });


// Image Viewer
$("#images img").click(function(){
    $("#full-image").attr("src", $(this).attr("src"));
    $('#image-viewer').show();
  });
  
  $("#image-viewer .close").click(function(){
    $('#image-viewer').hide();
  });

// Image Viewer
$("#tel").click(function(){
    $("#full-image").attr("src", $(this).attr("src"));
    $('#image-viewer').show();
  });
  
  $("#image-viewer .close").click(function(){
    $('#image-viewer').hide();
  });


//Pop up Form
function ProcessFrom(){
    let submtBtn = document.createElement('input');
    submtBtn.type = 'submit';
    let par = document.querySelector('form');
    $(document).ready(function(){
            par.appendChild(submtBtn);
        $('.pop-btns').click(function(){
            console.log('Clicked: ',$('form').serializeArray());
            $('submit').submit()
        })
    })
}

const divs = document.querySelectorAll(".hidden");
var observer = new IntersectionObserver(entries => {
    entries.forEach(entry =>{
        //console.log(entry.target)
        entry.target.classList.toggle("show", entry.isIntersecting)
        if (entry.isIntersecting) observer.unobserve(entry.target)
        })
    },
    {
    threshold:0,
    //rootMargin:"0px"
    }
);

divs.forEach(div =>{
    observer.observe(div);
});

// let timer;

// function handleScroll(){
//     console.log("Window Scrolled")
//     post = document.querySelector('post1');
//     post.classList.toggle('shuffle-btn');
//     clearTimerout(timer);

//     timer = setTimeout(function(){
//         console.log("Stopped Scrolling")
//         // Add code here
//     },2000);
// }

// window.addEventListener('scroll', function(){
//     console.log("Window Scroll");
// });

// Menu 
function openMenu(){
    const otherNav = document.querySelector(".other-nav");
    const navlinks = document.querySelectorAll(".nav-link");
    console.log("Test Menu");
    otherNav.classList.toggle('menu-appear');
    burger.classList.toggle("toggle");
}

// burger.addEventListener("click", () => {

//     console.log("Test1");
//     otherNav.classList.toggle('menu-appear');
//     burger.classList.toggle("toggle");

//  });

function openNavBar(){
    var navActionIcon = document.querySelector('.nav-action-icon');
    navActionIcon.classList.toggle('toggle-side-drw');
};

// var handle = document.querySelector('.handle');

// handle.addEventListener('click', ()=>{
//     var navActionIcon = document.querySelector('.nav-action-icon');
//     console.log('Handle Clicked');
//     navActionIcon.classList.toggle('toggle-side-drw');
// });

var btn = document.querySelector('#telephone');

btn.addEventListener("click",() => {

    console.log("Event Clicked")
    // let popUp = document.querySelector("#updates-popup");
    // let popCont = document.querySelector("#updates-cont");

    // popCont.classList.toggle("show-popup");
    // popUp.classList.toggle("show-popup");
    
});

// quoteBtns.forEach(function(btn){
function updatesPopup(id){
        // var popScrnLogo = document.getElementById("updates");
        // popScrnLogo.classList.toggle("show-popup");
     let popup = document.querySelector("#updates_popup-"+id);
     let popCont = document.querySelector('#updates-cont-'+id);
     popup.classList.toggle("show-popup");
     popCont.classList.toggle("show-popup");

     popCont.classList.toggle("updates-cont");
 // })
 //         }else if(event.target.id === 'poster_quote_btn'){
 //             var popScrnPoster = document.getElementById("poster_quote");
 // //            console.log("Contains Poster Quote: ")
 //             popScrnPoster.classList.toggle("show-popup");
 //             popup.classList.toggle("show-popup");
 //         }else if(event.target.id === 'flyer_quote_btn'){
 //             var popScrnPoster = document.getElementById("flyer_quote");
 //             console.log("Contains Poster Quote: ")
 //             popScrnPoster.classList.toggle("show-popup");
 //             popup.classList.toggle("show-popup");
 //             }
 //         })
 };

// quoteBtns.forEach(function(btn){
function popUp(id){
    // var popScrnLogo = document.getElementById("updates");
    // popScrnLogo.classList.toggle("show-popup");
    console.log("Pop-up");
    let popCont = document.querySelector('#pop_cont_'+id);
    let popup = document.querySelector("#popup_"+id);

    popCont.classList.toggle("show-popup");
    popup.classList.toggle("show-popup");

    // Assuming you want to remove the query parameter from the URL
    // // Get the current URL without the query parameter
    // var newUrl = window.location.protocol + '//' + window.location.host + window.location.pathname;

    // // Use replaceState to update the URL without the query parameter
    // window.history.replaceState({path: newUrl}, '', newUrl);
    
};

// quoteBtns.forEach(function(btn){
function popChatUp(id){
    // var popScrnLogo = document.getElementById("updates");
    // popScrnLogo.classList.toggle("show-popup");
    console.log("Pop-up on Chats");
    let popCont = document.querySelector('#pop_chatscont_'+id);
    let popup = document.querySelector("#popup_chats_"+id);
    document.querySelector("#commentField").value = "";
    popCont.classList.toggle("show-popup");
    popup.classList.toggle("show-popup");

    // Assuming you want to remove the query parameter from the URL
    // // Get the current URL without the query parameter
    // var newUrl = window.location.protocol + '//' + window.location.host + window.location.pathname;

    // // Use replaceState to update the URL without the query parameter
    // window.history.replaceState({path: newUrl}, '', newUrl);
    
};


function closeChatsPopup(id){
    let popup = document.querySelector("#popup_chats_"+id);
    let popCont = document.querySelector('#pop_chatscont_'+id);
    document.querySelector("#commentField").value = "";
    popup.classList.remove("show-popup");
    popCont.classList.remove("show-popup");
};

function closePopup(id){
    let popup = document.querySelector("#popup_"+id);
    let popCont = document.querySelector('#pop_cont_'+id);
    popup.classList.remove("show-popup");
    popCont.classList.remove("show-popup");
};

function closePopup1(id){
    let popup = document.querySelector("#popup1_"+id);
    let popCont = document.querySelector('#pop_cont1_'+id);
    popup.classList.remove("show-popup");
    popCont.classList.remove("show-popup");
};


function closeUpdatesPop(id){
    let popup = document.querySelector("#updates-popup-"+id);
    let popCont = document.querySelector('#updates-cont-'+id);
    popup.classList.remove("show-popup");
    popCont.classList.remove("show-popup");
};

var contact = null;

var yesBtn = document.querySelector("#yes-conctact");

function openContact(){

    window.location.href = contact;

};

function openPopContacts(assign_cont,id){
    // var popScrnLogo = document.getElementById("updates");
    // popScrnLogo.classList.toggle("show-popup");
    // const newUrl = '/enquiry_posts?id=' + userId;
    // window.history.pushState({ path: newUrl }, '', newUrl);

    console.log("Pop-up1",contact);
    contact = assign_cont;
    console.log("Pop-up2",contact);

    let popCont = document.querySelector('#pop_cont1_'+id);
    let popup = document.querySelector("#popup1_"+id);

    popCont.classList.toggle("show-popup");
    popup.classList.toggle("show-popup");

    // Assuming you want to remove the query parameter from the URL
    // Get the current URL without the query parameter
    // var newUrl = window.location.protocol + '//' + window.location.host + window.location.pathname;

    // // Use replaceState to update the URL without the query parameter
    // window.history.replaceState({path: newUrl}, '', newUrl);
};

const listIcon = document.querySelector("#list");
const blocksIcon = document.querySelector("#blocks");

listIcon.addEventListener("click", function(){

    window.location.href = "/?icon=listview";
    // listIcon.classList.add('active') ;

});

blocksIcon.addEventListener("click", function(){

    window.location.href = "/?icon=blockview";
    console.log("Blocks Icon CLicked");

});

