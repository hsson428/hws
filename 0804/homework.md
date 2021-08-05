#### 1. Block Button

```html
<div class="d-grid gap-2 col-2 mx-auto">
  <button class="btn btn-success" type="button">Sign in</button>
</div>
```



#### 2. Navs

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="">
    </a>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              프로젝트
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              그룹들
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          </ul>
        </li>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
        </ul>
        <li class="nav-item">
          <a class="nav-link" href="#">활동</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">마일스톤</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">스니펫</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```



#### 3. Pagination > Disabled and active states

```html
<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item disabled">
      <a class="page-link" href="#">Previous</a>
    </li>
    <li class="page-item active" aria-current="page">
      <a class="page-link" href="#">1</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">4</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```



#### 4. Alerts

```html
<div class="container ">
  <div class="alert alert-danger" role="alert">
    Invalid Login or password.
  </div>
  <h1>SSAFY 전용 Gitlab 시스템</h1>
  <hr>
  <div class="Sign-in border">
    <div class="text-center fw-bold border-bottom p-3">
        Sign in
    </div>
    <div class="Sign-in-form p-3">
      <form action="">
        <div class="fw-bold my-2">Username or email</div>
        <input type="text">
        <div class="fw-bold my-2">Password</div>
        <input type="text">
        <br>
        <div class="d-flex justify-content-between fw-bold my-2">
          <div>
            <input type="checkbox" id="remember-me" name="remember-me" value="1">
            <label for="remember-me">Remember me</label>
          </div>
          <a href="#" class="text-decoration-none">Forgot your password?</a>
        </div>
        <div class="d-grid gap-2 mx-auto">
          <button class="btn btn-success" type="button">Sign in</button>
        </div>
      </form>
    </div>
  </div>
</div>
```

