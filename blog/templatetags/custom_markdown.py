# -*- coding: utf-8 -*-
import re

import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def custom_markdown(value):
    # extensions = ["nl2br", ]

    return mark_safe(markdown.markdown(value,
                                       extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))
    # return mark_safe(markdown2.markdown(force_text(value),
    # extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))


@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def clear_css_img(value):
    imgurlcp = re.compile(r'http.*\.(png|jpg|gif)')  # 匹配图片
    try:
        imgurl = r'<a href="' + re.search(imgurlcp, value).group(0) + r'">[图片]</a>'
    except AttributeError:
        imgurl = r'<a href="https://www.baidu.com">https://www.baidu.com</a>'
    imgtag = re.compile(r'<img.*/>')
    value = re.sub(imgtag, imgurl, value)
    value = re.sub(r'<h\d>', '<p>', value)
    value = re.sub(r'</h\d>', '</p>', value)
    print(value)
    return value
