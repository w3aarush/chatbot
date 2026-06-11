def chatbot():

    import pandas as pd
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from sentence_transformers import util
    # --------------Loading Data----------------------------------------
    data = pd.read_csv('./chatdata.csv')    # reading the chat data
    
    user_input = list(data['user_input'])   # changing the user_input column from chatdatat ot list
    response_msg = list(data['response_msg'])   # changing response message
    # --------------Load embedding model----------------------------------
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # --------------Create Embeddings for existing user input
    input_embeddings = model.encode(user_input)

    # ---------------Similarity Function-------------------------------------
    # def cosine_similarity(a, b):
    #     return np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))

    
    # i1 = list(enumerate(user_input))    # indexing the user_input
    # r1 = list(enumerate(response_msg))  #indexing the response_msg


    while True:
        message = input('user: -> ')    # taking user input
        if message.lower() == 'exit':           # to exit if user types 'exit'
            print('bye! take care')
            # print('here is your updated list')
            updated_data = {'user_input':user_input,
                            'response_msg':response_msg
            }                                               # binding updated data in dictionary
            data = pd.DataFrame(updated_data)               # changed updated into dataframe
            data.to_csv('./chatdata.csv')                   # exported into csv format
            break

        # encoding user message
        message_embedding = model.encode(message)

        # finding similarity
        similarities = [
            util.pytorch_cos_sim(message_embedding, emb)
            for emb in input_embeddings
        ]

        # similarities2 = util.semantic_search(
        #     query_embeddings=message_embedding,
        #     corpus_embeddings=input_embeddings,
        #     top_k=1
        # )

        best_match_index = np.argmax(similarities)
        best_score = similarities[best_match_index]

        # ---------------threshold decision-------------------------------------
        THRESHOLD = 0.5

        if best_score >= THRESHOLD:
            print(f"bot: => {response_msg[best_match_index]} (sim={best_score.tolist()[0][0]:.2f})")

        else:
            print("Sorry, didn't get that")
            user_input.append(message)

            print("please tell me, what should have been my response here.")
            new_response = input()

            response_msg.append(new_response)

            # updating embeddings
            new_embedding = model.encode(message)
            input_embeddings = np.vstack([input_embeddings, new_embedding])

            print("thanks buddy, now I know. Try asking my again.")
            continue
'''
        text_num = None
        if message in user_input:
            for num, text in i1:
                if text==message:
                    text_num = num
        else:
            print("sorry, didn't get that")
            user_input.append(message)
            print('please tell me, what should have been my response here.')
            new_response = input()
            response_msg.append(new_response)
            i1 = list(enumerate(user_input))
            r1 = list(enumerate(response_msg))
            print('thanx buddy, now I know. Try asking me again.')
            continue
        for num, text in r1:
            if num == text_num:
                print(f'bot: => {text}')
'''
chatbot()