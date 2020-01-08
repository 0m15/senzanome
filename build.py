import time
start = time.time()

from senzanome import clear, create_nodes, create_index, create_page, copy_static_files

# rm the public dir
clear()

create_nodes('./src/contents/blog/*.md', 'components/Post.html')
create_nodes('./src/contents/works/*.md', 'components/Post.html')
create_nodes('./src/contents/*.md', 'components/Post.html')

# create indexes/archives pages
blog = create_index('./src/contents/blog/*.md', 'components/PostList.html', 'components/PostItem.html')
works = create_index('./src/contents/works/*.md', 'components/PostList.html', 'components/PostItem.html')
pages = create_index('./src/contents/*.md', 'components/PostList.html', 'components/PostItem.html') 
create_page('Home', 'index.html', 'templates/home.html', {'works': works, 'blog': blog })
create_page('Blog', 'blog/index.html', 'templates/blog.html', {'content': blog })
create_page('Works', 'works/index.html', 'templates/works.html', {'content': works })

copy_static_files()

end = time.time()

print(' ------------------------------- ')
print(' ✓ Done in %0.3fs' % ((end - start)))
print(' ')