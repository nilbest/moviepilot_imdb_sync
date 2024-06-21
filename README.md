# moviepilot_imdb_sync

## Project Overview
This project synchronizes movie ratings between Moviepilot and IMDb accounts by extracting user ratings from each site and adding missing ratings to the other.

## Setup Instructions

### Prerequisites
- Python 3.x
- `pip` (Python package installer)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/nilbest/moviepilot_imdb_sync.git
    cd moviepilot_imdb_sync
    ```

2. Set up a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install required libraries:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

#### Using Environment Variables
1. Install `python-dotenv`:
    ```sh
    pip install python-dotenv
    ```

2. Create a `.env` file in the root directory and add your credentials:
    ```env
    MOVIEPILOT_USERNAME=your_moviepilot_username
    MOVIEPILOT_PASSWORD=your_moviepilot_password
    IMDB_USERNAME=your_imdb_username
    IMDB_PASSWORD=your_imdb_password
    ```

3. Ensure `.env` is added to `.gitignore`:
    ```gitignore
    .env
    ```

#### Using Configuration File
1. Copy `config_template.py` to `config.py`:
    ```sh
    cp config_template.py config.py
    ```

2. Edit `config.py` and add your credentials.

## Project Tasks and Goals

### Phase 1: Initial Research and Setup
- [ ] **Task 1**: Research Website Structures
  - **Goal**: Understand the HTML structure of Moviepilot and IMDb rating pages.
- [ ] **Task 2**: Setup Project Environment
  - **Goal**: Set up your development environment with necessary libraries.

### Phase 2: Web Scraping and Data Extraction
- [ ] **Task 3**: Scrape Moviepilot Ratings
  - **Goal**: Extract ratings from your Moviepilot account.
- [ ] **Task 4**: Scrape IMDb Ratings
  - **Goal**: Extract ratings from your IMDb account.

### Phase 3: Data Handling and Comparison
- [ ] **Task 5**: Store and Manipulate Data with Pandas
  - **Goal**: Organize the extracted data using Pandas.
- [ ] **Task 6**: Compare Ratings Data
  - **Goal**: Identify missing ratings between Moviepilot and IMDb.

### Phase 4: Automation for Adding Ratings
- [ ] **Task 7**: Automate Adding Ratings to Moviepilot
  - **Goal**: Automatically add missing ratings to Moviepilot.
- [ ] **Task 8**: Automate Adding Ratings to IMDb
  - **Goal**: Automatically add missing ratings to IMDb.

### Phase 5: Error Handling and Logging
- [ ] **Task 9**: Implement Error Handling
  - **Goal**: Add robust error handling to your scripts.
- [ ] **Task 10**: Add Logging
  - **Goal**: Log the operations to track the synchronization process.

### Phase 6: Environment Setup for Users
- [ ] **Task 11**: Manage Credentials Securely
  - **Goal**: Ensure credentials are not exposed and can be configured by users.
- [ ] **Task 12**: Provide Configuration Template
  - **Goal**: Allow users to configure the project with their own credentials.

### Phase 7: Final Testing and Polish
- [ ] **Task 13**: Conduct Final Tests
  - **Goal**: Ensure the entire workflow is seamless and bug-free.
- [ ] **Task 14**: Code Review and Refactoring
  - **Goal**: Improve code quality and maintainability.
- [ ] **Task 15**: Update Documentation
  - **Goal**: Ensure comprehensive and clear documentation.

## Progress Tracking

| Task | Description | Status |
|------|-------------|--------|
| Task 1 | Research Website Structures | Not Started |
| Task 2 | Setup Project Environment | Not Started |
| Task 3 | Scrape Moviepilot Ratings | Not Started |
| Task 4 | Scrape IMDb Ratings | Not Started |
| Task 5 | Store and Manipulate Data with Pandas | Not Started |
| Task 6 | Compare Ratings Data | Not Started |
| Task 7 | Automate Adding Ratings to Moviepilot | Not Started |
| Task 8 | Automate Adding Ratings to IMDb | Not Started |
| Task 9 | Implement Error Handling | Not Started |
| Task 10 | Add Logging | Not Started |
| Task 11 | Manage Credentials Securely | Not Started |
| Task 12 | Provide Configuration Template | Not Started |
| Task 13 | Conduct Final Tests | Not Started |
| Task 14 | Code Review and Refactoring | Not Started |
| Task 15 | Update Documentation | Not Started |

## Contributions
Feel free to fork this repository and contribute by submitting a pull request. Please ensure your changes are well-documented and tested.

## License
This project is licensed under the MIT License.
