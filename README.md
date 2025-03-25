# koreatech_dataanalysis_with_ais

## Docker 설치 및 VS Code로 접근하는 방법

### Docker 설치

1. **Docker 다운로드 및 설치:** [Docker 공식 사이트](https://www.docker.com/products/docker-desktop)에서 Docker Desktop을 다운로드하여 설치합니다. 설치 과정에서 기본 설정을 그대로 사용하면 됩니다.
2. **Docker 실행:** 설치가 완료되면 Docker Desktop을 실행합니다. Docker가 정상적으로 실행되고 있는지 확인합니다.

### 프로젝트 클론 및 Docker 컨테이너 실행

1. **프로젝트 클론:** 터미널을 열고 다음 명령어를 입력하여 프로젝트를 클론합니다.
   ```bash
   git clone https://github.com/yourusername/koreatech_dataanalysis_with_ais.git
   cd koreatech_dataanalysis_with_ais
   ```
2. **Docker 컨테이너 실행:** 클론한 프로젝트 디렉토리에서 다음 명령어를 실행하여 Docker 컨테이너를 빌드하고 실행합니다.
   ```bash
   docker-compose up --build
   ```

### VS Code로 접근

1. **VS Code 열기:** Visual Studio Code를 실행합니다.
2. **Remote - Containers 확장 설치:** VS Code의 확장 마켓플레이스에서 **Remote - Containers** 확장을 설치합니다.
3. **컨테이너에 연결:** VS Code 왼쪽 하단의 **><** 아이콘을 클릭하고 **Remote-Containers: Attach to Running Container...**를 선택합니다. 실행 중인 Docker 컨테이너 목록에서 해당 프로젝트의 컨테이너를 선택합니다.
4. **개발 환경 설정:** 컨테이너에 연결되면, VS Code 내에서 프로젝트 파일을 열고 개발을 시작할 수 있습니다.

이제 Docker 컨테이너 내에서 VS Code를 사용하여 프로젝트를 개발할 수 있습니다.