scraped_data = ['Name:','Aalok Dinkar Khandekar', 'Position:','Assistant Professor', 'Department(s):', 'Liberal Arts', 'Climate Change', 'Ph.D:', 'Rensselaer Polytechnic Institute', 'Research Interests:', 'Science, technology, and society studies (STS)', 'Environmental sustainability', 'Urban studies', 'Cultural anthropology', 'Climate Change', 'Energy', 'Waste Management', 'Design Innovation', 'Tangible and Intangible Heritage', 'Health & Society', 'Social Sciences', 'Office Address:', 'Room B-316', 'Academic Block B', 'Indian Institute of Technology Hyderabad', 'Kandi-502284, Sangareddy', 'Telangana, India', 'E-mail:', 'Office Phone:','(040) 2301 - 6513']

result_dict = {}
current_key = None
current_values = []

for item in scraped_data:   
    if ':' in item:
        if current_key is not None:
            result_dict[current_key] = current_values
        current_key = item.rstrip(':')
        current_values = []
    else:
        current_values.append(item)

if current_key is not None:
    result_dict[current_key] = current_values

result_dict['Office Address']=', '.join(result_dict['Office Address'])
for key, value in result_dict.items():
    print(key,':',value)