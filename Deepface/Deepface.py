from deepface import DeepFace

dfs = DeepFace.find(
  img_path = "D:\\flutter_projects\\Deepface\\images.jpg",
  db_path = "Database/",
)
print(dfs)
