    $(document).ready(function(){
    
    //After an image has been selected, get the file contents as a base64
    //string to be transfered to the server with the rest of the form data.
    fileData = null;
    $("#add_project_image").change(function () {
        //Start conversion and disable the add button until it's finished.
        $('#add_project_add').disabled = true;
        fileReader = new FileReader();
        //Save the result and enable the add button after the conversion
        //is finished.
        fileReader.addEventListener("load", function () {
            fileData = fileReader.result;
            $('#add_project_add').disabled = false;
        }, false);
        // Convert file
        var fileSelected = $("#add_project_image")[0];
        var file = fileSelected.files[0];
        fileReader.readAsDataURL(file);
    });
    
    //JQuery code to retrieve the project list for the current program and year.
    //$("#get_projects").click(function(){
    //    $("#project_list").load('../projects/cmpe/2016/');
    //});
    $("#remove_projects").click(function(){
        $("#project_list").empty();
    });

    //Call function to initialize the year dropdown.
    //Note: This must be called before the .list-group-item function.
    $("#years_list").load('../projects/years/');

    //Get the list of years for the dropdown.
    $.get("../projects/years/", function(data, status){
        year_list = data.year_list;
        year_list.sort();
        //Add years to the dropdown.
        for(i = 0; i<year_list.length; i++){
            if(i == 0){
                //Make year html items.
                listItem = document.createElement("li");
                anchor = document.createElement("a");
                //Set classes for the anchors i the list items of the dropdown.
                $(anchor).addClass("year_item");
                $(anchor).addClass("active_year");
                $(anchor).addClass("dropdown-toggle")
                $(anchor).attr("href", function(i, orig){
                    return "#";
                });
                $(anchor).attr("data-toggle", function(i, orig){
                    return "dropdown";
                });
                $(anchor).text(year_list[i]);
                //Add the anchor to the list item, and add the list item to the year_list.
                $(listItem).append(anchor);
                $("#year_list").append(listItem);
            }else{
                //Make year html items.
                listItem = document.createElement("li");
                listItem = document.createElement("li");
                anchor = document.createElement("a");
                //Set classes for the anchors i the list items of the dropdown.
                $(anchor).addClass("year_item");
                $(anchor).addClass("dropdown-toggle")
                $(anchor).attr("href", function(i, orig){
                    return "#";
                });
                $(anchor).attr("data-toggle", function(i, orig){
                    return "dropdown";
                });
                $(anchor).text(year_list[i]);
                $(listItem).append(anchor);
                //Add the anchor to the list item, and add the list item to the year_list.
                $("#year_list").append(listItem);
            }
        }
        //Set the text of the dropdown to the first year.
        $("#year_button").html(year_list[0] + "<span class=\"caret\"></span>");


        //Note, the binding of this function to the .year_item class must be called after 
        //elements have been added to the DOM that have this class.
        $(".year_item").click(function(){
            //Reset all year items.
            $(".year_item").removeClass("active_year");
            //Set the current year item as active.
            $(this).addClass("active_year");
            //Update the year button with the current year.
            $("#year_button").html($(this).text() + "<span class=\"caret\"></span>");
            //Call the initial click on the program list to load data.
            $(".list-group-item.program.active").click();
        });

    });

    //Functions used to show and hide the create project panel.
    $("#add_project").click(function(){
        //$("#add_project_inputs").load('../projects/addprojectform/', function(){
            $("#add_project_inputs").show("slow");
        //});
    });
    $("#add_project_cancel").click(function(){
        $("#add_project_inputs").hide("slow");
        //$("#add_project_inputs").empty()
    });


    //Functions to collect the new project parameters and submit to the PUT "projects/" url.
    $("#add_project_add").click(function(){
        var projectJson = {}
        projectJson.Title = $("#add_project_title").val();
        projectJson.Topic = $("#add_project_topic").val();
        projectJson.Abstract = $("#add_project_abstract").val();
        projectJson.Group = $("#add_project_members").val();
        projectJson.Advisor = $("#add_project_advisor").val();
        projectJson.Futurework = $("#add_project_future_work").val();
        projectJson.Year = $("#year_button").text();
        //Get the degree program name for the currently selected program.
        var degree_program = $(".list-group-item.program.active").text();
        //Set degree program name to lowercase.
        degree_program = degree_program.toLowerCase();
        degree_program_sentence_list = degree_program.split(" ");
        degree_program = "";
        //Remove spaces, and add an underscore.
        for(i = 0; i< degree_program_sentence_list.length; i++){
            degree_program += degree_program_sentence_list[i] + "_";
        }
        //Remove the last underscore added by the loop.
        degree_program = degree_program.slice(0, degree_program.length - 1);
        projectJson.Program = degree_program;

        //Image file and data
        projectJson.ImageFile = fileData;
        var fileSelected = $("#add_project_image")[0];
        var file = fileSelected.files[0];
        projectJson.PosterImage = file.name
        
        $.post("../projects/project/", JSON.stringify(projectJson), function(){
            $("#add_project_inputs").hide("slow");
            $("#add_project_inputs").empty();
            $(".list-group-item.program.active").click();
        });

    });

});


//Code for the program selection list.
$(document).on("click", ".list-group-item.program", function(){
    //JQuery code to update the program selected.
    $(".list-group-item.program").removeClass("active");
    $(this).addClass("active");

    //Clear the project listing.
    $("#project_list").empty();

    //JQuery to retrieve the currenlty active panel, and to 
    var degree_program = $(this).text();
    //Set degree program name to lowercase.
    degree_program = degree_program.toLowerCase();
    degree_program_sentence_list = degree_program.split(" ");
    degree_program = "";
    //Remove spaces, and add an underscore.
    for(i = 0; i< degree_program_sentence_list.length; i++){
        degree_program += degree_program_sentence_list[i] + "_";
    }
    //Remove the last underscore added by the loop.
    degree_program = degree_program.slice(0, degree_program.length - 1); 
    //Retrieve the selected year.
    var year = $("#year_button").text();
    year = year.slice(0, 4);   
    //Send the query.
    $("#project_list").load('../projects/' + degree_program + "/" + year + "/", function(){
        $("#num_projects").text($(".animated.grow.panel").length);
    });
});


function handler() {
    alert(this.responseText);
}