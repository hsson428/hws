![screenshot](C:\Users\gudtj\hws\1020\screenshot.png)

#### views.py

```python
@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.like_articles.filter(pk=article_pk).exists():
        request.user.like_articles.remove(article)
    else:
        request.user.like_articles.add(article)
    return redirect('articles:index')
```



#### models.py

```python
class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```



#### index.html

```html
<form action="{% url 'articles:like' article.pk %}" method="POST" id="like-form-{{article.pk}}">
  {% csrf_token %}
</form>
{% if user in article.like_users.all %}
  <a href="#" onclick="document.querySelector('#like-form-{{article.pk}}').submit()"><i class="fas fa-heart" style="color: red"></i></a>
{% else %}
  <a href="#" onclick="document.querySelector('#like-form-{{article.pk}}').submit()"><i class="far fa-heart" style="color: black"></i></a>
{% endif %}
<a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
<p>{{ article.like_users.all|length }} likes</p>
```

