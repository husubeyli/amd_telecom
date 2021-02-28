const domain = `http://localhost:8000/`
console.log('salam');
const categoryProduct = $('.category-pro')[0]
let theCategory = categoryProduct.getAttribute('for-filter')
console.log(theCategory);
function getData() {
    $(".ajaxLoader").hide();

    // let value = $getvalues.on("click", updateInputs);
    // console.log(value);
        
    
    // var category = $('#categoryId').data('category')
    console.log($(this))
    var _filterObj={};
    $(".filter-item-checkbox").each(function(index,ele){
        var _filterVal=$(this).val();
        var _filterKey=$(this).data('filter');
        console.log(_filterKey);
        _filterObj['category'] = theCategory
        _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
            return el.value;
        });
        // if($('.filter-item-checkbox').attr = 'range') {
        //     let value = $getvalues.on("click", updateInputs);
        //     console.log(value);
        // }
    });


    function getProImage(id){
        let image	
        $.ajax({
            url: `${domain}api/v1.0/filter-api-product-images/`,
            // data: _filterObj,
            async: false,
            global: false,
            dataType: 'json',
            
            success:function(res){
                // console.log(res);
                for(j of res){
                    console.log(j);
                    // console.log(j.id);
                    if (j.id == id ) {
                        image = j.image
                    }
                }
            },
            error: function(res){
                console.log(res, 'error');
            }

        })
        return image

    }

    $.ajax({
        url: `${domain}api/v1.0/filter-api-product/`,
        type : 'GET',
        data:_filterObj,
        dataType:'json',
        success:function(response){
            let DOM = $('.prod-items')
            let products = ''
            for(let product of response){
                
                products += `
                        <div class="col-xl-3 col-6 col-grid-box">
                        <div class="product-box">
                            <div class="img-wrapper">
                                <div class="front">
                                        <a href="http://localhost:8000/product/${product.slug}/">
                                        <img
                                            src="${getProImage(product.images[1])}"
                                            class="img-fluid blur-up lazyload bg-img" alt="">
                                        </a>
                                </div>
                                <div class="back">
                                    <a href="http://localhost:8000/product/${product.slug}/">
                                        <img
                                            src="${getProImage(product.images[0])}"
                                            class="img-fluid blur-up lazyload bg-img" alt="${product.title}">
                                        </a>
                                </div>
                                <div class="cart-info cart-wrap">
                                    <button data-toggle="modal" data-target="#addtocart" title="Add to cart"><i
                                            class="ti-shopping-cart"></i></button> <a href="javascript:void(0)" title="Add to Wishlist"><i
                                            class="ti-heart" aria-hidden="true"></i></a> <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View"><i
                                            class="ti-search" aria-hidden="true"></i></a> <a href="compare.html" title="Compare"><i
                                            class="ti-reload" aria-hidden="true"></i></a>
                                </div>
                            </div>
                            <div class="product-detail">
                                <div>
                                    <a href="product-page(no-sidebar).html">
                                        <h6>${product.title}</h6>
                                    </a>
                                    <p>${product.description}
                                    </p>
                                    <h4>${product.price} AZN</h4>
                                    <ul class="color-variant">
                                        <li class="bg-light0" style="background-color: ${product.color_code} !important;"></li>
                                        <!-- <li class="bg-light1"></li>
                                        <li class="bg-light2"></li> -->
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                `

                DOM.html(products)

            }

            _filterObj = {}
        },
        error: function(response){
            console.log(response, 'error');
        }

    })
    console.log(_filterObj)


}

