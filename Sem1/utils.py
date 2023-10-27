from Sem1.models import Author, Article, Comment


def get_arts_by_name(author: str, sort_param: str = 'pub_date', limit: int = 5):
    author = Author.objects.filter(name=author)
    articles = Article.objects.filter(author=author).order_by(sort_param)[:limit]
    return articles


def get_comments_by_name(author: str, sort_param: str = 'category', limit: int = 5):
    author = Author.objects.filter(name=author)
    comments = Comment.objects.filter(author=author).order_by(sort_param)[:limit]
    return comments


def get_comments_by_art(name: str, sort_param: str = 'category', limit: int = 5):
    comments = Comment.objects.filter(name=name).order_by(sort_param)[:limit]
    return comments