

/* 
Script runs every 24 hours. Will parse the HTML for the search link from an unread linked 
job posting email and upload the job search link to a specific G Drive folder. 
*/

// Daily Trigger
function setTrigger(){
  ScriptApp.newTrigger('getLinkedInJobAlerts')
  .timeBased()
  .everyHours(24)
  .create();
}

// Parse for HTML link... 
function getLinkedInJobAlerts() {
  
  // Searching for unread job posting email with a custome label: linkedin_job_alerts
  var job_alert_email = GmailApp.search('label:unread and label:linkedin_job_alerts');
  var first_email     = job_alert_email[0];
  GmailApp.markThreadsRead(job_alert_email);
  
  // Check for NULL
  if (first_email != undefined){
    var todays_date       = Utilities.formatDate(new Date(), "EST", "yyyy-MM-dd");
    var message_to_parse  = first_email.getMessages()[0].getPlainBody();
    var start_position    = message_to_parse.search("See more new jobs: ") + "See more new jobs: ".length;
    var end_position      = message_to_parse.search("Manage job alerts:");
    
    // Update log before posting to gdrive...
    postToDrive(todays_date, message_to_parse.substring(start_position, end_position));
    console.log("Created " + "LinkedIn_Daily " + todays_date + ".txt" + " on " + todays_date);
  }
  else{
    console.log("New job posting email from LinkedIn not found for " + todays_date);
  }
}

/*
// Helper to send emails.
function sendEmail(date, body) {
  GmailApp.sendEmail("kaushik.bhimraj@gmail.com", "Lasted Jobs from LinkedIn - " + date, body);
}
*/

// Create a new file in the Job_Links on G Drive. 
// File format -> {LinkedIn_Daily 2020-mm-dd.txt}
function postToDrive(date, body){
  var folders = DriveApp.getFolders();

  while (folders.hasNext()) {
    var folder = folders.next();
    var folderName = folder.getName();
    
    if (folderName == "Job_Links"){
      folder.createFile("LinkedIn_Daily " + date + ".txt", body);
    }
  }
}
