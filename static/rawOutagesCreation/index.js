const createRawOutages = function() {
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;

    $.ajax({
        type: 'post',
        dataType: 'json',
        contentType: "application/json",
        data: JSON.stringify({ startDate: startDate, endDate: endDate }),
        success: function(response) {
            // $('#response').text('Response : ' + response);
            console.log(response)
        }
    });
}

document.getElementById('createRawOutagesBtn').onclick = createRawOutages