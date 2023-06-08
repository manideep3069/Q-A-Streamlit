
# # # # # import os
# # # # # import tempfile
# # # # # import torch
# # # # # from transformers import BertForQuestionAnswering, BertTokenizer
# # # # # import streamlit as st
# # # # # from pyngrok import ngrok

# # # # # # Load the pre-trained model and tokenizer
# # # # # model_name = 'bert-base-uncased'
# # # # # model = BertForQuestionAnswering.from_pretrained(model_name)
# # # # # tokenizer = BertTokenizer.from_pretrained(model_name)


# # # # # def extract_text_from_file(file_path):
# # # # #     _, file_extension = os.path.splitext(file_path)
# # # # #     if file_extension == '.pdf':
# # # # #         # Handle PDF files
# # # # #         from PyPDF2 import PdfFileReader
# # # # #         with open(file_path, 'rb') as f:
# # # # #             pdf = PdfFileReader(f)
# # # # #             text = ""
# # # # #             for page_num in range(pdf.numPages):
# # # # #                 page = pdf.getPage(page_num)
# # # # #                 text += page.extract_text()
# # # # #     else:
# # # # #         # Handle text files
# # # # #         with open(file_path, 'r') as f:
# # # # #             text = f.read()
# # # # #     return text


# # # # # def answer_question(file_path, question):
# # # # #     context = extract_text_from_file(file_path)
# # # # #     # Tokenize the inputs and handle long sequences
# # # # #     inputs = tokenizer.encode_plus(question, context, add_special_tokens=True,
# # # # #                                    return_tensors='pt', max_length=512, truncation_strategy='only_second')
# # # # #     # Generate predictions
# # # # #     start_logits, end_logits = model(**inputs).values()
# # # # #     # Find the start and end indices with the highest logits
# # # # #     start_index = torch.argmax(start_logits)
# # # # #     end_index = torch.argmax(end_logits)
# # # # #     # Get the tokens corresponding to the answer
# # # # #     tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())
# # # # #     answer = ' '.join(tokens[start_index:end_index + 1]).replace(' ##', '')
# # # # #     return answer


# # # # # def main():
# # # # #     st.title("Question Answering from PDF or Text Files")
# # # # #     st.markdown(
# # # # #         "Upload a PDF or text file and ask a question to get the answer.")
# # # # #     # File upload
# # # # #     file = st.file_uploader("Upload a file", type=["pdf", "txt"])
# # # # #     # Question input
# # # # #     question = st.text_input("Enter your question")
# # # # #     if file is not None and question != "":
# # # # #         # Save uploaded file as temporary file
# # # # #         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
# # # # #             temp_path = temp_file.name
# # # # #             temp_file.write(file.read())
# # # # #         try:
# # # # #             # Answer the question
# # # # #             answer = answer_question(temp_path, question)
# # # # #             # Display the answer
# # # # #             st.markdown(f"**Question:** {question}")
# # # # #             st.markdown(f"**Answer:** {answer}")
# # # # #         except Exception as e:
# # # # #             st.error(f"Error: {e}")
# # # # #         # Remove temporary file
# # # # #         st.button("Remove Temporary File",
# # # # #                   on_click=lambda: os.remove(temp_path))


# # # # # if __name__ == '__main__':
# # # # #     main()

# # # # import os
# # # # import tempfile
# # # # import torch
# # # # from transformers import BertForQuestionAnswering, BertTokenizer
# # # # import streamlit as st
# # # # from pyngrok import ngrok

# # # # # Load the pre-trained model and tokenizer
# # # # model_name = 'bert-base-uncased'
# # # # model = BertForQuestionAnswering.from_pretrained(model_name)
# # # # tokenizer = BertTokenizer.from_pretrained(model_name)


# # # # def extract_text_from_file(file_path):
# # # #     _, file_extension = os.path.splitext(file_path)
# # # #     if file_extension == '.pdf':
# # # #         # Handle PDF files
# # # #         from PyPDF2 import PdfFileReader
# # # #         with open(file_path, 'rb') as f:
# # # #             pdf = PdfFileReader(f)
# # # #             text = ""
# # # #             for page_num in range(pdf.numPages):
# # # #                 page = pdf.getPage(page_num)
# # # #                 text += page.extract_text()
# # # #     else:
# # # #         # Handle text files
# # # #         with open(file_path, 'r') as f:
# # # #             text = f.read()
# # # #     return text


# # # # def answer_question(file_paths, question):
# # # #     context = ""
# # # #     for file_path in file_paths:
# # # #         context += extract_text_from_file(file_path)
# # # #     # Tokenize the inputs and handle long sequences
# # # #     inputs = tokenizer.encode_plus(question, context, add_special_tokens=True,
# # # #                                    return_tensors='pt', max_length=512, truncation_strategy='only_second')
# # # #     # Generate predictions
# # # #     start_logits, end_logits = model(**inputs).values()
# # # #     # Find the start and end indices with the highest logits
# # # #     start_index = torch.argmax(start_logits)
# # # #     end_index = torch.argmax(end_logits)
# # # #     # Get the tokens corresponding to the answer
# # # #     tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())
# # # #     answer = ' '.join(tokens[start_index:end_index + 1]).replace(' ##', '')
# # # #     return answer


# # # # def main():
# # # #     st.title("Question Answering from a Dataset of Text Documents")
# # # #     st.markdown(
# # # #         "Upload a dataset of text documents and ask a question to get the answer.")
# # # #     # File upload
# # # #     file_paths = []
# # # #     uploaded_files = st.file_uploader(
# # # #         "Upload a file", type=["pdf", "txt"], accept_multiple_files=True)
# # # #     for uploaded_file in uploaded_files:
# # # #         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
# # # #             temp_path = temp_file.name
# # # #             temp_file.write(uploaded_file.read())
# # # #             file_paths.append(temp_path)
# # # #     # Question input
# # # #     question = st.text_input("Enter your question")
# # # #     if file_paths and question != "":
# # # #         try:
# # # #             # Answer the question
# # # #             answer = answer_question(file_paths, question)
# # # #             # Display the answer
# # # #             st.markdown(f"**Question:** {question}")
# # # #             st.markdown(f"**Answer:** {answer}")
# # # #         except Exception as e:
# # # #             st.error(f"Error: {e}")
# # # #         # Remove temporary files
# # # #         st.button("Remove Temporary Files", on_click=lambda: [
# # # #                   os.remove(file_path) for file_path in file_paths])


# # # # if __name__ == '__main__':
# # # #     main()

import os
import tempfile
import torch
from transformers import BertForQuestionAnswering, BertTokenizer
import streamlit as st

# Load the pre-trained model and tokenizer
model_name = 'bert-base-uncased'
model = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)


def extract_text_from_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.pdf':
        # Handle PDF files
        from PyPDF2 import PdfFileReader
        with open(file_path, 'rb') as f:
            pdf = PdfFileReader(f)
            text = ""
            for page_num in range(pdf.numPages):
                page = pdf.getPage(page_num)
                text += page.extract_text()
    else:
        # Handle text files
        with open(file_path, 'r') as f:
            text = f.read()
    return text


def answer_question(file_paths, question):
    context = ""
    for file_path in file_paths:
        context += extract_text_from_file(file_path)
    # Tokenize the inputs and handle long sequences
    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True,
                                   return_tensors='pt', max_length=512, truncation_strategy='only_second')
    # Generate predictions
    start_logits, end_logits = model(**inputs).values()
    # Find the start and end indices with the highest logits
    start_index = torch.argmax(start_logits)
    end_index = torch.argmax(end_logits)
    # Get the tokens corresponding to the answer
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())
    answer = ' '.join(tokens[start_index:end_index + 1]).replace(' ##', '')
    return answer


def main():
    st.title("Question Answering from a Dataset of Text Documents")
    st.markdown(
        "Upload a dataset of text documents and ask a question to get the answer.")
    # File upload
    file_paths = []
    uploaded_files = st.file_uploader(
        "Upload a file", type=["pdf", "txt"], accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(uploaded_file.read())
            file_paths.append(temp_path)
    # Question input
    question = st.text_input("Enter your question")
    if file_paths and question != "":
        try:
            # Answer the question
            answer = answer_question(file_paths, question)
            # Display the answer
            st.markdown(f"**Question:** {question}")
            st.markdown(f"**Answer:** {answer}")
        except Exception as e:
            st.error(f"Error: {e}")
        # Remove temporary files
        st.button("Remove Temporary Files", on_click=lambda: [
                  os.remove(file_path) for file_path in file_paths])


if __name__ == '__main__':
    main()

# import os
# import tempfile
# import torch
# from transformers import BertForQuestionAnswering, BertTokenizer
# import streamlit as st


# # Load the pre-trained model and tokenizer
# model_name = 'bert-base-uncased'
# model = BertForQuestionAnswering.from_pretrained(model_name)
# tokenizer = BertTokenizer.from_pretrained(model_name)


# def extract_text_from_file(file_path):
#     _, file_extension = os.path.splitext(file_path)
#     if file_extension == '.pdf':
#         # Handle PDF files
#         from PyPDF2 import PdfFileReader
#         with open(file_path, 'rb') as f:
#             pdf = PdfFileReader(f)
#             text = ""
#             for page_num in range(pdf.numPages):
#                 page = pdf.getPage(page_num)
#                 text += page.extract_text()
#     else:
#         # Handle text files
#         with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
#             text = f.read()
#     return text




# def extract_text_from_folder(folder_path):
#     text = ""
#     for root, _, files in os.walk(folder_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             text += extract_text_from_file(file_path)
#     return text


# def answer_question(context, question):
#     # Tokenize the inputs and handle long sequences
#     inputs = tokenizer.encode_plus(question, context, add_special_tokens=True,
#                                    return_tensors='pt', max_length=512, truncation_strategy='only_second')
#     # Generate predictions
#     start_logits, end_logits = model(**inputs).values()
#     # Find the start and end indices with the highest logits
#     start_index = torch.argmax(start_logits)
#     end_index = torch.argmax(end_logits)
#     # Get the tokens corresponding to the answer
#     tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())
#     answer = ' '.join(tokens[start_index:end_index + 1]).replace(' ##', '')
#     return answer


# def main():
#     st.title("Question Answering from a Dataset of Text Documents")
#     st.markdown(
#         "Upload a folder containing text documents and ask a question to get the answer.")
#     # Folder upload
#     folder = st.file_uploader("Upload folder", type=[
#                               "zip"], accept_multiple_files=False, key="folder_uploader")
#     if folder is not None:
#         with tempfile.TemporaryDirectory() as temp_dir:
#             folder_path = os.path.join(temp_dir, folder.name)
#             os.makedirs(folder_path)
#             with open(os.path.join(folder_path, folder.name), "wb") as f:
#                 f.write(folder.getvalue())
#             # Extract text from the folder
#             context = extract_text_from_folder(folder_path)
#             # Question input
#             question = st.text_input("Enter your question")
#             if question != "":
#                 try:
#                     # Answer the question
#                     answer = answer_question(context, question)
#                     # Display the answer
#                     st.markdown(f"**Question:** {question}")
#                     st.markdown(f"**Answer:** {answer}")
#                 except Exception as e:
#                     st.error(f"Error: {e}")


# if __name__ == '__main__':
#     main()
# import os
# import tempfile
# import torch
# from transformers import DistilBertForQuestionAnswering, DistilBertTokenizer
# import streamlit as st
# import zipfile

# # Load the pre-trained model and tokenizer
# model_name = 'distilbert-base-uncased'
# model = DistilBertForQuestionAnswering.from_pretrained(model_name)
# tokenizer = DistilBertTokenizer.from_pretrained(model_name)


# def extract_text_from_file(file_path):
#     _, file_extension = os.path.splitext(file_path)
#     if file_extension == '.pdf':
#         # Handle PDF files
#         from PyPDF2 import PdfFileReader
#         with open(file_path, 'rb') as f:
#             pdf = PdfFileReader(f)
#             text = ""
#             for page_num in range(pdf.numPages):
#                 page = pdf.getPage(page_num)
#                 text += page.extract_text()
#     else:
#         # Handle text files
#         with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
#             text = f.read()
#     return text


# def answer_question(file_paths, question):
#     context = ""
#     for file_path in file_paths:
#         context += extract_text_from_file(file_path)
#     # Tokenize the inputs
#     inputs = tokenizer.encode_plus(
#         question, context, add_special_tokens=True, truncation=True, max_length=256, return_tensors='pt')
#     # Generate predictions
#     start_logits, end_logits = model(**inputs).values()
#     # Find the start and end indices with the highest logits
#     start_index = torch.argmax(start_logits)
#     end_index = torch.argmax(end_logits)
#     # Get the tokens corresponding to the answer
#     tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())
#     answer = ' '.join(tokens[start_index:end_index + 1]).replace(' ##', '')
#     return answer


# def main():
#     st.title("Question Answering from a Dataset of Text Documents")
#     st.markdown(
#         "Upload a zip file containing text documents and ask a question to get the answer.")
#     # File upload
#     file_paths = []
#     uploaded_file = st.file_uploader("Upload a zip file", type=["zip"])
#     if uploaded_file is not None:
#         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#             temp_path = temp_file.name
#             temp_file.write(uploaded_file.read())
#         with zipfile.ZipFile(temp_path, 'r') as zip_ref:
#             extract_dir = tempfile.mkdtemp()
#             zip_ref.extractall(extract_dir)
#             for root, dirs, files in os.walk(extract_dir):
#                 for file in files:
#                     file_paths.append(os.path.join(root, file))
#     # Question input
#     question = st.text_input("Enter your question")
#     if file_paths and question != "":
#         try:
#             # Answer the question
#             answer = answer_question(file_paths, question)
#             # Display the answer
#             st.markdown(f"**Question:** {question}")
#             st.markdown(f"**Answer:** {answer}")
#         except Exception as e:
#             st.error(f"Error: {e}")
#         # Remove temporary files
#         st.button("Remove Temporary Files", on_click=lambda: [
#                   os.remove(file_path) for file_path in file_paths])
#         if 'temp_path' in locals():
#             os.remove(temp_path)
#             os.rmdir(extract_dir)


# if __name__ == '__main__':
#     main()
