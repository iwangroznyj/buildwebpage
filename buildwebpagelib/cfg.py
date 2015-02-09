RE_TEMPL_TITLE = _RE_COMMENT.format(SUBST_TITLE)
RE_TEMPL_CONTENT = _RE_COMMENT.format(SUBST_CONTENT)
# We don't know what the menuid will be, so the regex gets a replacement field
RE_TEMPL_MENUID = _RE_ATTRIBUTE.format(SUBST_ATTRIBUTE, '{0}')
