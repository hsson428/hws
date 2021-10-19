```python
def comment_create(request, pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id = pk
        comment.save()
    return redirect('articles:detail', pk)


def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', comment.article_id)

def detail():
    comment_form = CommentForm()
```

