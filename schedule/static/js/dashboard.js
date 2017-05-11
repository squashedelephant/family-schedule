function submitParentForm(event) {
    var values = $(this).serialize();
    url = "/dashboard/parent";
    var submitParent = $.ajax({method: "POST",
                               data: JSON.stringify(values),
                               url: url});
    submitParent.done(function(data) {
        console.log("submitted ParentForm response: " + String(data));
        var parentId = JSON.parse(data)["data"]["id"]
        alert("Parent: " + parentId + " created");
        location.reload()
        console.log("form.submitParentForm done");
    });
    submitParent.fail(function(jqXHR, textStatus) {
        console.log("form.submitParentForm fail");
    });
}

function clickCreateParent(event) {
    var plink = document.getElementById("#plink");
    console.log("plink properties: " + Object.keys(plink));
    console.log("registering parent.submit");
    $("#parent").on("submit", submitParentForm(event));
}

function loadDashboardForm(event) {
    url = "/dashboard/schedule";
    var loadForm = $.ajax({method: "GET",
                           url: url});
    loadForm.done(function(data) {
        $("#dashboard").empty().append(data);
        console.log("loadDashboardForm done");
    });
    loadForm.fail(function(data) {
        console.log("loadDashboardForm fail");
    });
}

function submitDashboardForm(event) {
    event.preventDefault();
    var values = $(this).serialize();
    url = "/dashboard/schedule";
    getSummary = $.ajax({method: "POST",
                          data: JSON.stringify(values),
                          url: url});
    getSummary.done(function(data) {
        $("#dashboard").hide();
        console.log("retrieved: " + data);
        $("#result").empty().append(data);
        console.log("getSummary done");
    });
    getSummary.fail(function(jqXHR, textStatus) {
        console.log("getSummary failed");
    });
}

$(document).ready(function() {
    console.log("registering plink.click");
    //$("#plink").on("click", clickCreateParent);
    $("#dashboard").on("submit", submitDashboardForm);
    loadDashboardForm();
});
