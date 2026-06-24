import pytest
import os
import ast
import glob

def test_python_syntax_integrity():
    # Recursively find all python files in the directory to ensure advanced scripts compile cleanly
    base_dir = os.path.dirname(os.path.dirname(__file__))
    python_files = glob.glob(os.path.join(base_dir, "**/*.py"), recursive=True)
    
    # Assert that all files compile into valid ASTs without SyntaxErrors
    for py_file in python_files:
        with open(py_file, 'r', encoding='utf-8') as f:
            source = f.read()
        try:
            ast.parse(source, filename=py_file)
        except SyntaxError as e:
            pytest.fail(f"Syntax error in {os.path.basename(py_file)}: {e}")
