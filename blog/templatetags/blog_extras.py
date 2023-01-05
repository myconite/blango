from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django import template
from blog.models import Post


user_model = get_user_model()
register = template.Library() # register is a good var name to reg and init the filter func

### Filter Function ###

@register.filter(name="author_details") # can be empty eg. @register.filter w/o name if function name same
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    # return empty string as safe default
    return ''

  if author == current_user:
    return format_html("<strong>me</strong>")

  if author.first_name and author.last_name:
    name = f'{author.first_name} {author.last_name}'
  else:
    name = f'{author.username}'

  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html('</a>')
  else:
    prefix = ""
    suffix = ""

  return format_html('{}{}{}', prefix, name, suffix)

### Custom Template Tags ###

@register.simple_tag(name="row")
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)

@register.simple_tag(name="endrow")
def endrow():
    return format_html('</div>')

@register.simple_tag(name="col")
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)

@register.simple_tag(name="endcol")
def endcol():
    return format_html("</div>")



@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}