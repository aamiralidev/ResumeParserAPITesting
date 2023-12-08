

def export_to_json(resume):
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
