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
                console.error(error);
                alert('An error occurred while processing your request. Please try again.');
            }
        });
    });

    // Define the discardChanges function
    function discardChanges(itemId) {
        // Display confirmation dialog
        if (confirm('Are you sure you want to discard changes?')) {
            window.location.href = '/edit/' + itemId + '?action=discard'; // 
        }
    }

    //Define the function to discard changes
    // $( "#dialog" ).dialog({ autoOpen: false });
    // function discardChanges(itemId) {
    //     // Display confirmation dialog
    //     $("#discard-dialog").dialog({
    //         resizable: false,
    //         height: "auto",
    //         width: 400,
    //         modal: true,
    //         buttons: {
    //             Confirm: function() {
    //                 $(this).dialog("close");
    //                 // Send AJAX request to discard changes
    //                 $.ajax({
    //                     type: 'GET',
    //                     url: '/edit/' + itemId + '?action=discard',
    //                     success: function(response) {
    //                         // Redirect to the view item page
    //                         window.location.href = '/view/' + itemId;
    //                     },
    //                     error: function(xhr, status, error) {
    //                         console.error(error);
    //                         alert('An error occurred while processing your request. Please try again.');
    //                     }
    //                 });
    //             },
    //             Cancel: function() {
    //                 $(this).dialog("close");
    //             }
    //         }
    //     });
    // }

    // // Attach event handler to the "Discard Changes" button
    // $('.discard-button').click(function(event) {
    //     event.preventDefault(); // Prevent the default action of the button
    //     console.log('Discard button clicked'); // Debugging message

    //     var itemId = $(this).data('item-id');
    //     console.log('Item ID:', itemId); // Debugging message

    //     discardChanges(itemId); // Call discardChanges function with item ID
    // });

});
