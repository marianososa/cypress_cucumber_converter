# cypress_cucumber_converter
> Scripts that create .feature files and add cucumber preprocessor to cypress scripts that match an specific criteria
# Preconditions
- Python 3 installed
- Use gherkin notation inside the cypress project.
Example:
```
describe('As a user I want to log out from the app', () => {
  it('Given I am a logged in user', () => {
    logInPage.homepage();
    logInPage.navigateToLogin();
  });

  it('When I click on the Logout button', () => {
    homePage.clickLogOut();
  });

  it('Then I should be navigated to the login page', () => {
    logInPage.validateLoginPageIsDisplayed();
  });
});
```
# Usage
Place the .py files inside the folder that contains the cypress (.cy.js) scripts and run them in a terminal window by doing
```
python3 AddPreprocessor.py
```
> 

```
python3 CreateGherkin.py
```
The scripts will automatically detect any "cy.js" file and create the corresponding files (.feature and "cucumber_fileName.cy.js")
