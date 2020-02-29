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

selectCat.onchange = function () {
    cat = selectCat.value;

    
}