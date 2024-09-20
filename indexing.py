#-------------------------------------------------------------------------
# AUTHOR: Dat Nguyen
# FILENAME: TF_IDF Calculation
# SPECIFICATION: Manually calculating TF_IDF Matrix
# FOR: CS 5180- Assignment #1
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"i", "and", "she", "they", "her", "their"}
documents = [" ".join([word for word in doc.split() if word.lower() not in stopWords]) for doc in documents]
# #Conducting stemming. Hint: use a dictionary to map word variations to their stem.
# #--> add your Python code here
stemming = {"cats": "cat", "dogs": "dog", "loves": "love"}

documents = [" ".join([stemming.get(word, word) for word in doc.split()]) for doc in documents]

#Identifying the index terms.
#--> add your Python code here
terms = []
for doc in documents:
    for term in doc.split():
        if term not in terms:
            terms.append(term)
n = len(documents)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
for doc in documents:
    docTermMatrix.append([])

idfTerm = []
for i in terms:
    df_tD = 0
    for idx, doc in enumerate(documents):
        isAppeared = False
        cnt = 0
        for word in doc.split():
            if word == i:
                cnt +=1
                if not isAppeared:
                    df_tD+=1
                    isAppeared = True
        df_td = cnt / len(doc.split())
        docTermMatrix[idx].append(df_td)
    idfTerm.append(math.log10(n/df_tD))

for i, row in enumerate(docTermMatrix):
    for j, col in enumerate(row):
        docTermMatrix[i][j]= round(docTermMatrix[i][j]*idfTerm[j], 2)



#Printing the document-term matrix.
#--> add your Python code here
# print(docTermMatrix)
print("------------Document Term Matrix------------")
def print_table(data, index, columns):
    # Get the width for each column for better formatting
    col_widths = [max(len(str(col)), max(len(str(row[i])) for row in data)) for i, col in enumerate(columns)]
    row_width = max(len(str(i)) for i in index)

    # Create header row
    header = f"{' ' * (row_width + 2)}" + "  ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(columns))
    print(header)

    # Print each row with index
    for idx, row in zip(index, data):
        row_str = f"{idx:<{row_width}}  " + "  ".join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row))
        print(row_str)

index = ["d1", "d2", "d3"]
print_table(docTermMatrix, index, terms)