# Instagram Follower Tracker

A script that looks at your Instagram follower data

## Prerequisites

### 1. Export Your Instagram Data

1. Open Instagram and navigate to your profile
2. Click the three lines in the top right corner
3. Go to **Settings** > **Account Center**
4. Select **Your information and permissions**
5. Click **Download your information** > **Request a download**
6. Choose **Download to device**
7. Under **Select types of information**:
   - Select only **Followers and following** from the Connections category
   - Deselect all other options
8. Set **Date range** to **All time**
9. Set **Format** to **JSON**
10. Click **Create files**
11. Wait for the download to be ready (you'll receive an email notification)
12. Download and unzip the file
13. Move the `followers_and_following` directory into this project directory

### 2. Install Python

Ensure you have Python 3 installed on your system. Check by running:
```bash
python3 --version
```

## Usage

Run the script:
```bash
python3 follower_tracker.py
```