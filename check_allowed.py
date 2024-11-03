def allowed_files(file_name):
    allowed = {'.py', '.java', 'c', 'cpp', '.ml', '.rs', '.lua'}
    file_ext = file_name[file_name.rfind('.'):]
    print(file_ext)
    return file_ext if file_ext in allowed else None


comp_cmd_map = {
    '.rs': 'cargo run',
    '.c': 'gcc',
    '.py': 'python3',
    '.cpp': 'gcc',
    '.java': 'java'
}
