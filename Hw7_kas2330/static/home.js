// home.js
$(document).ready(function() {
    console.log("home.js is executing.");
    // Define data for popular items (You can modify this according to your data)
    var popularItems = [
        {id: 9, title: "PETLIBRO Automatic Feeder", image: "https://m.media-amazon.com/images/I/61xZGeIJgiL._AC_SY879_.jpg"},
        {id: 2, title: "Electric Lady Bug", image: "file:///Users/Kyleigh/Desktop/UI%20Design/Midterm/UI-Midterm/Hw7_kas2330/static/ladybug_med.jpeg"},
        {id: 6, title: "Cat Dancer Toy", image: "url_for('static', filename='cat_dancer_med.jpeg')"}
    ];

    // Function to handle click on popular item
    function handleItemClick(itemId) {
        console.log("Item clicked:", itemId);
        window.location.href = '/view/' + itemId; // Redirect to view page with item ID
    }

    // Loop through popular items data and append to the DOM
    var popularItemsContainer = $('#popular-items');
    $.each(popularItems, function(index, item) {
        var itemHtml = '<div class="col-md-4 mb-3">';
        itemHtml += '<div class="card item" style="cursor: pointer;" onclick="handleItemClick(' + item.id + ')">';
        itemHtml += '<img src="' + item.image + '" class="card-img-top" alt="' + item.title + '">';
        itemHtml += '<div class="card-body">';
        itemHtml += '<h5 class="card-title">' + item.title + '</h5>';
        itemHtml += '</div></div></div>';
        popularItemsContainer.append(itemHtml);
    });
});

