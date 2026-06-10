#1.select_related - SQL JOIN for FK/OneToOne

posts = Post.objects.select_related('auther','category')


# Prefetch_related
Posts = Post.objects.prefetch_related('tags')


#3 Only()

posts = Post.objects.only('id', 'title', 'created')


#4 value() -returns dict
Post.objects.values('id', 'title',).filter(published = True)