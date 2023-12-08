def convert_resume_to_text(resume):
    text = ""

    # Basics Section
    basics = resume.get("basics", {})
    text += f"Name: {basics.get('name', '')}\n"
    text += f"Label: {basics.get('label', '')}\n"
    text += f"Email: {basics.get('email', '')}\n"
    text += f"Phone: {basics.get('phone', '')}\n"
    text += f"Website: {basics.get('url', '')}\n"
    text += f"Location: {basics.get('location', {}).get('city', '')}, {basics.get('location', {}).get('region', '')}, {basics.get('location', {}).get('countryCode', '')}\n"
    text += f"Summary: {basics.get('summary', '')}\n\n"

    # Work Section
    work = resume.get("work", [])
    text += "Work Experience:\n"
    for job in work:
        text += f"- {job.get('position', '')} at {job.get('name', '')}\n"
        text += f"  {job.get('startDate', '')} to {job.get('endDate', '')}\n"
        text += f"  Summary: {job.get('summary', '')}\n"
        if job.get('highlights'):
            text += f"  Highlights: {', '.join(job.get('highlights'))}\n"
        text += "\n"

    # Volunteer Section
    volunteer = resume.get("volunteer", [])
    text += "Volunteer Experience:\n"
    for org in volunteer:
        text += f"- {org.get('position', '')} at {org.get('organization', '')}\n"
        text += f"  {org.get('startDate', '')} to {org.get('endDate', '')}\n"
        text += f"  Summary: {org.get('summary', '')}\n"
        if org.get('highlights'):
            text += f"  Highlights: {', '.join(org.get('highlights'))}\n"
        text += "\n"

    # Education Section
    education = resume.get("education", [])
    text += "Education:\n"
    for school in education:
        text += f"- {school.get('studyType', '')} in {school.get('area', '')} at {school.get('institution', '')}\n"
        text += f"  {school.get('startDate', '')} to {school.get('endDate', '')}\n"
        text += f"  Score: {school.get('score', '')}\n"
        if school.get('courses'):
            text += f"  Courses: {', '.join(school.get('courses'))}\n"
        text += "\n"

    # Skills Section
    skills = resume.get("skills", [])
    text += "Skills:\n"
    for skill in skills:
        text += f"- {skill.get('name', '')}: {skill.get('level', '')}\n"
        if skill.get('keywords'):
            text += f"  Keywords: {', '.join(skill.get('keywords'))}\n"
    text += "\n"

    # Languages Section
    languages = resume.get("languages", [])
    text += "Languages:\n"
    for language in languages:
        text += f"- {language.get('language', '')}: {language.get('fluency', '')}\n"
    text += "\n"

    # Interests Section
    interests = resume.get("interests", [])
    text += "Interests:\n"
    for interest in interests:
        text += f"- {interest.get('name', '')}\n"
        if interest.get('keywords'):
            text += f"  Keywords: {', '.join(interest.get('keywords'))}\n"
    text += "\n"

    return text

# Example Usage:
json_resume = {
    "basics": {
      "name": "Aamir Ali",
      "label": "Choose based on job details",
      "image": "",
      "email": "aamirali.dev@gmail.com",
      "phone": "+92 322 7724884",
      "url": "https://aamirali-dev.github.io/",
      "summary": "write a compelling summary based on the job details",
      "location": {
        "city": "Lahore",
        "countryCode": "PK",
        "region": "Pakistan"
      },
      "profiles": [{
        "network": "github",
        "username": "aamirali-dev",
        "url": "https://github.com/aamirali-dev"
      }]
    },
    "work": [{
      "name": "Woxifi",
      "position": "Write a relevant position based on the job description",
      "url": "https://woxifi.com/",
      "startDate": "2022-10-10",
      "endDate": "Present",
      "summary": "Woxifi is a project based company. You can modify the description of the company based on the job description except the fact that it is a project based company",
      "highlights": [
        "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
      ]
    },
    {
        "name": "CERN",
        "position": "Write a relevant position based on the job description",
        "url": "https://home.cern/",
        "startDate": "2022-06-20",
        "endDate": "2022-09-09",
        "summary": "You can write the description of the company based on your knowledge and try to make it relevant to the job description",
        "highlights": [
          "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
        ]
      },
      {
          "name": "Fiverr",
          "position": "Write a relevant position based on the job description",
          "url": "https://www.fiverr.com/",
          "startDate": "2021-04-04",
          "endDate": "2022-06-20",
          "summary": "You can write the description of the company based on your knowledge and try to make it relevant to the job description",
          "highlights": [
            "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
          ]
        },
        {
            "name": "Freelancer",
            "position": "Write a relevant position based on the job description but must prepend Freelance before the position since I was working as an independent freelancer",
            "url": "https://aamirali-dev.github.io/",
            "startDate": "2020-01-01",
            "endDate": "2021-04-01",
            "summary": "I have worked as a freelancer in the local market place getting clients from whatsapp and facebook groups hence building my client base. modify this summary based on the job details",
            "highlights": [
              "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
            ]
          }],
    "volunteer": [{
      "organization": "Organization",
      "position": "Volunteer",
      "url": "https://organization.com/",
      "startDate": "2012-01-01",
      "endDate": "2013-01-01",
      "summary": "Description…",
      "highlights": [
        "Awarded 'Volunteer of the Month'"
      ]
    }],
    "education": [{
      "institution": "University of Engineering and Technology Lahore",
      "url": "https://www.uet.edu.pk/",
      "area": "Computer Science",
      "studyType": "Bachelor",
      "startDate": "write based on the requirements in the job description",
      "endDate": "write based on the requirements in the job description",
      "score": "4.0",
      "courses": [
        ""
      ]
    }],
    "awards": [{
      "title": "Award",
      "date": "2014-11-01",
      "awarder": "Company",
      "summary": "There is no spoon."
    }],
    "certificates": [
        "From the below list of certificates, choose those relevant to the job description and also sort them based on the relevance to the job description",
        {
      "name": "Certified Kubernetes Administrator ",
      "date": "2021-11-07",
      "issuer": "KodeKloud",
      "url": "https://certificate.com"
    },{
        "name": "Certified Kubernetes Security Specialist",
        "date": "2021-11-07",
        "issuer": "KodeKloud",
        "url": "https://certificate.com"
      },{
        "name": "Certified System Administrator ",
        "date": "2021-11-07",
        "issuer": "Linux Foundation",
        "url": "https://certificate.com"
      },{
        "name": "Back-End Developer",
        "date": "2021-11-07",
        "issuer": "META",
        "url": "https://certificate.com"
      },{
        "name": "Database Engineer",
        "date": "2021-11-07",
        "issuer": "META",
        "url": "https://certificate.com"
      },{
        "name": "Data Engineer",
        "date": "2021-11-07",
        "issuer": "IBM",
        "url": "https://certificate.com"
      }],
    "publications": [
        "Write publication only if relevant otherwise, remove the whole publication section",
        {
      "name": "Implementation of New Security Features in CMSWEB Kubernetes Cluster at CERN",
      "publisher": "CERN",
      "releaseDate": "2022-09-09",
      "url": "https://cds.cern.ch/record/2826676"
    }],
    "skills": [{
      "name": "fill this section based on the job description, add 4 to 5 skills and 4-5 keywords in each skill",
      "level": "select level based on the job description",
      "keywords": []
    }],
    "projects": [
        "Select a list of only relevant projects based on the job description. remove this whole section if none of the project is relevant. try to sort the them as well based on their relevance",
        {
      "name": "CrypTop",
      "startDate": "2019-01-01",
      "endDate": "2021-01-01",
      "description": "this is a cryptocurrency analysis platform, modify the description based on the job description to make it more and more relevant",
      "highlights": [
        "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
      ],
      "url": "https://project.com/"
    },{
        "name": "Algebrix",
        "startDate": "2019-01-01",
        "endDate": "2021-01-01",
        "description": "this is a linear and non-linear algebriac calculator. it can solve single equation or a system of equations, modify the description based on the job description to make it more and more relevant",
        "highlights": [
          "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
        ],
        "url": "https://project.com/"
      },{
        "name": "OtoDeck",
        "startDate": "2019-01-01",
        "endDate": "2021-01-01",
        "description": "this is a DJ Player application for playing, controlling, and mixing multiple audios. modify the description based on the job description to make it more and more relevant",
        "highlights": [
          "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
        ],
        "url": "https://project.com/"
      },{
        "name": "Hazri",
        "startDate": "2019-01-01",
        "endDate": "2021-01-01",
        "description": "this is a mess attendance management system for hostel students. modify the description based on the job description to make it more and more relevant",
        "highlights": [
          "create a list of 5-7 bullet points based on the job description in the following format <what was the achievement><how it was achieved><and what was the impact>. try your best to include numerical metrices in achievements and impact like 15M, 20%, 25k"
        ],
        "url": "https://project.com/"
      }]
  }
text_resume = convert_resume_to_text(json_resume)
print(text_resume)
