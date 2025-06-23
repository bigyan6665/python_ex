import os

all_files_path = os.path.join("exercises\\14library", "all_files")
all_files = os.listdir(all_files_path)  # list
print(f"Before separation: Total files = {len(all_files)}")

programs = [file for file in all_files if file.endswith(".py")]
documents = [file for file in all_files if file.endswith(".txt")]

programs_path = os.path.join(all_files_path, "Programs")
os.makedirs(programs_path, exist_ok=True)
documents_path = os.path.join(all_files_path, "Documents")
os.makedirs(documents_path, exist_ok=True)

for program in programs:
    src = os.path.join(all_files_path, program)
    dest = os.path.join(programs_path, program)
    os.rename(src, dest)  # moving files

for document in documents:
    src = os.path.join(all_files_path, document)
    dest = os.path.join(documents_path, document)
    os.rename(src, dest)

print(
    f"After separation: Total files = {len(os.listdir(programs_path)) + len(os.listdir(documents_path))}"
)
