import zipfile
with zipfile.ZipFile("nturgb+d_skeletons.zip","r") as zip_ref:
	zip_ref.extractall('/home/natepidl/Downloads/SNU-Subjects/GCN/FinalProject/NAS_FinalExam')
