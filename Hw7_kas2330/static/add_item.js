// Submit form data via AJAX
$('#add-item-form').submit(function(event) {
    // Prevent default form submission
    event.preventDefault();

    // Serialize form data
    var formData = $(this).serialize();

    // Send AJAX POST request
    $.ajax({
        type: 'POST',
        url: '/add',
        data: formData,
        success: function(response) {
            // Display success message
            $('#add-item-form').before('<div class="alert alert-success" role="alert">New item successfully created. <a href="/view/' + response.id + '">See it here</a></div>');

            // Clear form fields
            $('#add-item-form')[0].reset();

            // Set focus on the first text box
            $('#title').focus();
        },
        error: function(xhr, status, error) {
            // Display error message
            console.error(error);
            alert('An error occurred while processing your request. Please try again.');
        }
    });
});
