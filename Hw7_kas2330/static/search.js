$(document).ready(function() {
    // Handle form submission
    $('#search-form').submit(function(event) {
        // Get the search input field value
        var query = $('#search-input').val();

        // If the query exists and contains non-whitespace characters
        if (query && query.trim()) {
            // Redirect to search results page
            window.location.href = '/search?query=' + encodeURIComponent(query.trim());
        } else {
            // Clear the search input field
            $('#search-input').val('').focus();
            // Prevent form submission
            event.preventDefault();
        }
    });

    // Handle input event on search input
    $('#search-input').on('input', function(event) {
        // Get the trimmed search query
        var query = $(this).val().trim();

        // If the query is empty or contains only whitespace
        if (!query) {
            // Keep the focus in the search input field
            $(this).focus();
        }
    });
});

