// Handles navigation between different sections of the webpage 
function showSection(sectionId) {
    // Get all elements with class "section"
    const sections = document.querySelectorAll('.section')

    sections.forEach(section => {
        if (section.id === sectionId) {
            section.classList.remove('hidden')
        }
        else {
            section.classList.add('hidden')
        }
    });
    
    console.log(sectionId)
    if (sectionId === "recent") {
        console.log("loading table in recent"); 
    }
        
    // ADD CODE TO UPDATE COLOUR OF NAVIGATION BUTTONS IN HEADER
}


function submitReport() {
    console.log("in submitReport() function")

    const form = document.getElementById("report-form"); 
    const formData = new FormData(form); 
    
    fetch("/submit-report", {
        method: "POST", 
        body: formData 
    }).then(res => {
        if (res.ok) {
            console.log("Report submitted")
            form.reset(); 
        }
        else {
            console.log("Error submitting report")
        }
    }); 
}




