import PyPDF2 # This is a pdf library that navigate 
# import sys # This call using the system function to run value

'''This changes pdf files to watermark pdf file'''
template = PyPDF2.PdfReader(open("super.pdf", "rb")) # Var carries the lib that open files that needs to be watermarked
watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb")) # Var carries the watermarked sample file

output = PyPDF2.PdfWriter() # This edit file when opened

num_watermark_pages = len(watermark.pages)  # Get the number of pages in the watermark PDF

for i in range(len(template.pages)): # This go into the template file and try adding wtr.pdf to each element
    page = template.pages[i]
    page.merge_page(watermark.pages[i % num_watermark_pages])  # Use modulus to cycle through watermark pages
    output.add_page(page)


with open("watermarked_output.pdf", "wb") as file: # new file that holds the watermarked 
    output.write(file)



# ALSO: Check out the below code and remove the commit up beside import sys 

'''This is to combine multiple pdf files as one file'''
input = sys.argv[1:] # keep all argv from second value

def combiner(pdf_list): # The func combines pdf files using merger
    merger = PyPDF2.PdfMerger() # merger obj
    for pdf in pdf_list: # literate over pdf file
        print(pdf)
        merger.append(pdf) # This saves and keeps file in new py file
    merger.write('super.pdf') # new py file creation without using with func to write or read file.

combiner(input)


# Continue exploring

'''This is to rotate the pdf file'''
# Test to understand pdf code file

with open("dummy.pdf", "rb") as file: # open a file and make it accessable by using rb= read binary
    reader = PyPDF2.PdfReader(file) # This read the pdf file
    num_pages = len(reader.pages) # This shows the num of pdf file
    writer = PyPDF2.PdfWriter() # This over write the file and trying changing to rotating form
    for page in range(num_pages): # loop into the file and rotate 
        page_obj = reader.pages[page]
        page_obj.rotate(90)  # Rotate the page 90 degrees clockwise
        writer.add_page(page_obj)

    with open("tilt.pdf", "wb") as new_file: # Turn the rotated file into another file by over riding it using wb= write binary
        writer.write(new_file)

