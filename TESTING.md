# Testing

## Site Goals & User Story testing

User stories were tracked in a [google sheet](https://docs.google.com/spreadsheets/d/1cLw34TLgnHsWQUCyxNQNolB0Wog3KuQlkmCOjkjQZpg/edit?usp=sharing) as well on the [project board](https://github.com/users/eosull/projects/7). The testing criteria for each user story is presented on each user story on the google sheet along with completion status

## Link Testing

Site links tested using [Broken Link Checker](https://www.brokenlinkcheck.com/broken-links.php#status) with no broken links being shown

| ![Broken Link Check](/assets/readme_images/broken_links_check.png) |
|:--:|
|Broken Link Check|

## HTML Validator Testing

HTML Code validation was carried out using [W3 Validation](https://validator.w3.org/) with results as follows:

| Page | Result |
| ---- | ------ |
| Home | Pass |
| Products | Pass |
| Product Detail | Pass |
| Edit Product | Pass |
| Delete Product | Pass |
| Basket | Pass |
| Checkout | Pass |
| Checkout Success | Pass |
| About | Pass |
| Faqs | Pass |
| Edit Faq | Pass |
| Add Faq | Pass |
| Contact | Pass |
| Login | Pass |
| Logout | Pass |
| Register | Pass |
| Profile | Pass |

Any remaining warnings are as a result of django templating tags.

## CSS Validator Testing

CSS Validation carried out using [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) with results as follows:

| Page | Result |
| ---- | ------ |
| Base CSS | Pass |
| About CSS | Pass |
| Checkout CSS | Pass |
| Profile CSS | Pass |

## Javascript & Python Testing

Javascript testing completed using [JSHint](https://jshint.com/) with all code passing without issues. Python code formatting was tested tested continuously during development using [pycodestyle](https://pypi.org/project/pycodestyle/) extenstion in VS code for Gitpod. A final flake8 report was run on Python code with only unavoidable line length and whitespace warnings showing up.

## Accessibility & SEO

Accesibility testing completed using Chrome Developer Tools [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) results can be seen below

| ![Lighthouse Report](/assets/readme_images/lighthouse_report.png) |
|:--:|
|Lighthouse Report|

## Bugs during production

Any bugs found during production were either added as an or can be seen in the [GitHub issues page](https://github.com/eosull/Seoda-By-Sophie/issues?q=is%3Aissue+is%3Aclosed+label%3Abug) or via commits with the message starting with 'fix' [here](https://github.com/eosull/Seoda-By-Sophie/commits/main)
