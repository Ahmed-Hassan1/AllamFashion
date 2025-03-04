var updateBtns = document.getElementsByClassName('update-cart');


for (i=0; i<updateBtns.length; i++)
{
    updateBtns[i].addEventListener('click', function(){
        var prodID = this.dataset.product;
        var action = this.dataset.action;

        const sizeOption = document.getElementById("sizeOption");
        if(sizeOption)
        {
            addCookieItem(prodID,action,1,sizeOption.value);
        }
        else
        {
            addCookieItem(prodID,action,1,"");
        }
        
    })
}

function addCookieItem(prodID,action,prodQuant,size)
{
    if(action == 'add'){
        if(cart[prodID] == undefined)
        {
            cart[prodID] = {'quantity':parseInt(prodQuant),'size':size};
        }
        else
        {
            cart[prodID]['quantity'] += parseInt(prodQuant);
        }
    }

    if(action == 'remove'){
        delete cart[prodID];
        // cart[prodID]['quantity'] = 0;

        // if (cart[prodID]['quantity']<=0)
        // {
        //     console.log('deleted item')
        //     delete cart[prodID];
        // }
        
    }
    console.log(cart)

    document.cookie = 'cart='+ JSON.stringify(cart) + ";domian=;path=/"

    setTimeout(function(){location.reload()},1000)
    
}

function updateUserOrder(prodID,action,prodQuant)
{

    url = '/accounts/update-item/'
    fetch(url, {
        method: 'post',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFTOKEN':csrftoken,
        },
        body:JSON.stringify({
            'prodID': prodID,
            'action': action,
            'prodQuant':prodQuant
        })
    }).then((response)=>{
        return response.json()
    }).then((data)=>{
        setTimeout(function(){location.reload()},1000)
    });
}






// Quant in product page
$(document).ready(function(){
    $('#qty_input').prop('disabled', true);
    $('#plus-btn').click(function(){
    	$('#qty_input').val(parseInt($('#qty_input').val()) + 1 );
    	    });
        $('#minus-btn').click(function(){
    	$('#qty_input').val(parseInt($('#qty_input').val()) - 1 );
    	if ($('#qty_input').val() == 0) {
			$('#qty_input').val(1);
		}

    	    });
 });