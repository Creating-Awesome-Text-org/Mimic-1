# from tempfile import NamedTemporaryFile
#
#
#
# def files_to_vector_store(files: list):
#     for file in files:
#         name_split = file.filename.split(".")  # Split the file name using the dot seperator
#         file_type = name_split[1]  # Determine the file type
#
#         file_content = file.read()
#         file_bytes = bytes(file_content)
#
#         file_type_handling(file_type, file_bytes)  # File type specific handling
#
#
# def file_type_handling(file_type: str, temp_file):
#     match file_type:
#         case "pdf":
#             print("PDF detected")
#         case "txt":
#             print("txt detected")
#             txt_file_upload(temp_file)
#         case "md":
#             print("md detected")
#         case "docx":
#             print("docx detected")
#         case _:
#             print("File type not recognized")
#
#
# def txt_file_upload(temp_file):
#     text_loader = TextLoader(temp_file)
#     document_text = text_loader.load()
#     print(document_text)
