with open('inputex12.txt', 'r') as input_file:
    lines = input_file.readlines()
document_header = lines[0].strip()
heading = lines[1].strip()
paragraphs = [line.strip() for line in lines[2:]]

with open('index.html', 'w') as output_file:
    output_file.write('<!DOCTYPE html>\n')
    output_file.write('<html>\n')
    output_file.write('<head>\n')
    output_file.write('<title>{}</title>\n'.format(document_header))
    output_file.write('</head>\n')
    output_file.write('<body>\n')
    output_file.write('<h1>{}</h1>\n'.format(heading))
    for paragraph in paragraphs:
        output_file.write('<p>{}</p>\n'.format(paragraph))
    output_file.write('</body>\n')
    output_file.write('</html>\n')
