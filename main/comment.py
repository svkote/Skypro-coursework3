class Post:
    def __init__(self, post_id, commenter_name, comment, pk):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk

    def __repr__(self):
        return f'Комментарий от {self.commenter_name}, ID: {self.pk}'
