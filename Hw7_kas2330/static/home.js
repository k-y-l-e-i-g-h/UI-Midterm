// home.js
$(document).ready(function() {
    console.log("home.js is executing.");
    // Define data for popular items (You can modify this according to your data)
    var popularItems = [
        {id: 9, title: "PETLIBRO Automatic Feeder", image: "https://m.media-amazon.com/images/I/61xZGeIJgiL._AC_SY879_.jpg"},
        {id: 2, title: "Electric Lady Bug", image: "https://m.media-amazon.com/images/I/31A4NAQiJEL._AC_SX679_.jpg"},
        {id: 6, title: "Cat Dancer Toy", image: "https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1200,height=672,format=auto/https://doordash-static.s3.amazonaws.com/media/photosV2/f30d732a-f0f6-4010-ad6e-26cf90a9b53a-retina-large.png"}
    ];

    // Function to handle click on popular item
    function handleItemClick(itemId) {
        console.log("Item clicked:", itemId);
        window.location.href = '/view/' + itemId; // Redirect to view page with item ID
    }

    // Loop through popular items data and append to the DOM
    var popularItemsContainer = $('#popular-items');
    $.each(popularItems, function(index, item) {
        var itemHtml = '<div class="card item" style="width: 18rem; cursor: pointer;" onclick="handleItemClick(' + item.id + ')">';
        itemHtml += '<img src="' + item.image + '" class="card-img-top" alt="' + item.title + '">';
        itemHtml += '<div class="card-body">';
        itemHtml += '<h5 class="card-title">' + item.title + '</h5>';
        itemHtml += '<a href="/view/' + item.id + '" class="btn btn-primary">View Details</a>'; // View Details button
        itemHtml += '</div></div>';
        popularItemsContainer.append(itemHtml);
    });
});

