Understanding the role of context and global features in object recognition

Dataset used: Microsoft COCO - 90 object categories in real, natural scenes



1. Extract low level, global feature descriptors like GIST

2. Train using these features and retain contender images if loss of accuracy is under limits.

3. Apply semantic features - i) Co-occurence          (Add more)

4. Apply spatial features - i) Relative positioning   (Add more)

5. Apply geometric features- i) Relative size         (OPTIONAL)

6. Model the above features using a conditional random field to get top object category suggestions

