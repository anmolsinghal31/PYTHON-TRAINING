from bs4 import BeautifulSoup

# This represents the HTML you would "find" on the hospital's patient list page
html_content = """
<table>
    <tr><th>Name</th><th>Age</th><th>Doctor</th></tr>
    <tr><td>Sarah Jenkins</td><td>29</td><td>Dr. Adams</td></tr>
    <tr><td>Robert Paul</td><td>52</td><td>Dr. Baker</td></tr>
</table>
"""


def test_extract_patient_data():
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')[1:]  # Skipping the header row

    patient_names = []
    for row in rows:
        cells = row.find_all('td')
        patient_names.append(cells[0].text)

    print(f"Extracted Patients: {patient_names}")
    assert "Sarah Jenkins" in patient_names