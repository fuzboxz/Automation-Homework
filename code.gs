function SpreadsheettoForm() {
  Logger.log("Getting top5 id")
  let cast_sheet_id = getSheetId("top5")
  Logger.log("Getting automation_email id")
  let email_sheet_id = getSheetId("automation_email")

  let formURL = createForm(cast_sheet_id)
  Logger.log("Published URL: " + formURL["puburl"])
  Logger.log("Edit URL: " + formURL["editurl"])
  sendToContacts(formURL, email_sheet_id)
}

function getSheetId(filename){
  return DriveApp.getFilesByName(filename).next().getId()
}

function createForm(cast_sheet_id) {
  try{
    DriveApp.getFilesByName("Top Cast").next().getId()
  }
  catch (err) {
    Logger.log("Error deleting previous forms. Maybe no previous form was created?")
  }
  
  let cast = Sheets.Spreadsheets.Values.get(cast_sheet_id, 'A1:A').values
  
  let cast_form = FormApp.create("Top Cast")
  cast_form.addMultipleChoiceItem()
    .setTitle("Which one of these is your favorite?")
    .setChoiceValues(cast)
    .showOtherOption(false);
  return {"puburl": cast_form.getPublishedUrl(), "editurl": cast_form.getEditUrl()} 
}


function sendToContacts(formURL, email_sheet_id) {
  // Sends formURL to contacts specified in the spreadsheet

  let addresses = Sheets.Spreadsheets.Values.get(email_sheet_id, 'A1:A')
  let subject = "Form is ready"
  let body = "The form is ready, you can access it here " + formURL["puburl"] +" (published URL) and edit it here " + formURL["editurl"] + " (edit URL)." 
  Logger.log("Emails will be sent out with subject '" + subject + "' and body of '" + body +"'")
  for (let counter = 0; counter < addresses.values.length; counter++) {
    let recipient = String(addresses.values[counter])
    Logger.log("Sending email to: " + recipient)
    MailApp.sendEmail(recipient=recipient, subject=subject, body=body)
  }
}