Changelog
=========

1.0.0 (2020-04-29)
------------

- Remove unnecessary classes and add missing order status. [Alefh Sousa]

  Some classes were unnecessary to make the payload to send to konduto, this way I removed from the project.

  Another change is in some corner cases of case sensitive to create KondutoOrderStatus or KondutoRecommentation based on the response from Konduto.

  For the last, I added some missing KondutoOrderStatus like PENDING and NOT_ANALYZED when some order return this status broken the app because she can't parse the value

- Change return methods to use Right and Left abstraction. [Alefh Sousa]

  When you use the client is hard to verify whether the operation is a success or failure to check this was necessary to check the class type.

  Now all operation that can be failed return a Union[Right, Left] this way:

  Right is a successful operation and Left is a failure operation
  
- Add konduto prefix in all class. [Alefh Sousa]

  To avoid ambiguous names when someone uses in your domain, for example, whether someone uses this SDK in e-commerce in the code is very possible that have:

  Customer -> Domain
  Customer -> Konduto

  and when we read the code is very complex to understand the difference between the customer class.

  with these changes the code is more legible:

  Customer -> Domain
  KondutoCustomer -> Konduto.
  
- Remove unnecessary classes and change all enums to lower case. [Alefh Sousa]
- Set theme jekyll-theme-cayman. [Alefh Sousa]
- Add folder for gh pages. [Alefh Sousa]
- Fix workflow file from github actions. [Alefh Sousa]

  When is created a workflow file in the GitHub actions, they not update this file anymore, this way when I created the file on pr #5 this wad a typo in the `releases` and broken the job. I fix this file in the pr, but GitHub not updated this file :(

  I think this is a bug from GitHub actions and already an issue in the GitHub community https://github.community/t5/GitHub-Actions/Workflow-file-not-updating-anymore

  To fix the problem I renamed the file and created new commit.
- Remove release-pypi file from github actions workflows. [Alefh Sousa]



0.1.0 (2020-04-06)
------------

- Add restrict list client. [Alefh Sousa]

  include restrict the client with all operations supported by konduto API, this way is possible to:

  1) create a restrict entry
  2) update a restrict entry
  3) load information from restrict entry
  4) remove a restrict entry

  The konduto API called this resource as "blacklist" but here I prefer to call for `RestrictList` because the word `blacklist` is a very offensive term and we already have an event to stop the use of these words that can be offensive.

  You can read more here: https://www.theregister.co.uk/2019/09/03/chromium_microsoft_offensive/

- Configure codecov status check. [Alefh Sousa]

- Improve documentation. [Alefh Sousa]

  Improve documentation including readme in the project and add docstring for some core class

- Add github actions for ci and codecov for code quality. [Alefh Sousa]

  Setup the GitHub action as a tool to CI and Codev as a tool to quality code, the ci configured is based on:

  Python versions 3.6, 3.7 and 3.8 and the workflow is:

  1. setup machines
  2. setup python version
  3. install dependencies
  4. check code style
  5. run unit tests
  6. upload coverage to codecov

  I changed the Makefile to delete unused targets and remove PyYaml from dependencies because this dependency doesn't is used in the project
- Initial project :tada: [Alefh Sousa]


