import sys
from sentence_transformers import SentenceTransformer, util
import torch
from benchmark_util import create_images_list, load_image
from database_config import get_data
import siglip_256_multilingual
import numpy as np
from sentense_transformer_multilingual import get_embeddings

def main():

    data_rows, img_list = get_data()
    images = [load_image(img_row) for img_row in img_list]
    cleaned_images = [img for img in images if img is not None]

    img_embeddings, text_embeddings = get_embeddings(data_rows, cleaned_images)
    
    np.savetxt('output_files/image_embeddings.txt', img_embeddings)
    np.savetxt('output_files/text_embeddings.txt', text_embeddings)

    # probs_output = siglip_256_multilingual.siglip_miltilingual_model(data_rows, cleaned_images)
    # np.savetxt('multilingual_probs.txt',probs_output)
    
    # code to add image embeddings and text embeddings to mysql database. 
    cos_sim = util.cos_sim(text_embeddings, img_embeddings)
    
    with open("output_files/consine_similarity_with_sentense_transformer.txt", "w") as f:
        for text, scores in zip(data_rows, cos_sim):
            max_img_idx = torch.argmax(scores)
            print("Text:", text)
            print("Score:", scores[max_img_idx] )
            print("Path:", img_list[max_img_idx], "\n")
            f.write(f"Score: {scores[max_img_idx]} \n")
    
    return 0;

    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(1)
