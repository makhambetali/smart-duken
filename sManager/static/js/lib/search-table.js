const input = document.getElementById("searchInput");
document.getElementById("searchInput").addEventListener("input", function() {   
    var filter, table, tr, td, i, txtValue;
    
    filter = input.value.toUpperCase();
    table = document.getElementById("search-table");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0]; // Assuming search is based on the first column
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
});
