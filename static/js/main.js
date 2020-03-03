/*
=================================
   COLLAPSING ITEM DESCRIPTION
=================================
*/

const cardCollapse = Array.from(document.getElementsByClassName("card-collapse"));

cardCollapse.forEach(card => {
    card.addEventListener("click", function(){
    let collapsedContent = card.nextElementSibling;
    if(collapsedContent.style.display === "block"){
        collapsedContent.style.display = "none";
    } else collapsedContent.style.display = "block"
})
})

/*
=================================
           SEARCH BAR
=================================
*/

const selectCat = document.getElementById("search_category");


selectCat.onchange = function() {
    cat = selectCat.value;
    alert(cat)

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
            data.forEach(item => {
                console.log(item);
            })
        })
    })
    .catch(err => console.log(err));
}