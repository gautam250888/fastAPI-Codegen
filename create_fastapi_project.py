#!/usr/bin/env python3
import os
import argparse
from pathlib import Path

BASE_STRUCTURE = {
    "app": {
        "api": {"__init__.py": "", "v1": {"__init__.py": "", "routes.py": ""}},
        "core": {"__init__.py": "", "config.py": ""},
        "models": {"__init__.py": ""},
        "schemas": {"__init__.py": ""},
        "services": {"__init__.py": ""},
        "main.py": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI project generator works!"}
"""
    },
    "requirements.txt": """fastapi
uvicorn[standard]
pydantic
sqlalchemy
""",
    "README.md": "# New FastAPI Project"
}


def create_files(base_path, structure):
    for name, content in structure.items():
        path = Path(base_path) / name

        if isinstance(content, dict):
            # Make folder
            path.mkdir(parents=True, exist_ok=True)
            create_files(path, content)
        else:
            # Make file
            with open(path, "w") as f:
                f.write(content)


def main():
    parser = argparse.ArgumentParser(description="FastAPI Project Generator")
    parser.add_argument("project_name", help="Name of the project folder")
    args = parser.parse_args()

    project_path = Path(args.project_name)

    if project_path.exists():
        print(f"Error: Directory '{args.project_name}' already exists.")
        return

    print(f"Creating FastAPI project: {args.project_name}")
    create_files(project_path, BASE_STRUCTURE)
    print("Project created successfully!")
    print(f"\nTo run:\n  cd {args.project_name}\n  uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()

# To run:
#   cd project_name
#   uvicorn app.main:app --reload