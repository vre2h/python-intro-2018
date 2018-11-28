class LetterAttr:
    res = ''
    isName = False

    def __getattr__(self, arg):
        return LetterAttr.res if LetterAttr.res or LetterAttr.isName else arg

    def __setattr__(self, attr, val):
        formatted = ''

        for i in val:
            if i in attr:
                formatted += i

        LetterAttr.isName = True
        LetterAttr.res = formatted

        return formatted
