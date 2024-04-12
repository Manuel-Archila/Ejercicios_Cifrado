import hashlib

# Function that takes a document path and returns a hash of the document
def hash_document(document_path):
    with open(document_path, 'rb') as document:
        document_content = document.read()
        return hashlib.sha256(document_content).hexdigest()


calculated_hash = hash_document('document.txt')
actual_hash = ""

if calculated_hash == actual_hash:
    print("The document is valid")
else:
    print("The document is not valid")