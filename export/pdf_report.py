from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(filename,data):

    doc = SimpleDocTemplate(filename)

    story = []

    for k,v in data.items():
        story.append(Paragraph(f"{k}: {v}"))

    doc.build(story)
