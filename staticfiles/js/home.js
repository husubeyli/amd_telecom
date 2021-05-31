console.log('home.js -->');
// function changeDisplaySearchBtn() {

    let searchInput = document.querySelector('.mobile-search--body')
    let inputJqWidth = $('.mobile-search--body')
    let inputVal = $('#search-filter-value')
    let responseArea = document.getElementById('search-filter-body');
    let responseJqArea = $('#search-filter-body')
    let searchBtnIcon = document.getElementById('search-btn-icon')

    let witdInput = getComputedStyle(searchInput)
    let widthStyle = witdInput.width
    let width = parseInt(widthStyle.split('p')[0])

    if (width == 36) {
        inputVal.css('background-color', 'rgb(45, 42, 37)')
    }
    else {
        inputVal.css('background-color', 'white')
    }


    $(window).resize(function(e) { // 991px den yuxari oldugu zaman input hissesi acilir
        /* Do shit */
        console.log(e.target.innerWidth);
        if (e.target.innerWidth > 991) {
            inputVal.css('background-color', '#fff')
            // responseJqArea.css('display', 'block')
            if (inputVal.val().length != 0) {
                responseJqArea.css('display', 'block')
            }
            else {
                responseJqArea.css('display', 'none')
            }
        }
        else {
            responseJqArea.css('display', 'none')
            inputVal.css('background-color', '#2d2a25')
            // inputVal.css('border', '0')
            // inputVal.css('background-color', '')
            inputVal.val('')
        }
    });



    // SEARCH INPUTU ACIQ OLDUQDA BODY DE IF SERTINDEN BASQA HER HANSI BIT EVENT HADIDESI OLDUGU ZAMAN BAGLANSIN DEYE
    document.querySelector("body").addEventListener("click", function(e){
        
        if (e.target.getAttribute("class") == 'data-title' || e.target.getAttribute("class") == 'image-attr' || e.target.getAttribute('class') == 'mobile-search--body--input'){
            responseJqArea.css('display', 'block')
        }
        else {
            responseJqArea.css('display', 'none')
        }
    })

function changeDisplay(widthSearch) { // for resize search body
    
    inputVal.toggleClass('bg-white')
    inputJqWidth.toggleClass('w-200')

    if (widthSearch == 36) {
        responseArea.classList.remove('d-none')
        responseArea.classList.remove('d-block')

        searchBtnIcon.classList.add('ti-close')
        searchBtnIcon.classList.remove('ti-search')
        searchBtnIcon.classList.remove('text-white')
        searchBtnIcon.classList.add('text-dark')

    }
    else {
        // searchInput.classList.remove('w-200')
        responseArea.classList.add('d-none')
        responseArea.classList.remove('d-block')

        searchBtnIcon.classList.remove('ti-close')
        searchBtnIcon.classList.add('ti-search')
        searchBtnIcon.classList.remove('text-dark')
        searchBtnIcon.classList.add('text-white')

        inputVal.val('')
    }
}
// changeDisplay(width)
// }

searchBtnIcon.addEventListener('click', (e)=>{
    console.log('salam');
    // e.preventDefault()
    let widthStyle = witdInput.width
    let width = parseInt(widthStyle.split('p')[0])

    changeDisplay(width)
})



// changeDisplaySearchBtn()