Changelog
=========


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


