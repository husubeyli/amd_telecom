const domain = document.getElementById('YOUR_ENV_VARIABLE').value


// keep this page category id
const categoryProduct = $('.category-pro')[0]
let theCategory = categoryProduct.getAttribute('for-filter')

// the seuences for min and max price 
// default empty
let min_max = ''
let min_max_arr = []
let min = ''
let max = ''

$(document).on('input', '#range', function() { // price range when changed keep values(min,max)
    $('#slider_value').html( $(this).val() );
    min_max = $(this).val()
    min_max_arr = min_max.split(';')

    min = min_max_arr[0]
    max = min_max_arr[1]

    getData()

});

function getData() { // filter product data return products
    // $(".ajaxLoader").hide();

    var _filterObj={};
    _filterObj['price_min'] = min
    _filterObj['price_max'] = max
    _filterObj['category'] = theCategory


    if($(".filter-item-checkbox")){
        $(".filter-item-checkbox").each(function(index,ele){
            _filterObj['price_min'] = min
            _filterObj['price_max'] = max
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');

            console.log(min);
            // if (min == ''){
            // }
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            })

            console.log(_filterObj, 'gelen datalar');

        });
    }
    // else{
    //     log
    // }
    console.log(_filterObj, 'yeni');

    $.ajax({
        url: `${domain}api/v1.0/filter-api-product/`,
        async: true,
        type : 'GET',
        data: _filterObj,
        dataType:'json',
        success:function(response){
            console.log(response, 'product data');
            let DOM = $('.prod-items')
            let products = ''
            if (response.length){  
                console.log('zero');

                for(let product of response){
                    // console.log(product, 'datalar');
                    var is_discount_logo= `<div class="lable-block"><span class="lable3" style="left:unset; right:7px">Endirim</span></div>`
                    var is_new_logo = `<div class="lable-block"><span class="lable3">Yeni</span></div>`

                    var mainSeconImage = `

                    ${ product.is_discount ? is_discount_logo : ''}
                    ${ product.is_new ? is_new_logo : ''}
                    
                    <div class="front">
                        <a href="${domain}product/${product.slug}/">
                        <img
                            src="${ product.products_images.length > 1 ? product.products_images[0].image : '' }"
                            class="img-fluid blur-up lazyload bg-img" alt="${product.title.toUpperCase()}">
                        </a>
                    </div>
                    <div class="back">
                        <a class="text-center" href="${domain}product/${product.slug}/">
                            <img
                                src="${ product.products_images.length > 1 ? product.products_images[1].image : '' }"
                                class="img-fluid blur-up lazyload bg-img" alt="${product.title.toUpperCase()}">
                            </a>
                    </div>
                    `

                    var secondImage = `
                    <div class="front">
                        <a href="${domain}product/${product.slug}/">
                        <img
                            src="$${ product.products_images.length > 1 ? product.products_images[1].image : '' }"
                            class="img-fluid blur-up lazyload bg-img text-center" alt="${product.title.toUpperCase()}">
                        </a>
                    </div>
                    `
               
                    var price_no_disc = `
                    <h4 class="">${product.priced} 
                        <svg style='width: 1em; height: 1em;' data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 37.41 32.09">
                            <defs>
                                <style>
                                    .cls-1<!-- -->{<!-- -->fill:#2b2929<!-- -->}
                                </style>
                            </defs>
                            <title>manat</title>
                            <path class="cls-1" d="M312.33 418.63q-4.54-9.25-13.63-9.89l-.11-3.83-2.26.92-.14 2.9q-8.91.56-13.57 9.73-3.89 7.71-3.89 18.54h5.51c.2-16 5.47-24.67 11.88-26l-.7 23.66 4-1.37-.65-22.41c6.43.75 11.89 9.45 12 26.1h5.41q-.09-10.85-3.81-18.37z" transform="translate(-278.73 -404.91)" id="Layer_1-2"></path>
                        </svg>
                    </h4>
                    `
                    var price_discounted = `
                    <h4 class="d-flex">${product.priced} 
                        <svg style='width: 1em; height: 1em;' data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 37.41 32.09">
                            <defs>
                                <style>
                                    .cls-1<!-- -->{<!-- -->fill:#2b2929<!-- -->}
                                </style>
                            </defs>
                            <title>manat</title>
                            <path class="cls-1" d="M312.33 418.63q-4.54-9.25-13.63-9.89l-.11-3.83-2.26.92-.14 2.9q-8.91.56-13.57 9.73-3.89 7.71-3.89 18.54h5.51c.2-16 5.47-24.67 11.88-26l-.7 23.66 4-1.37-.65-22.41c6.43.75 11.89 9.45 12 26.1h5.41q-.09-10.85-3.81-18.37z" transform="translate(-278.73 -404.91)" id="Layer_1-2"></path>
                        </svg>
                    
                    <del class="ml-2">
                        <h4 class=""></h4>${product.price} 
                        <svg style='width: 1em; height: 1em;' data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 37.41 32.09">
                            <defs>
                                <style>
                                    .cls-1<!-- -->{<!-- -->fill:#2b2929<!-- -->}
                                </style>
                            </defs>
                            <title>manat</title>
                            <path class="cls-1" d="M312.33 418.63q-4.54-9.25-13.63-9.89l-.11-3.83-2.26.92-.14 2.9q-8.91.56-13.57 9.73-3.89 7.71-3.89 18.54h5.51c.2-16 5.47-24.67 11.88-26l-.7 23.66 4-1.37-.65-22.41c6.43.75 11.89 9.45 12 26.1h5.41q-.09-10.85-3.81-18.37z" transform="translate(-278.73 -404.91)" id="Layer_1-2"></path>
                        </svg>
                        </h4>
                    </del> 
                    </h4>
                    `

                    // nomrelerin filteri ucun
                    if(product.operator_code) {

                        products += `
                            <div class="col-xl-4 col-sm-6 col-md-4 col-grid-box category-pro" style="margin-top: 20px;">
                            
                            <div class="numberCard">
                                <div class="numberCard__container">

                                    <div class="numberCard__container__head">
                                        
                                        <ul>
                                            <li>
                                                <svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" style="cursor:pointer">
                                                    <path d="M15.55 13c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.37-.66-.11-1.48-.87-1.48H5.21l-.94-2H1v2h2l3.6 7.59-1.35 2.44C4.52 15.37 5.48 17 7 17h12v-2H7l1.1-2h7.45zM6.16 6h12.15l-2.76 5H8.53L6.16 6zM7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zm10 0c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"></path>
                                                </svg>
                                            </li>
                                        </ul>

                                    </div>

                                    <div class="numberCard__container__body">
                                        <div class="numberCard__container__body-img">
                                            <img src="${product.product_marka[0].image}" alt="" style="height: 72px; width: 72px;">
                                        </div>
                                        <div class="numberCard__container__body-number">
                                            <p class="m-0 text-dark">(<!-- -->${product.operator_code}<!-- -->) <!-- -->${product.title.toUpperCase()}</p>
                                        </div>
                                    </div>

                                    <div class="numberCard__container__footer">
                                        <div class="numberCard__container__footer-price">
                                            <span class="text-dark">
                                                ${product.price}
                                                <svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 37.41 32.09">
                                                    <defs>
                                                        <style>
                                                            .cls-1<!-- -->{<!-- -->fill:#2b2929<!-- -->}
                                                        </style>
                                                    </defs>
                                                    <title>manat</title>
                                                    <path class="cls-1" d="M312.33 418.63q-4.54-9.25-13.63-9.89l-.11-3.83-2.26.92-.14 2.9q-8.91.56-13.57 9.73-3.89 7.71-3.89 18.54h5.51c.2-16 5.47-24.67 11.88-26l-.7 23.66 4-1.37-.65-22.41c6.43.75 11.89 9.45 12 26.1h5.41q-.09-10.85-3.81-18.37z" transform="translate(-278.73 -404.91)" id="Layer_1-2"></path>
                                                </svg>
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                        `
                    }
                    else {
                        // productun rengi ucun
                        products += `
                                <div class="col-xl-3 col-sm-6 col-md-4 col-grid-box category-pro">
                                <div class="product-box">
                                    <div class="img-wrapper">
                                        ${ product.products_images.length > 1 ? mainSeconImage : secondImage }
                                        
                                    </div>
                                    <div class="product-detail text-center">
                                        <div>
                                            <a href="product-page(no-sidebar).html">
                                                <h6>${product.product_marka[0].title ? product.product_marka[0].title.toUpperCase() : '' } ${product.title.toUpperCase()} ${ product.ram ? product.ram + 'GB/': ''} ${ product.internal_storage ? product.internal_storage + 'GB' : '' } ${product.color_title ? product.color_title.toUpperCase() : ''}</h6>
                                            </a>
                                            <p>${product.description}
                                            </p>
                                            ${ product.is_discount ? price_discounted : price_no_disc }
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `
                        
                    }
                    DOM.html(products)
                    mainSeconImage = ''
                    secondImage = ''
                    price_no_disc= ''
                    price_discounted = ''
                    is_discount_logo = ''
                    is_new_logo = ''
                    

                }  

            }
            else {
                DOM.html('')
            } 
            $(function() {
                $(".product-load-more .col-grid-box").slice(0, 12).show();
                $(".loadMore").on('click', function(e) {
                    e.preventDefault();
                    $(".product-load-more .col-grid-box:hidden").slice(0, 4).slideDown();
                    if ($(".product-load-more .col-grid-box:hidden").length === 0) {
                        console.log(`$(".loadMore").css('display', 'none')`);
                        $(".loadMore").css('display', 'none')
                    }

                });
                if ($(".product-load-more .col-grid-box:hidden").length > 0) {
                    console.log(`$(".loadMore").css('display', 'block')`);
                    $(".loadMore").css('display', 'block')
                }
            });
 

            _filterObj = {}
        },
        error: function(response){
            console.log(response, 'error');
        }

    })
    // console.log(_filterObj)


}

