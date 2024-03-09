// home.js
$(document).ready(function() {
    console.log("home.js is executing.");
    // Define data for popular items (You can modify this according to your data)
    var popularItems = [
        {id: 11, title: "Churu Cat Treat", image: "../static/images/churu_small1.jpeg", rating: 5.0},
        {id: 6, title: "Cat Dancer Toy", image: "../static/images/cat_dancer_med.jpeg", rating: 4.6},
        {id: 2, title: "Electric Lady Bug", image: "../static/images/ladybug_med.jpeg", rating: 4.0}
    ];

    // Function to handle click on popular item
    function handleItemClick(itemId) {
        console.log("Item clicked:", itemId);
        window.location.href = '/view/' + itemId; // Redirect to view page with item ID
    }

    function populateStars() {
        $('.stars').each(function() {
          var rating = parseFloat($(this).attr('data-rating')); // Get rating from data attribute
          console.log(rating);
          var starsHtml = '';
          for (var i = 0; i < 5; i++) {
            if (i < rating) {
              starsHtml += '<span class="fa fa-star checked"></span>';
            } else {
              starsHtml += '<span class="fa fa-star"></span>';
            }
          }
          $(this).html(starsHtml); // Populate stars inside the container
        });
    }

    // Loop through popular items data and append to the DOM
    var popularItemsContainer = $('#popular-items');
    $.each(popularItems, function(index, item) {
        var itemHtml = '<div class="col-md-4 mb-3">';
        itemHtml += '<div class="card item" style="cursor: pointer;">';
        itemHtml += '<img src="' + item.image + '" class="card-img-top" alt="' + item.title + '" data-item-id="' + item.id + '">';
        itemHtml += '<div class="card-body">';
        itemHtml += '<h5 class="card-title">' + item.title + '</h5>';
        itemHtml += '<div class="stars" data-rating="' + item.rating + '"></div>'
        itemHtml += '</div></div></div>';
        popularItemsContainer.append(itemHtml);
    });

    $('.stars').each(function() {
      var rating = parseInt($(this).attr('data-rating')); // Get rating from data attribute
      console.log(rating);
      var starsHtml = '';
      for (var i = 0; i < 5; i++) {
        if (i < rating) {
          starsHtml += '<span class="fa fa-star checked"></span>';
        } else {
          starsHtml += '<span class="fa fa-star"></span>';
        }
      }
      $(this).html(starsHtml); // Populate stars inside the container
    });
    // Delegate click event to dynamically created elements
    popularItemsContainer.on('click', '.card.item', function() {
        var itemId = $(this).find('img').data('item-id');
        handleItemClick(itemId);
    });

});
