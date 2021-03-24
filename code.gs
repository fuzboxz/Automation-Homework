// CODE FOR AUTOMATING THE GOOGLE PART OF THE HOMEWORK
// Replace the id's in the SpreadsheettoForm function with your own
// cast_sheet_id comes from the script output
// for email_sheet_id create your own spreadsheet with the emails and copy the id in the URL

function SpreadsheettoForm() {
  // Main function of the script
  // Add the id of the cast and email spreadsheets here
  let cast_sheet_id = "ADD_CAST_SHEET_ID_HERE"
  let email_sheet_id = 'ADD_EMAIL_SHEET_ID_HERE'

  let formURL = createForm(cast_sheet_id)
  Logger.log("Published URL: " + formURL["puburl"])
  Logger.log("Edit URL: " + formURL["editurl"])
  sendToContacts(formURL, email_sheet_id)
}

function createForm(cast_sheet_id) {
  // Creates the form based on the values in the cast sheet
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