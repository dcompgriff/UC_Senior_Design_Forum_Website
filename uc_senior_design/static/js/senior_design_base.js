$(document).ready(function(){

    
    //JQuery code to retrieve the project list for the current program and year.
    $("#get_projects").click(function(){
        $("#project_list").load('../projects/cmpe/2016/');
    });
    $("#remove_projects").click(function(){
        $("#project_list").empty();
    });

    //Simulate an initial click on the program list to load data.
    $(".list-group-item.program").first().click();

    $('.dropdown-toggle').dropdown();

});


//Code for the program selection list.
$(document).on("click", ".list-group-item.program", function(){
    //JQuery code to update the program selected.
    $(".list-group-item.program").removeClass("active");
    $(this).addClass("active");

    //Clear the project listing.
    $("#project_list").empty();

    //JQuery to retrieve the currenlty active panel, and to 
    var degree_program = $(this).text()
    //Set degree program name to lowercase.
    degree_program = degree_program.toLowerCase()
    degree_program_sentence_list = degree_program.split(" ")
    degree_program = ""
    //Remove spaces, and add an underscore.
    for(i = 0; i< degree_program_sentence_list.length; i++){
        degree_program += degree_program_sentence_list[i] + "_"
    }
    //Remove the last underscore added by the loop.
    degree_program = degree_program.slice(0, degree_program.length - 1)    
    //Retrieve the selected year.
    year = $("#year_input").val()
    year = year.slice(0, 4)    
    //Send the query.
    $("#project_list").load('../projects/' + degree_program + "/" + year + "/");
});
