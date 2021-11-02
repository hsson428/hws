```javascript
<style>
    .red {color: rgb(223, 36, 36);}
    .black {color: black;}
</style>
<script>
  const hearts = document.querySelectorAll('.fa-heart')

  hearts.forEach(heart => {
    heart.addEventListener('click', event => {
      const articlePk = event.target.dataset.articlePk
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
        axios.post(`/articles/${articlePk}/likes/`, {}, {
          headers: { 'X-CSRFToken': csrftoken}
        })
          .then(res => {
            const {isLiking, likeCount} = res.data
            event.target.classList.toggle('fas')
            event.target.classList.toggle('far')
            if (isLiking) {
              event.target.classList.add('red')
            } else {
              event.target.classList.add('black')
            }
            const likeCountSpan = document.querySelector(`#like-count-${articlePk}`)
            likeCountSpan.innerText = likeCount
        })
    })
  })
</script>
```

