from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHeaderView, QToolBar, QMessageBox, QInputDialog
from PySide6.QtGui import QIcon, QAction
import sys
import shutil
import os
import subprocess


class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Explorer")
        self.resize(800, 600)

        # Central Widget and Layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Tree View and File System Model
        self.tree_view = QTreeView()
        self.model = QFileSystemModel()
        self.model.setRootPath("")  # Set root to the whole file system or specific path

        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index("D:/"))  # Change to a desired starting directory
        self.tree_view.setIndentation(20)  # Indentation for child elements
        self.tree_view.setHeaderHidden(True)  # Hide the header if you don't need it

        # Show only the first column (Name)
        # for column in range(1, self.model.columnCount()):  # Hide all columns except the first
            # self.tree_view.setColumnHidden(column, True)
        # self.tree_view.setColumnHidden(1, True)

        # Customize header appearance (optional)
        header = self.tree_view.header()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # Stretch the first column
        header.setVisible(True)  # Hide the header for a cleaner look

        # Increase font size
        font = self.tree_view.font()
        font.setPointSize(10)  # Adjust the font size
        self.tree_view.setFont(font)

        # adding toolbar for cut, copy and paste
        toolbar = QToolBar("File operations")
        self.addToolBar(toolbar)

        # toolbar action
        cut_action = QAction(QIcon.fromTheme("edit-cut"), "cut", self)
        copy_action = QAction(QIcon.fromTheme("edit-copy"), "copy", self)
        paste_action = QAction(QIcon.fromTheme("edit-paste"), "paste", self)
        # action "open in file explorer"
        open_explorer_action = QAction(QIcon.fromTheme("folder-open"), "Open in file explorer", self)
        # rename action
        rename_action = QAction(QIcon.fromTheme("edit-rename"), "rename", self)

        # connect action
        cut_action.triggered.connect(self.cut_file)
        copy_action.triggered.connect(self.copy_file)
        paste_action.triggered.connect(self.paste_file)
        open_explorer_action.triggered.connect(self.open_in_explorer)
        rename_action.triggered.connect(self.rename_file_or_folder)

        # add action to toolbar
        toolbar.addAction(cut_action)
        toolbar.addAction(copy_action)
        toolbar.addAction(paste_action)
        toolbar.addAction(open_explorer_action)
        toolbar.addAction(rename_action)


        layout.addWidget(self.tree_view)

        # clipboard
        self.clipboard = {"path":None, "operation":None}
    
    def get_selected_path(self):
        # Path to selected item in the tree view
        index = self.tree_view.currentIndex()
        if index.isValid():
            return self.model.filePath(index)
        return None

    def rename_file_or_folder(self):
        path = self.get_selected_path()
        if path:
            base_dir = os.path.dirname(path)
            current_name = os.path.basename(path)

            # Prompt for the new name
            new_name, ok = QInputDialog.getText(self, "Rename", "Enter new name:", text=current_name)
            
            if ok and new_name.strip():
                new_path = os.path.join(base_dir, new_name.strip())
                try:
                    os.rename(path, new_path)
                    print(f"Renamed to: {new_path}")
                except Exception as e:
                    print(f"Error renaming: {e}")
            else:
                print("Rename cancelled or invalid name.")
        else:
            print("No file or folder selected.")
    
    def open_in_explorer(self):
        # open file/folder in system's explorer
        path = self.get_selected_path()
        if path:
            if os.path.exists(path):
                import pathlib
                path_ = pathlib.Path(path)
                print(f'Explorer.exe /root,"{path_}"')
                subprocess.run(f'Explorer.exe /root,"{path_}"', shell=True)
            else:
                print("Path does not exist")
        else:
            print("No file or folder selected")

    def copy_file(self):
        # copying the file
        path = self.get_selected_path()
        if path:
            self.clipboard = {"path": path, "operation": "copy"}
            QMessageBox.information(self, "Copy", f"Copied: {os.path.basename(path)}")
        else:
            QMessageBox.warning(self, "Copy", "No file or folder selected.")

    def cut_file(self):
        # cut the file
        path = self.get_selected_path()
        if path:
            self.clipboard = {"path": path, "operation": "cut"}
            QMessageBox.information(self, "Cut", f"Cut: {os.path.basename(path)}")
        else:
            QMessageBox.warning(self, "Cut", "No file or folder selected.")

    def paste_file(self):
        # paste the file
        target_path = self.get_selected_path()
        if target_path and os.path.isdir(target_path):
            src_path = self.clipboard.get("path")
            operation = self.clipboard.get("operation")

            if not src_path or not operation:
                QMessageBox.warning(self, "Paste", "Nothing to paste.")
                return

            dest_path = os.path.join(target_path, os.path.basename(src_path))

            try:
                if operation == "copy":
                    if os.path.isdir(src_path):
                        shutil.copytree(src_path, dest_path)
                    else:
                        shutil.copy2(src_path, dest_path)
                    QMessageBox.information(self, "Paste", f"Copied to: {dest_path}")
                elif operation == "cut":
                    shutil.move(src_path, dest_path)
                    QMessageBox.information(self, "Paste", f"Moved to: {dest_path}")

                # Clear clipboard after operation
                self.clipboard = {"path": None, "operation": None}

            except Exception as e:
                QMessageBox.critical(self, "Paste Error", str(e))
        else:
            QMessageBox.warning(self, "Paste", "Select a folder to paste into.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec())