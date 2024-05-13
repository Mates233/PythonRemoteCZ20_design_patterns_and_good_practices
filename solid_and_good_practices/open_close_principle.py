class ReportGenerator:

    def __init__(self, data):
        self.data = data

    def generate(self):
        return "Report:\n" + "\n".join([f"{key}: {value}" for key, value in self.data.items()])


class HTMLReportGenerator(ReportGenerator):

    def generate(self):
        html_content = "<html><body><h1>Report</h1><ul>"
        for key, value in self.data.items():
            html_content += f"<li>{key}: {value}</li>"
        html_content += "</ul></body></html>"
        return html_content


class PDFReportGenerator(ReportGenerator):

    def generate(self):
        # Imagine this is a complex PDF generation logic
        return f"PDF Report -- {self.data}"