/*
=================================
           SEARCH BAR
=================================
*/
    const selectCat = document.getElementById("search_category");
    const card = document.getElementById("card_item")

selectCat.onchange = function() {
    cat = selectCat.value;
            
    fetch(`${window.origin}/items/filter`, {
        method: "POST",
        credentials: 'include',
        body: JSON.stringify(cat),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    .then(function(response) {
        response.json().then(function(data){
            loopItems(data)
        })
    })
    .catch(err => console.log(err));
}


function loopItems(data) {
    let cardContent = '';
    data.forEach(item => {
        /**
 * Adding $oid behind _id to remove id hex number from object and construct url for editing item
 */
        item_id = item._id.$oid
        cardContent += injectCard(item)
    })
    $("#card_item").html(cardContent);
    collapsingCards()
}

// found solution to inject if statement within template literals: https://stackoverflow.com/questions/44488434/inserting-if-statement-inside-es6-template-literal/55913826#55913826

function injectCard(item) {
    cardHtml = `
            <div class="col-12 col-sm-6 col-lg-4">
			<div class="card my-2 text-center">
				<div class="card-body p-0">
                    <div class="row my-3">
                        <div class="col-10 px-0">
                            <h3 class="card-title text-uppercase mb-4">${item.item_name}</h3>
                        </div>
                        <div class="col-2 mt-2">
                            <h5 class="card-subtitle mb-4">
                            ${(() => {
                                if (item.item_category == 'Outdoor') {
                                    return `<i class="fas fa-cloud-sun"></i>`;
                                } else if (item.item_category == 'Kids') {
                                    return `<i class="fas fa-child"></i>`;
                                } else if (item.item_category == 'Household') {
                                    return `<i class="fas fa-home"></i>`;
                                } else {return `<i class="fas fa-random"></i>`}
                                })()}
                            </h5>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col">
                            <a type='button' class='card-collapse light_text px-0 mx-0'>
                                <h6>Find more info about this item...<i class="pl-2 fas fa-chevron-down"></i></h6>
                            </a>
                            <p class="card-text collapsed-content text-left px-0 mx-0 lgreen_text">${item.item_description}</p>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col">
                            <h6>Can be collected in ${item.item_location}</h6>
                        </div>
                    </div>
                    ${(() => {
                        if (item.item_img){
                            return `<div class="card-img-contain text-left mb-3">
                                        <img src="${item.item_img}" class="card-img-top card-img" alt="Item Image">
                                    </div>`
                        }
                    })()}
                    <div class="row my-3">
                        <div class="col-12">>
                            <a href="mailto:${item.item_contact}" class="card-link">Contact</a>
                            <span class="card-subtitle mt-0">${item.username}</span>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col-12">
                        <!--url_for('python_function_name', any other function argument)-->
                            <a href="/items/update/${item_id}" class="btn bg-darkgreen light_text">Edit</a>
                        </div>
                    </div>
				</div>
			</div>
		</div>
        `;
        return cardHtml;
}



/*
=================================
   COLLAPSING ITEM DESCRIPTION
=================================
*/

function collapsingCards(){
    let cardCollapse = Array.from(document.getElementsByClassName("card-collapse"));

cardCollapse.forEach(card => {
    card.addEventListener("click", function(){
    let collapsedContent = card.nextElementSibling;
    if(collapsedContent.style.display === "block"){
        collapsedContent.style.display = "none";
    } else collapsedContent.style.display = "block"
})
})
}

collapsingCards()


/*
=================================
    LOGO DISAPPEAR ON SCROLL
=================================
*/

// courtesy of Simen Daehlin from my first milestone, via https://codepen.io/Eventyret/pen/RXBNaJ
$(window).scroll(function(){
    $("#logo-img").css("opacity", 1 - $(window).scrollTop() / 50)
})

