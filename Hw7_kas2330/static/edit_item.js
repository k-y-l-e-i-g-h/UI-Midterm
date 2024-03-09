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
                window.location.href = response.redirect;
            },
            error: function(xhr, status, error) {
                console.error(error);
                alert('An error occurred while processing your request. Please try again.');
            }
        });
    });

    // Define the discardChanges function
    function discardChanges(itemId) {
        // Display confirmation dialog
        if (confirm('Are you sure you want to discard changes?')) {
            window.location.href = '/view/' + itemId;
        }
    }

    // Attach event handler to the "Discard Changes" button
    $('.discard-button').click(function(event) {
        event.preventDefault();
        console.log('Discard button clicked');

        var itemId = $(this).data('item-id');
        console.log('Item ID:', itemId);

        discardChanges(itemId); // Call discardChanges function with item ID
    });

});
