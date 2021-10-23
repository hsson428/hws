![screenshot](C:\Users\gudtj\hws\1021\screenshot.png)

#### views.py

- accounts

  ```python
  def profile(request, username):
      User = get_user_model()
      person = get_object_or_404(User, username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  
  
  @login_required
  def follow(request, user_pk):
      if request.method == 'POST':
          person = get_object_or_404(get_user_model(), pk=user_pk)
          if request.user != person:
              if request.user.followings.filter(pk=user_pk).exists():
                  request.user.followings.remove(person)
              else:
                  request.user.followings.add(person)
      return redirect('accounts:profile', person)
  
  
  @login_required
  def follows(request, user_pk, ings_or_wers):
      person = get_object_or_404(get_user_model(), pk=user_pk)
      followings = person.followings.all()
      followers = person.followers.all()
      context = {
          'followings': followings,
          'followers': followers,
          'ings_or_wers': ings_or_wers,
      }
      return render(request, 'accounts/follows.html', context)
  
  ```

- articles

  ```python
  def like(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.user.like_articles.filter(pk=pk).exists():
          request.user.like_articles.remove(article)
      else:
          request.user.like_articles.add(article)
      return redirect('articles:index')
  ```



#### models.py

- accounts

  ```python
  followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```

- articles

  ```python
  class Article(models.Model):
  	like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  ```

  



#### profile.html

```html
{% extends 'base.html' %}

{% block content %}
  <div>
    <span>{{ person }}</span>
    <a href="{% url 'accounts:follows' person.pk 'followings' %}">followings: {{ person.followings.all|length}}</a>
    <a href="{% url 'accounts:follows' person.pk 'followers' %}">followers: {{ person.followers.all|length}}</a>
  </div>

  {% if user != person %}
  <form action="{% url 'accounts:follow' person.pk %}" method="POST">
    {% csrf_token %}
    {% if person in user.followings.all %}
      <input type="submit" class="btn btn-secondary" value="팔로우취소">
    {% else %}
      <input type="submit" class="btn btn-primary" value="팔로우">
    {% endif %}
  </form>
  {% else %}
    <a href="{% url 'accounts:update' %}" class="btn btn-secondary">회원정보수정</a>
  {% endif %}

  <p>{% for article in person.article_set.all %}</p>
  <a href="{% url 'articles:detail' article.pk %}">{{ article }}</a> <span><i class="fas fa-heart" style="color: red"></i> {{ article.like_users.all|length }}</span>
  {% endfor %}
{% endblock content %}
```

