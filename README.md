# Readme
<!—
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag “enhancement”.
*** Thanks again! Now go create something AMAZING! :D
—>



<!— PROJECT SHIELDS —>
<!—
*** I’m using markdown “reference style” links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
—>

<!— TABLE OF CONTENTS —>
<details open=“open”>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href=“#about-the-project">”bout The Project</a>
      <ul>
        <li><a href="“built-with">Bu”lt With</a></li>
      </ul>
    </li>
    <li>
      <a href="#g“tting-started">Ge”ting Started</a>
      <ul>
        <li><a href="#p“erequisites">Pr”requisites</a></li>
      </ul>
    </li>
    <li><a href="#r“st-endpoints">Re”T Endpoints</a></li>

  </ol>
</details>



<!-- A—UT THE PROJECT -->
—About The Project
This repository serves as a microservice to send notification email to a student after instructor leaves feedback for a project.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* [Postman](https://www.postman.com/)

<!-- G—TING STARTED -->
—Getting Started

1. Clone this repo
2. Install dependencies `pip3 install -r requirements.txt`
3. Local development needs an API key `https://sendgrid.com/docs/api-reference/`
4. Create `sendgrid.env` under `/`
```E.G

export SENDGRID_API_KEY='<your key>'

```
7. Start Flask  Server
```
 $python3 main.py

```
### Prerequisites

* Python
* Flask

<!— USAGE EXAMPLES —>

<details open>
<summary>ReST Endpoints</summary>
<br>

### Put Email
* Sends Email to the recipient with the corresponding subject and content. Required parameters to be sent in body request as JSON.
> Required Parameters: `{“to”: “test@example.com”,  “subject”: “Test”, “content”: “This is a test”}`
```
PUT /api/v1/email
```

</details>
