/* edit_item.js */

$(document).ready(function() {
    // Submit form data via AJAX
    $('#edit-item-form').submit(function(event) {
        // Prevent default form submission
        event.preventDefault();

        // Serialize form data
        var formData = $(this).serialize();

        // Send AJAX POST request
        $.ajax({
            type: 'POST',
            url: window.location.pathname,  // Use the current URL for submission
            data: formData,
            success: function(response) {
                // Redirect to the view/<id> page after successful submission
                window.location.href = response.redirect;
            },
            error: function(xhr, status, error) {
                // Display error message
                console.error(error);
                alert('An error occurred while processing your request. Please try again.');
            }
        });
    });

    // Handle "discard changes" button click
    $('#discard-changes').click(function() {
        // Display confirmation dialog
        if (confirm('Are you sure you want to discard changes?')) {
            // Get the item ID from the URL
            var itemId = window.location.pathname.split('/').pop();
            
            // Redirect to the view/<id> page
            window.location.href = '/view/' + itemId;
        }
    });

});


