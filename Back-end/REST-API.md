# REST API

## Before the REST API

```
/createMovie
/seeMovies
/getMovie/harrypoter
/deleteMovie/harrypoter
/updateMovie/harrypoter
/getTopRateMovies
/findMoviesFromThisYear
```

위와 같이 API를 설계하는 것은 명확한 패턴이 없어 다른 사람이 이해하기 힘들고 효율적이지 못하다.

---

<h3>API설계를 효율적으로 하기위해서 REST API 같은 표준이 필요했다.</h3>
REST API는 아래와 같은 규칙을 따른다.

- URL에서 동사를 사용하지 않는다.

- HTTP 메소드를 이용하여 데이터를 요청한다.

```
/Movies //-> Collection

// Element
GET /Movie/harrypoter
PUT /Movie/harrypoter
DELETE /Movie/harrypoter
UPDATE /Movie/harrypoter
/Movies?min_rating=9.8
/Movies?release_date=2021
```

/Movie/harrypoter + HTTP 메소드를 이용한 URL로 이전보다 이해하기 쉽고 효율적으로 API설계가 가능해졌다. 또한 Query Parameters를 이용하여 이해하기 쉬운 API를 만들 수 있다.
