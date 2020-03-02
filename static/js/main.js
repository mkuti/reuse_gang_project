const cardCollapse = Array.from(document.getElementsByClassName("card-collapse"));
const selectCat = document.getElementById("search_category");

cardCollapse.forEach(card => {
    card.addEventListener("click", function(){
    let collapsedContent = card.nextElementSibling;
    if(collapsedContent.style.display === "block"){
        collapsedContent.style.display = "none";
    } else collapsedContent.style.display = "block"
})
})

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
        console.log(response)
        if (response.status !== 200) {
            console.log(`Response status was not 200: ${response.status}`);
            return;
        }
        response.json().then(function(data){
            console.log(data)
        })
    })
    .catch(err => console.log(err));
}