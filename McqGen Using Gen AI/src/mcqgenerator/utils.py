import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception('error while reading with file')
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file supported"
            )
        
def get_table_data(quiz_str):
    try:
        # convert the quiz from str to dict
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]
        
        # Iterate over the quiz dictionary and extract the required information
        for key,value in quiz_dict.items():
            mcq=value['mcq']
            options="  ||  ".join(
                [
                    f"(option)->{option_value}" for option,option_value in value["options"].items()
                    
                ]
            )
            
            correct=value['correct']
            quiz_table_data.append({"MCQ":mcq, "Choices":options, "Correct":correct})
        
        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
    
# import os
# import PyPDF2
# import json
# import traceback

# def read_file(file):
#     """
#     Reads the contents of a file.

#     Args:
#     file: File object to be read.

#     Returns:
#     Text content of the file.
#     """
#     try:
#         if file.name.endswith(".pdf"):
#             pdf_reader = PyPDF2.PdfFileReader(file)
#             text = ""
#             for page in pdf_reader.pages:
#                 text += page.extract_text()
#             return text
#         elif file.name.endswith(".txt"):
#             # Assuming text files are encoded in UTF-8
#             return file.read().decode("utf-8")
#         else:
#             raise Exception("Unsupported file format. Only PDF and text files are supported.")
#     except Exception as e:
#         raise Exception(f"Error while reading file: {str(e)}")

# def get_table_data(quiz_str):
#     """
#     Extracts quiz data from a JSON string.

#     Args:
#     quiz_str: JSON string containing quiz data.

#     Returns:
#     List of dictionaries containing quiz data.
#     """
#     try:
#         quiz_dict = json.loads(quiz_str)
#         quiz_table_data = []
        
#         for key, value in quiz_dict.items():
#             mcq = value['mcq']
#             options = " || ".join([f"(option)->{option_value}" for option, option_value in value["options"].items()])
#             correct = value['correct']
#             quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        
#         return quiz_table_data
#     except Exception as e:
#         traceback.print_exception(type(e), e, e.__traceback__)
#         # Consider logging the exception or handling it in a more specific manner
#         return False
