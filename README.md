## FastAPI Study

패키지 시스템으로는 [Poetry](https://python-poetry.org/)를 사용했습니다.

다음과 같이 Poetry를 설치하고 의존성을 설치합니다.

```sh
pip install poetry
poetry install
```

설치된 의존성은 Poetry를 이용하여 사용합니다.

```sh
poetry shell
```

각 장의 내용들은 다음과 같은 방식으로 수행합니다.

```sh
cd week1
uvicorn homework:app --reload
```

### 스터디

 * [Week 1](/week1)