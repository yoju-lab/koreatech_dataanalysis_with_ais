FROM python:3.11

ARG GIT_BRANCH_NAME
ARG APP_DIR_NAME
ARG GIT_URI

# 기본 도구 설치
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /apps

# Clone the Git repository. Here we dynamically specify the repository name using the variable defined earlier.
RUN git clone -b ${GIT_BRANCH_NAME} ${GIT_URI} ${APP_DIR_NAME}

# Changes the working directory to /app/${REPO_NAME}. This uses the variable to dynamically set the directory path.
WORKDIR /apps/${APP_DIR_NAME}

RUN pip install --no-cache-dir -r ./requirements.txt

# RUN rm -rf .git