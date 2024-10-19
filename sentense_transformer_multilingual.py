import sentence_transformers
from benchmark_util import load_image

def get_embeddings(data_rows, img_list):

    img_model = sentence_transformers.SentenceTransformer('clip-ViT-B-32')
    text_model = sentence_transformers.SentenceTransformer('sentence-transformers/clip-ViT-B-32-multilingual-v1')
    
    img_embeddings = img_model.encode(img_list)
    text_embeddings = text_model.encode(data_rows)

    return img_embeddings, text_embeddings
