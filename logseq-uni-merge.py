# very simple script for unidirectional merging of two graphs
# note: no assets 
# tags: logseq, log-seq, merge, merging, graphs, unidirectional

import os
import shutil

source_graph_path = "place_path_to_src_repo_here" # for example: ~/logseq-note-mobile
destination_graph_path = "place_path_to_dest_repo_here" #for example: ~/log-seq-note
# for journals files are used mobij workspace, for pages mobi workspace
prefix_map = {
  "journals": "mobij",
  "pages": "mobi"
}

def copy_and_rename(source_folder, dest_folder, prefix):
  """Copies files from source to destination, adding workspace prefixes."""
  os.makedirs(dest_folder, exist_ok=True)  # Create destination if needed

  for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    workspace_prefix = prefix + "___"  # Add workspace delimiter
    dest_path = os.path.join(dest_folder, f"{workspace_prefix}{filename}")
    shutil.copyfile(source_path, dest_path)
    print(f"Copied '{source_path}' to '{dest_path}'")

if __name__ == "__main__":
  for folder_key, prefix in prefix_map.items():
    source_folder = os.path.join(source_graph_path, folder_key)
    dest_folder = os.path.join(destination_graph_path, folder_key)

    copy_and_rename(source_folder, dest_folder, prefix)
