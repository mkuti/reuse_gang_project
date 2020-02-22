const cardCollapse = Array.from(document.getElementsByClassName("card-collapse"));

cardCollapse.forEach(card => {
    card.addEventListener("click", function(){
    card.classList.toggle('bg-othergreen')
    let collapsedContent = card.nextElementSibling;
    if(collapsedContent.style.display === "block"){
        collapsedContent.style.display = "none";
    } else collapsedContent.style.display = "block"
})
})